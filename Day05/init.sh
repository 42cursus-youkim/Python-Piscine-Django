#!/bin/bash

VENV=".venv"

# setup venv
python3 -m venv $VENV
source $VENV/bin/activate

# pip version
pip --version

# pip install
#pip --freeze >>requirements.txt
pip install --force-reinstall -r requirements.txt
