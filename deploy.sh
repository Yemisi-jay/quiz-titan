#!/bin/bash

#run migrations
python manage.py migrate
python manage.py collectstatic --no-input