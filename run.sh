#!/bin/bash

# Project root directory. IMPORTANT: Change this to your actual project path.
project_route="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
version="Meal-Time 1.0"

while getopts ":v" opt; do
  case "$opt" in
    v) echo $version; exit ;;
  esac
done

# Set PYTHONPATH to include the project root
export PYTHONPATH="$PYTHONPATH:$project_route"

clear

echo "Starting Pigpio"
sudo pigpiod

echo "Starting ngrok"
ngrok_url="tisa-potamic-tidily.ngrok-free.dev"
ngrok http 5000 --url=$ngrok_url --pooling-enabled > /dev/null 2>&1 &
echo "Visit ngrok on: https://$ngrok_url"

echo "Starting GPIO Meal Manager..."
python3 $project_route/gpio-meal-manager.py &

echo "Starting Main Application..."
python3 $project_route/web/main.py

echo ""
echo "Killing?"
sudo pkill ngrok
sudo pkill python3
