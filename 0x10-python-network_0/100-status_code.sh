#!/bin/bash
# Takes in a URL and sends a POST request with email and subject
(curl -so /dev/null --write-out "%{http_code}" "$1")
