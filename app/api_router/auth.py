from fastapi import APIRouter, HTTPException
from app.core.hash import verify_password
from app.core.jwt import create_access_token

router = APIRouter()

# mock user (replace with DB)
fake_user = {
    "user_id": "user123",
    "password": "$2b$12$KIXQ..."  # hashed password
}

@router.post("/login")
def login(username: str, password: str):
    if username != fake_user["user_id"] or not verify_password(password, fake_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": username})

    return {"access_token": token, "token_type": "bearer"}