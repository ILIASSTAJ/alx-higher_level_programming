#!/bin/bash
# Bash Script to GET request then show response status code.
curl -s -o /dev/null -w "%{http_code}" "$1"
