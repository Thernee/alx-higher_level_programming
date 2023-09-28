#!/bin/bash
# Takes in a URL and sends a POST request with email and subject
curl -sX POST -H "email: test@gmail.com" -H "subject: I will always be here for PLD" "$1"
