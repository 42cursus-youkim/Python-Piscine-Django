#!/bin/bash

location="$(pwd)/django_venv"

python3 -m venv $location

# virtualenv "$location"
python3 -m pip install -r requirement.txt

source $location/bin/activate
