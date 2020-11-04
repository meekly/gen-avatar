#!/bin/bash
set -e

if [ "$ENV" = 'DEV' ]; then
  echo "Running Development Server"

  exec uwsgi -b 32768 \
       --http 0.0.0.0:9090 \
       --stats 0.0.0.0:9191 \
       --wsgi-file /app/identidock.py \
       --callable app
else
  echo "Running Production Server"

  exec uwsgi -b 32768 \
       --http 0.0.0.0:9090 \
       --wsgi-file /app/identidock.py \
       --callable app
fi
