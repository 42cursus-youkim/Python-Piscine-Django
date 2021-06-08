#!/bin/sh

for num in $(seq -w 01 10); do
    name="ex$num"
    rm $name/migrations/0001_initial.py
    psql -u djangouser DROP TABLE $name"_movies"
    python3 ./manage.py migrate --fake $name zero
done
