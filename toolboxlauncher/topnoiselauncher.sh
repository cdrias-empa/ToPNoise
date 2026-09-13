#!/bin/bash

SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
PYTHONPATH=python3

cd $SCRIPTPATH

$PYTHONPATH railtracktoolboxLauncher.py
