#!/bin/bash

# Project root directory. IMPORTANT: Change this to your actual project path.
project_route="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"

# Set PYTHONPATH to include the project root
export PYTHONPATH="$PYTHONPATH:$project_route"

clear

echo "Starting GPIO Meal Manager..."
python3 $project_route/gpio-meal-manager.py &

echo "Starting Main Application..."
python3 $project_route/web/main.py