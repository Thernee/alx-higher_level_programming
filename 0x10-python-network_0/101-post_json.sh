#!/bin/bash
# Takes in a URL and sends a JSON POST request with email and subject
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
