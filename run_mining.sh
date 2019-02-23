#!/bin/bash
set -e
python src/main/python/br/com/jonathan/startup.py mining
read -t5 -n1 -r -p 'Press Enter to exit...' key
