#!/bin/bash
curl --fail http://localhost:${API_PORT}/api/v1/movies/ || exit 1
