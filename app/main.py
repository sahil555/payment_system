from fastapi import FastAPI
from app.api_router.routes import router

app = FastAPI(title="Payment System")

app.include_router(router)