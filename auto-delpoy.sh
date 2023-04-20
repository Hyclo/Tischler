#!/bin/bash

pid=$(ps aux | grep main.py | head -n 1 | cut -f7 -d" ")

echo "got PID: $pid"

kill $pid
echo "killed proccess: $pid"

echo "booting Bot
"
nohup python3 main.py