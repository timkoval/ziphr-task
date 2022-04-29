# ziphr-task

## ZipHR task - ZipAirlines

Implemented using Django, DRF, Coveragepy, SQLite

# How to launch 

1. `pip install -r requirements.txt` in your virtual environment
2. `python manage.py runserver` (no need to create database since we use SQLite)
3. `coverage run --source . manage.py test` to perform tests
4. `coverage html` and then `firefox htmlcov/index.html` or similar to get coverage report
5. use any http request tool ex. `hoppscotch.io` to test API

# API routes and sample requests

`POST` new plane:
`localhost:8000/planes/`

Body:
```
{
  "id": 2341, 
  "tank_capacity": 0, // just to simplify serializer
  "consumption": 0 // just to simplify serializer
}
```

`GET` all planes:
`localhost:8000/planes/`

`POST` new passenger:
`localhost:8000/passengers/`

Body:
```
{
    "name": "Ivan",
    "surname": "Ivanov",
    "plane": 1
}
```

`GET` all passengers:
`localhost:8000/passengers/`
