#!/bin/bash

echo "dropping database django-albums"
dropdb django-etr

echo "creating database django-albums"
createdb django-etr

python manage.py makemigrations

python manage.py migrate

echo "inserting users/auth"
python manage.py loaddata jwt_auth/seeds.json

echo "inserting colors"
python manage.py loaddata colors/seeds.json

echo "inserting foods"
python manage.py loaddata foods/seeds.json

echo "inserting user days"
python manage.py loaddata user_days/seeds.json
