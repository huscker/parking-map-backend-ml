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

# Keycloak
KEYCLOAK_PORT = os.getenv("KEYCLOAK_PORT", 8888)
REALM_NAME = os.getenv("REALM_NAME", "parking-map")
KEYCLOAK_URL = os.getenv("KEYCLOAK_URL", f"https//localhost:{KEYCLOAK_PORT}")
KEYCLOAK_CLIENT_ID = os.getenv("KEYCLOAK_CLIENT_ID", "")
KEYCLOAK_CLIENT_SECRET = os.getenv("KEYCLOAK_CLIENT_SECRET", "")
KEYCLOAK_ADMIN_USER = os.getenv("KEYCLOAK_ADMIN_USER", "admin")
KEYCLOAK_ADMIN_PASSWORD = os.getenv("KEYCLOAK_ADMIN_PASSWORD", "admin")

DB_CONNECTION_STRING = f'postgres://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
REDIS_CONNECTION_STRING = ''