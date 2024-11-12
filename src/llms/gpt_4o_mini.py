import json
import logging
import os
from typing import Dict, Any
from openai import OpenAI
from .prompts import Prompts
from dotenv import load_dotenv
import tiktoken

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

class GPT_4o_mini:
    def __init__(self, model_name: str = "gpt-4o-mini-2024-07-18"):
        self.client = OpenAI()
        self.model_name = model_name
        self.prompts = Prompts()
        self.encoder = tiktoken.encoding_for_model(self.model_name)

    def count_tokens(self, message: Dict[str, str]) -> int:
        """Count the number of tokens in a single message."""
        return len(self.encoder.encode(message["content"]))

    def _create_chat_completion(self, messages: list, function_def: dict) -> dict:
        """Helper method to create chat completion with common parameters"""
        try:
            total_tokens = sum(self.count_tokens(msg) for msg in messages)
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=messages,
                temperature=0,
                functions=[function_def],
                function_call={"name": function_def["name"]}
            )
            
            result = json.loads(response.choices[0].message.function_call.arguments)
            return result, total_tokens
            
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            return {"error": str(e)}, 0
        
    def categoryMainClassification(self, data: str) -> Dict[str, Any]:
        messages = [
            {
                "role": "system",
                "content": "Bạn là chuyên gia trong lĩnh vực Đấu Thầu, hiên tại tôi đang có những gói thầu cần được phân loại, tôi được yêu cầu phân loại gói thầu của mình thành các danh mục chính và danh mục con dựa vào các thông tin từ gói thầu nhằm tối ưu hóa cho hệ thống SEO, những thông tin của gói thầu được cung cấp như sau: Tên dự án, Tên gói thầu, Lĩnh vực MSC, hãy giúp tôi đưa ra kết quả phân loại danh mục chính và danh mục con phù hợp nhất"
            },
            {
                "role": "user",
                "content": self.prompts.categoryMainPrompt(data)
            }
        ]

        function_def = {
            "name": "classify_categories",
            "description": "Phân loại danh mục chính và danh mục con",
            "parameters": {
                "type": "object",
                "properties": {
                    "main_category": {"type": "string"},
                },
                "required": ["main_category", "sub_category"]
            }
        }

        result, total_tokens = self._create_chat_completion(messages, function_def)
        
        if "error" in result:
            return result
            
        return {
            "main_category": result.get("main_category"),
            "sub_category": result.get("sub_category"),
            "token_count": total_tokens
        }

    def categorySubClassification(self, data, context) -> Dict[str, Any]:
        messages = [
            {
                "role": "system",
                "content": "Bạn là chuyên gia trong lĩnh vực Đấu Thầu, hiên tại tôi đang có những gói thầu cần được phân loại, tôi được yêu cầu phân loại gói thầu của mình thành các danh mục chính và danh mục con dựa vào các thông tin từ gói thầu nhằm tối ưu hóa cho hệ thống SEO, những thông tin của gói thầu được cung cấp như sau: Tên dự án, Tên gói thầu, Lĩnh vực MSC, hãy giúp tôi đưa ra kết quả phân loại danh mục con phù hợp nhất"
            },
            {
                "role": "user",
                "content": self.prompts.categorySubPrompt(data, context)
            }
        ]

        function_def = {
            "name": "generate_feature_vector",
            "description": "Phân loại danh mục con từ gói Thầu cho trước",
            "parameters": {
                "type": "object",
                "properties": {
                    "sub_category": {"type": "string"}
                },
                "required": ["sub_category"]
            }
        }

        result, total_tokens = self._create_chat_completion(messages, function_def)
        
        if "error" in result:
            return result
            
        return {
            "sub_category": result.get("sub_category"),
            "token_count": total_tokens
        }

    def VsicClassification(self, data: str, context: str) -> Dict[str, Any]:
        messages = [
            {
                "role": "system",
                "content": "Bạn là chuyên gia trong lĩnh vực Đấu Thầu, hiên tại tôi đang có những gói thầu cần được phân loại, tôi được yêu cầu phân loại gói thầu của mình thành các danh mục chính và danh mục con dựa vào các thông tin từ gói thầu nhằm tối ưu hóa cho hệ thống SEO, những thông tin của gói thầu được cung cấp như sau: Tên dự án, Tên gói thầu, Lĩnh vực MSC, hãy giúp tôi đưa ra kết quả phân loại danh mục VSIC Vietnam standard industrial classification phù hợp nhất từ gói Thầu cho trước"
            },
            {
                "role": "user",
                "content": self.prompts.VsicPrompt(data, context)
            }
        ]

        function_def = {
            "name": "generate_feature_vector", 
            "description": "Phân loại danh mục VSIC phù hợp nhất từ gói Thầu cho trước",
            "parameters": {
                "type": "object",
                "properties": {
                    "vsic_categories": {"type": "string"},
                },
                "required": ["vsic_categories"]
            }
        }

        result, total_tokens = self._create_chat_completion(messages, function_def)
        
        if "error" in result:
            return result
            
        result["token_count"] = total_tokens
        return result
