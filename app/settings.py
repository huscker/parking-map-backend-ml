import os

# S3
REGION_NAME = ''
S3_ENDPOINT_URL = ''
S3_AWS_ACCESS_KEY_ID = ''
S3_AWS_SECRET_ACCESS_KEY = ''
BUCKET_NAME = ''

# DB
DB_NAME = os.getenv('DB_NAME','parking-map')
DB_USERNAME = os.getenv('DB_USERNAME','postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD','postgres')
DB_PORT = os.getenv('DB_PORT','5432')
DB_HOST = os.getenv('DB_HOST','localhost')

DB_CONNECTION_STRING = f'postgres://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
REDIS_CONNECTION_STRING = ''