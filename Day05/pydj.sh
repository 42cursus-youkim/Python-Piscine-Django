#!/bin/sh

location="$(pwd)/.venv"

case $1 in
k | kill)
    echo "kill port 8000"
    lsof -t -i tcp:8000 | xargs kill -9
    ;;
b | boot | run | runserv | runserver)
    # echo "remove exsisting migrations"
    # source final.sh

    echo "running django server"
    lsof -t -i tcp:8000 | xargs kill -9

    source $location/bin/activate

    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ;;
m | mig | migrate)
    python manage.py migrate
    ;;
mm | mmig | makemigrate | makemigration | makemigrations)
    python manage.py makemigrations
    ;;
init | install)
    # install prosygresql
    brew install PostgreSQL
    initdb djangotraining

    # Install python virtual environment
    python3 -m venv $location

    # Run installed virtual environment
    source $location/bin/activate

    pip install --upgrade pip
    pip install -r requirements.txt

    python -m django --version

    pagename="d05"
    django-admin startproject $pagename
    cd $pagename
    for i in {0..10}; do
        python3 manage.py startapp ex0$i
    done
    mv ex010 ex10

    python3 manage.py migrate
    ;;
*)
    echo "input ->$1 not found in available parameters"
    ;;
esac
