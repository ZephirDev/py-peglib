#!/usr/bin/env bash

set -e

BASEDIR=$(dirname "$0")
PYTHON_SCRIPT="$BASEDIR/python.sh"

function run() {
    SCRIPT="$BASEDIR/$1"
    echo "-- Execute $SCRIPT"
    $PYTHON_SCRIPT $SCRIPT
}

run 00_loading.py
run 01_simple.py
