from fastapi import FastAPI
from routers import *
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(classifyRouter, prefix="/api/v1")
app.include_router(healthRouter, prefix="")

Instrumentator().instrument(app).expose(app)

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)