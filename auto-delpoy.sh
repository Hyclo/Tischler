#!/bin/bash

pid=$(ps aux | grep main.py | head -n 1 | cut -f7 -d" ")

echo "$pid"