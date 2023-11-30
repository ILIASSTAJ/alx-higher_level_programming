#!/bin/bash
# A bash script that shows all HTTP methods on the server
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
