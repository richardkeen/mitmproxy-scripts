#!/bin/bash
echo "Proxy running on port 8080 of:"
ifconfig en0 | grep inet | grep -v inet6

mitmdump -s http_audit.py