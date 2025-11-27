import os
from datetime import timedelta

class Config:
    SECRET_KEY = 'minha-chave-secreta'
    JWT_SECRET_KEY = 'minha-jwt-secreta'
    JWT_ACCESS_TOKEN_EXPIRES = 172800  # 2 dias em segundos
    DB_PATH = 'database/db.json'