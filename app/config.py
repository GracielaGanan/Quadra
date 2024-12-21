
# app/config.py

class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:225868788898@db.tqkjslqvkulzrmspjqsd.supabase.co:5432/postgres"  # Cambia la URI de tu base de datos
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_ALGORITHM = "HS256"
    SECRET_KEY = "secret_key_example"
    PROPAGATE_EXCEPTIONS = True

