#!/bin/bash

# Install python virtual environment
location="$(pwd)/django_venv"

python3 -m venv $location

# Run installed virtual environment
source $location/bin/activate

pip install --upgrade pip
pip install -r requirement.txt

python -m django --version

django-admin startproject scarfpage
cd scarfpage
python3 manage.py startapp helloworld
