#!/bin/bash
# This script pulls latest code and restarts the Flask app

# Path to your running app
APP_DIR="/home/munyaradzi/Downloads/flask_webhook"

echo "==> Pulling latest code..."
cd $APP_DIR || exit
git reset --hard origin/main   # optional: force reset to remote
git pull origin main

echo "==> Restarting Flask app..."
# Kill previous Flask process (basic approach)
pkill -f "flask run"

# Activate virtual environment if you have one
if [ -f "$APP_DIR/venv/bin/activate" ]; then
    source "$APP_DIR/venv/bin/activate"
fi

# Start Flask app in background
# Adjust host/port if needed
nohup flask run --host=0.0.0.0 --port=5000 > flask.log 2>&1 &

echo "==> Update complete!"
