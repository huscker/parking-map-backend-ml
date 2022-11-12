include .env
export

PROJECT = app

prepare:
	poetry install

services:
	docker compose up -d postgresql keycloak

run:
	poetry run uvicorn ${PROJECT}.main:app  --host 0.0.0.0 --port=${UVICORN_PORT}

logs:
	docker compose logs

format:
	isort ${PROJECT}
	black ${PROJECT}

lint:
	pylint ${PROJECT}

postgres:
	docker compose up -d postgresql

keycloak:
	docker compose up -d keycloak

down:
	docker compose down

open_postgres:
	PGPASSWORD=${DB_PASSWORD} docker exec -it parking-map-backend-postgresql psql -U ${DB_USERNAME} -d ${DB_NAME}
