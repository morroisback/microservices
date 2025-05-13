#!/bin/sh
uvicorn app.main:app --reload --host ${API_HOST} --port ${API_PORT}
