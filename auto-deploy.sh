#!/bin/bash

pid=$(ps aux | grep main.py | head -n 1 | cut -f7 -d" ")

kill $pid

git pull

echo "booting Bot"
python3 main.py

exit 0