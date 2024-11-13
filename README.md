# Classification Service

This project is a classification service that uses OpenAI's GPT-4 model to classify tender packages into main and sub-categories based on provided information. The service integrates with Redis for caching, improving performance by storing previous responses.

## Technologies Used

- **Python**: Main programming language.
- **FastAPI**: Web framework for building APIs with Python 3.6+.
- **OpenAI API**: Utilizes GPT-4 model for classification tasks.
- **Redis**: In-memory data structure store, used for caching.
- **Docker**: Containerizes the application for easier deployment.
- **dotenv**: Manages environment variables from a `.env` file.
- **tiktoken**: Library for text encoding/decoding.
- **Gunicorn**: WSGI HTTP Server used to serve the FastAPI application.

## API Endpoint

### Classify Request

- **URL**: `http://localhost:8000/api/v1/classify`
- **Method**: `POST`
- **Content-Type**: `application/json`

#### Request Body

The request body should be a JSON object with the following fields:

| Field           | Type   | Description                                      |
|-----------------|--------|--------------------------------------------------|
| `id`            | string | Unique identifier for the request.               |
| `msc_field`     | string | MSC field of the tender.                         |
| `tender_name`   | string | Name of the tender.                              |
| `project_name`  | string | Name of the project.                             |
| `inviting_party`| string | Inviting party of the tender.                    |
| `investor`      | string | Investor in the project.                         |
| `scope_of_work` | string | Scope of work for the tender.                    |
| `other_details` | string | Any other relevant details about the tender.     |

#### Example Request

```json
{
  "id": "12345",
  "msc_field": "Construction",
  "tender_name": "Building a new bridge",
  "project_name": "Bridge Construction Project",
  "inviting_party": "City Council",
  "investor": "Government",
  "scope_of_work": "Construction of a new bridge over the river",
  "other_details": "The bridge should be completed within 2 years"
}
```

```cmd
OPENAI_API_KEY=your_openai_api_key
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_PASSWORD=your_redis_password
```


```
docker-compose up --build
```

Access the API: The API will be available at http://localhost:8000/api/v1/classify/request.