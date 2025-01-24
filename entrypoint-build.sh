#!/usr/bin/env bash

APP_NAME="$1"

echo "Building executable: $APP_NAME"

# Ensure the output directory exists and has correct permissions
mkdir -p dist
chmod 777 dist

# Run PyInstaller
pyinstaller --onefile --name "$APP_NAME" -y src/pycli/cli.py

# Ensure the resulting files are writable by all (optional for host compatibility)
chmod -R 777 dist
