# DjangoCarsComments
Реализация REST API для управления отзывами на автомобили. Используемые технологии: Django и DjangoRestFramework.

# How to run

### Set your database settings
1. Copy default_database_config.py to database_config.py
2. Replace db_name and db_user to your data
```
DATABASE_NAME = 'db_name'
DATABASE_USER = 'db_user'
DATABASE_PASSWORD = 'password'
DATABASE_HOST = 'localhost'
DATABASE_PORT = '5432'
```
3. Create database tables
```
python manage.py migrate
```

### Install requirements
1. Python 3.11+
2. Install pip requirements
```
pip install -r requirements.txt
```

### Run server
```
python manage.py runserver
```

# Authentication
This service use TokenAuthentication.

### How to get token
Request
```
curl -X POST http://127.0.0.1:8000/api/token-auth/
   -H "Content-Type: application/json"
   -d '{"username": "your_username", "password": "your_password"}'  
```

Response
```
{"token": "a01119da7e5055bed26eebfff501757d3c0000d0e"}
```

### How to setup Auth Headers
```
Authorization: Token {your_auth_token}
content-type: application/json
```
Example
```
Authorization: Token a01119da7e5055bed26eebfff501757d3c0000d0e
content-type: application/json
```


### Api Endpoints
 - /api/counties/ GET
 - /api/counties/ POST - auth required
 - /api/counties/<int:country_id>/ PUT - auth required
 - /api/counties/<int:country_id>/ DELETE - auth required
   
 - /api/brands/ GET
 - /api/brands/ POST - auth required
 - /api/brands/<int:brand_id>/ PUT - auth required
 - /api/brands/<int:brand_id>/ DELETE - auth required

 - /api/cars/ GET
 - /api/cars/ POST - auth required
 - /api/cars/<int:car_id>/ PUT - auth required
 - /api/cars/<int:car_id>/ DELETE - auth required

 - /api/comments/ GET
 - /api/comments/ POST
 - /api/comments/<int:comment_id>/ PUT - auth required
 - /api/comments/<int:comment_id>/ DELETE - auth required

# Comments API examples
1. /api/comments/ GET
   
Response
```
   [
  {
    "id": 1,
    "email": "test@test.com",
    "car": {
      "id": 1,
      "name": "Supra",
      "release_year": 1978,
      "release_end_year": 2002,
      "brand": 1
    },
    "text": "Awesome!",
    "created_at": "2023-10-19T13:26:52.352611Z",
    "car_id": 1
  },
  {
    "id": 2,
    "email": "testuser@example.com",
    "car": {
      "id": 1,
      "name": "Supra",
      "release_year": 1978,
      "release_end_year": 2002,
      "brand": 1
    },
    "text": "good",
    "created_at": "2023-10-19T13:27:44.750981Z",
    "car_id": 1
  }
]
```

2. /api/comments/ POST

Request body
```
{
  "email": "new_user@example.com",
  "text": "how i can buy it?",
  "car_id": 1
}
```

Response
```
{
  "id": 3,
  "email": "new_user@example.com",
  "car": {
    "id": 1,
    "name": "Supra",
    "release_year": 1978,
    "release_end_year": 2002,
    "brand": 1
  },
  "text": "how i can buy it?",
  "created_at": "2023-10-19T13:30:37.660923Z",
  "car_id": 1
}
```

3. /api/comments/<int:comment_id>/ PUT

Request body
```
{
  "email": "new_user@example.com",
  "text": "how much does it cost?",
  "car_id": 1
}
```

Response
```
{
  "id": 3,
  "email": "new_user@example.com",
  "car": {
    "id": 1,
    "name": "Supra",
    "release_year": 1978,
    "release_end_year": 2002,
    "brand": 1
  },
  "text": "how much does it cost?",
  "created_at": "2023-10-19T13:30:37.660923Z",
  "car_id": 1
}
```

4. /api/comments/<int:comment_id>/ DELETE
   
   The response contains no body
