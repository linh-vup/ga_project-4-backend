#!/bin/bash

echo "creating user_days/seeds.json"
python manage.py dumpdata user_days --output user_days/seeds.json --indent=2;

echo "creating foods/seeds.json"
python manage.py dumpdata foods --output foods/seeds.json --indent=2;

echo "creating colors/seeds.json"
python manage.py dumpdata colors --output colors/seeds.json --indent=2;

echo "creating jwt_auth/seeds.json"
python manage.py dumpdata jwt_auth --output jwt_auth/seeds.json --indent=2;