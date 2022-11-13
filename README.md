Сама модель вынесена в S3-хранилище
Также стоит вынести изображения
https://storage.yandexcloud.net/ar-education/model_weights.h5

# TODO:
* keycloak
* sentry-sdk
* миграции (aerich)
* Tortoise ORM
* Рефактор ML-кода
* Шаблоны для тестов

models - работа с БД
views - pydantic-модели
controllers - эндпоинты

# Требования к запуску
Для работы сервиса требуется наличие следующих утилит:
- `Make v^4.3`
- `poetry v^1.2.2`
- `python v^3.10`
- `docker v^20.10.21`
- ...
# Подготовка к запуску
1. Установка библиотек:
```shell
make prepare
```
2. Настройка параметров. Требуется создать файл `.env` в корневой директории проекта и настроить переменные окружения. Пример заполнения файла:
```shell
DB_NAME=parking-map
DB_USERNAME=postgres
DB_PASSWORD=postgres
DB_PORT=5432
DB_HOST=localhost

UVICORN_PORT=8080
REALM_NAME=temp
KEYCLOAK_URL=http://localhost:8888
KEYCLOAK_CLIENT_ID=name
KEYCLOAK_CLIENT_SECRET=gpGVn4EZecg1oqHMnE6VOEJqM9F0TWTy

KEYCLOAK_PORT=8888
KEYCLOAK_ADMIN_USER=admin
KEYCLOAK_ADMIN_PASSWORD=admin

REGION_NAME=region
S3_ENDPOINT_URL=url
S3_AWS_ACCESS_KEY_ID=access-id
S3_AWS_SECRET_ACCESS_KEY=secret-key
BUCKET_NAME=bucket-name
```
3. Запуск сервисов (postgresql, keycloak):
Для запуска необходимо наличие файла `.env`.
```shell
make services
```
4. Накатывание миграций:
```shell
...
```
5. Настроить realm в keycloak и получить `KEYCLOAK_CLIENT_ID` и `KEYCLOAK_CLIENT_SECRET`
6. Запустить сервис:
```shell
make run
```

# Пример построения предсказания

1. Выберите парковку.
2. Вручную разметьте её парковочные места  с помощью LabelImg, используя лейбл parking lot, и сохраните в формате .json (CreateML)
![img](example/step_1_label.png)


3. `python3 extra_scripts/show_predict.py example/Парковка_РИО_2022_09_07.json example/Парковка_РИО_2022_09_07.png`, чтобы получить занятость парковки на картинке.

```bash
[quakumei@boxpc park-backend-ml]$ python3 extra_scripts/show_predict.py example/Парковка_РИО_2022_09_07.json example/Парковка_РИО_2022_09_07.png
[False, False, False, False, False, False, False, False, True, True, True, True, False, True, False, True, False, False, False, False, True, True, False, False]
Occupancy rate of parking lot on example/Парковка_РИО_2022_09_07.png is 0.3333333333333333 (8/24)
```
