#!/bin/zsh

python3 ./manage.py makemigrations ex
python3 ./manage.py migrate
python3 ./manage.py collectstatic