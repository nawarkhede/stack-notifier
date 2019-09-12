#!/bin/bash
eval "$(pyenv init -)"
pyenv activate stack-notifier
while [ true ]; do
     sleep 1
     python /Users/nishantnawarkhede/projects/stack-notifier/notifier/cron.py
  done
