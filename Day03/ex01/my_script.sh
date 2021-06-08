#!/bin/bash

nowdir=$(pwd)

python3 -m venv "$nowdir/local_lib"

# virtualenv "$nowdir/local_lib"
source $nowdir/local_lib/bin/activate
#pip install --upgrade pip
pip install --upgrade pip
pip --version
pip install --log log.log --upgrade --force-reinstall git+https://github.com/jaraco/path.git

python my_program.py
