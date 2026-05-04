#!/bin/bash
while true; do
  if ! pgrep -f "siv_agent.py" > /dev/null; then
    echo "[WATCHDOG] Engine stopped. Restarting..."
    nohup python siv_agent.py &
  fi
  sleep 10
done

