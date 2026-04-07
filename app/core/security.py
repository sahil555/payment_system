from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = "super-secret-key" 
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60