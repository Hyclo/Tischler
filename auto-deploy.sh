#!/bin/bash

pid=$(ps aux | grep main.py | head -n 1 | cut -f7 -d" ")

echo "got PID: $pid"

echo "started killing bot: $pid"
kill $pid
echo "killed proccess: $pid"

echo "starting git pull"
git pull
echo "git pull done"

echo "booting Bot"

python3 main.py