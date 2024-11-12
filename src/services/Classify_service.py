import redis
import json
from hashlib import sha256
from response import ResponseHttp
from config import *
from llms import GPT_4o_mini
import os

# Khởi tạo GPT model và Redis client
gpt = GPT_4o_mini()
cache = redis.StrictRedis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    db=0,
    password=os.getenv("REDIS_PASSWORD"),
    decode_responses=True
)

# Check if the cache is running
try:
    cache.set("test_key", "test_value")
    if cache.get("test_key") == "test_value":
        print("Cache is running and accessible.")
    else:
        print("Cache is not accessible.")
except redis.ConnectionError as e:
    print(f"Error connecting to Redis cache: {e}")

with open(pathConfigure.DATA_PATH, 'r', encoding='utf-8') as f:
    DATA_VSIC = json.load(f)

def generate_cache_key(data):
    key_data = json.dumps(data, sort_keys=True)
    return sha256(key_data.encode()).hexdigest()

def getVsicData(main_category, sub_category):
    corpus = DATA_VSIC[main_category][sub_category]
    return corpus

async def classify_request_logic(requestInput):
    try:
        if not requestInput:
            return ResponseHttp().getResponse(400, "Request input is empty")
        
        request_data = requestInput.dict()
        cache_key = generate_cache_key(request_data)

        print("Cache key: ", cache_key)

        try:
            cached_response = cache.get(cache_key)
            print("Cached response: ", cached_response)
            if cached_response:
                return json.loads(cached_response)
        except redis.ConnectionError as e:
            print(f"Error retrieving from Redis cache: {e}")
            return ResponseHttp().getResponse(500, f"Error retrieving from cache: {str(e)}")
        except redis.AuthenticationError as e:
            print(f"Error authenticating to Redis cache: {e}")
            return ResponseHttp().getResponse(500, f"Error authenticating to cache: {str(e)}")
        
        print("Request data: ", request_data)
        
        price = 0
        id = getattr(requestInput, 'id', None)
        msc_field = getattr(requestInput, 'msc_field', "").strip()
        tender_name = getattr(requestInput, 'tender_name', "").strip()
        project_name = getattr(requestInput, 'project_name', "").strip()
        inviting_party = getattr(requestInput, 'inviting_party', "").strip()
        investor = getattr(requestInput, 'investor', "").strip()
        scope_of_work = getattr(requestInput, 'scope_of_work', "").strip()
        other_details = getattr(requestInput, 'other_details', "").strip()
        if id is None or not msc_field or not tender_name or not project_name:
            return ResponseHttp().getResponse(400, "Missing required fields in request input")

        result = {}
        main_category = msc_field
        token_count = 0

        if main_category not in MAIN_CATEGORIES:
            data = {
                "project_name": project_name,
                "tender_name": tender_name,
                "msc_field": main_category,
                "inviting_party": inviting_party,
                "investor": investor,
                "scope_of_work": scope_of_work,
                "other_details": other_details
            }
            try:
                res = gpt.categoryMainClassification(data)
                token_count += res.get('token_count', 0)
                main_category = res.get('main_category', main_category)
            except Exception as e:
                return ResponseHttp().getResponse(500, f"Error in categoryMainClassification: {str(e)}")

        sub_cate = SUB_CATEGORIES[main_category]
        context = "\n".join([f"- {item}" for item in sub_cate])

        data = {
            "project_name": project_name,
            "tender_name": tender_name,
            "msc_field": MAIN_CATE_ALIAS.get(main_category, main_category),
            "inviting_party": inviting_party,
            "investor": investor,
            "scope_of_work": scope_of_work
        }

        try:
            res = gpt.categorySubClassification(data, context)
            token_count += res.get('token_count', 0)
            sub_category = res['sub_category']
        except Exception as e:
            return ResponseHttp().getResponse(500, f"Error in categorySubClassification: {str(e)}")

        try:
            corpus = getVsicData(main_category, sub_category)
            context = "\n".join([f"{idx+1}. {item}" for idx, item in enumerate(corpus)])
        except Exception as e:
            return ResponseHttp().getResponse(500, f"Error in getVsicData: {str(e)}")

        data = {
            "project_name": project_name,
            "tender_name": tender_name,
            "main_category": MAIN_CATE_ALIAS.get(main_category, main_category),
            "sub_category": sub_category,
            "inviting_party": inviting_party
        }

        try:
            vsic_class = gpt.VsicClassification(data, context)
            token_count += vsic_class.get('token_count', 0)
            price += 0.15 * token_count / 1000000
            price = "{:.10f}".format(price)
            result = {
                "id": id,
                "main_category": MAIN_CATE_ALIAS.get(main_category, main_category),
                "sub_category": sub_category,
                "vsic_classification": vsic_class.get('vsic_categories', []),
                "token_count": token_count,
                "price": price,
            }
        except Exception as e:
            return ResponseHttp().getResponse(500, f"Error in VsicClassification: {str(e)}")
        
        # Lưu kết quả vào cache với TTL là 10 phút (600 giây)
        try:
            cache.setex(cache_key, 600, json.dumps(result))
        except redis.ConnectionError as e:
            print(f"Error saving to Redis cache: {e}")
            return ResponseHttp().getResponse(500, f"Error saving to cache: {str(e)}")
        except redis.AuthenticationError as e:
            print(f"Error authenticating to Redis cache: {e}")
            return ResponseHttp().getResponse(500, f"Error authenticating to cache: {str(e)}")
        
        return ResponseHttp().getResponse(200, result)

    except AttributeError as e:
        return ResponseHttp().getResponse(400, f"Missing or invalid attribute in request: {str(e)}")
    except Exception as e:
        return ResponseHttp().getResponse(500, f"Classification error: {str(e)}")