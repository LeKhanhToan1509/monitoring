#!/bin/bash
export TZ="Asia/Ho_Chi_Minh"

HEALTH_URL="http://localhost:8000/healthcheck"
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" $HEALTH_URL)

if [ "$HTTP_CODE" -eq 200 ]; then
  echo "$(date "+%Y-%m-%d %H:%M:%S") - Alive" >> logs/healthCheck.log
  exit 0
else
  echo "$(date "+%Y-%m-%d %H:%M:%S") - Dead with status code $HTTP_CODE" >> logs/healthCheck.log
  exit 1
fi
