#!/usr/bin/env bash

# TODO: debug server not loading on host

echo "Container's IP address: $(awk 'END{print $1}' /etc/hosts)"

# start jupyter lab
# jupyter lab --ip=0.0.0.0 --port=${PORT:-8888} --no-browser --ServerApp.token=${JUPYTER_TOKEN:-} --ServerApp.password=''
jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root
