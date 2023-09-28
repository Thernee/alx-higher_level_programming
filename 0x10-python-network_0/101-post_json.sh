#!/bin/bash
# Takes in a URL and sends a JSON POST request with email and subject
curl -sX POST --json @"$2" "$1"
