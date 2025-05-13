#!/bin/bash

set -e

if [ "$DEBUG" == "True" ]; then
    echo "Starting in DEBUG mode..."
    python -Xfrozen_modules=off -m debugpy --listen "$API_HOST":"$DEBUG_PORT" -m uvicorn app.main:app --host "$API_HOST" --port "$API_PORT" --reload
else
    echo "Starting in NORMAL mode..."
    uvicorn app.main:app --host "$API_HOST" --port "$API_PORT" --reload 
fi
