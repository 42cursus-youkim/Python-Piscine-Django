#!/bin/sh

location="$(pwd)/.venv"
venv="$location/bin/activate"

function srcvenv() {
    if test -f "$venv"; then
        source $venv
    fi
}

srcvenv

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
ma | miga | migrateall)
    python manage.py makemigrations
    python manage.py migrate
    ;;
init | install)
    # install postgresql
    #brew install PostgreSQL
    #initdb djangotraining
    echo ".venv" >>.gitignore
    echo "db.sqlite3" >>.gitignore
    # Install python virtual environment
    python3 -m venv $location

    # Run installed virtual environment
    srcvenv

    pip install --upgrade pip
    pip install django
    pip install black

    #pip install -r requirements.txt
    pip freeze >>requitements.txt

    python -m django --version

    django-admin startproject $2 .
    python3 manage.py startapp $3
    python3 manage.py migrate

    git add .
    git commit -m "inital commit"
    git push $gitflag origin master
    # /Users/youkim/YouShell/Boot/Core/1-shortcuts.sh
    ;;
"")
    echo "empty input parameters: operation not specified"
    ;;
*)
    echo "input -> $1 not found in available parameters"
    ;;
esac
