#!/bin/sh

python3 -m virtualenv django_venv && cd django_venv && source bin/activate && pip3 install -r ../requirement.txt