import os

db_URI = os.getenv('DATABASE_URL', 'postgres://localhost:5432/sample')
secret = os.getenv('SECRET', 'This the sample temp.')