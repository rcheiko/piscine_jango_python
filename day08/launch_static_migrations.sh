#!/bin/zsh

python3 ./day08/manage.py makemigrations ex
python3 ./day08/manage.py migrate
python3 ./day08/manage.py collectstatic