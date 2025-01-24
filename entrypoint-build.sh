#!/usr/bin/env bash

APP_NAME="$1"

echo "Building executable: $APP_NAME"

pyinstaller --onefile --name "$APP_NAME" -y src/pycli/cli.py
