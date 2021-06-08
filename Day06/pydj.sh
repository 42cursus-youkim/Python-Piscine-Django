#!/bin/sh

location="$(pwd)/.venv"
source "$location/bin/activate"

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

    # python manage.py makemigrations
    # python manage.py migrate
    python manage.py runserver
    ;;
m | mig | migrate)
    python manage.py migrate
    ;;
mm | mmig | makemigrate | makemigration | makemigrations)
    python manage.py makemigrations
    ;;
init | install)
    # install postgresql
    #brew install PostgreSQL
    #initdb djangotraining

    # Install python virtual environment
    python3 -m venv $location

    # Run installed virtual environment
    source $location/bin/activate

    pip install --upgrade pip
    pip install django
    pip install black

    #pip install -r requirements.txt
    pip freeze >>requitements.txt

    python -m django --version

    django-admin startproject d06 .
    #cd $pagename
    #for i in $(seq -w 1 10); do
    #    python3 manage.py startapp ex0$i
    #done
    python3 manage.py startapp ex

    python3 manage.py migrate
    ;;
"")
    echo "empty input parameters: operation not specified"
    ;;
*)
    echo "input ->$1 not found in available parameters"
    ;;
esac
