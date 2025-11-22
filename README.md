# Little Lemon Backend

## API Endpoints
- `/restaurant/menu-items/` (GET, POST)
- `/restaurant/menu-items/<id>/` (GET, PUT, DELETE)
- `/restaurant/booking/tables/` (GET, POST - Authenticated)
- `/auth/users/` (User Registration)
- `/auth/token/login/` (Token Generation)

## Installation
1. `pipenv install`
2. `pipenv run python manage.py migrate`
3. `pipenv run python manage.py runserver`
