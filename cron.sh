#!/bin/bash
source "/Users/nawarkhede/.virtualenvs/stack-notifier/bin/activate"
while [ true ]; do
     sleep 1
     python /Users/nawarkhede/projects/notifier/notifier/cron.py
  done
