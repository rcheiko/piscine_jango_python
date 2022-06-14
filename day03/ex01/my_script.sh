#!/bin/sh

pip3 --version
pip3 install path.py -t ./local_lib --upgrade > installed.log
python3 my_program.py

# pip3 install -r requirement.txt