#!/bin/bash

DIR="$(dirname "$(readlink -f "$0")")"

if [[ $(python -V) ~= Python 3.* ]]; then
    echo "Checking dependencies are installed.."
    pip3 -q install -r $DIR/requirements.txt

    echo "Starting application.."
    python $DIR/src/pyverify.py
fi

echo "You are using old version of Python [3.x.x required]:"
echo $(python -V)