#!/bin/sh

# this script runs all unit tests

python -m unittest discover -s tbs/helper/tests -p "*_test.py"