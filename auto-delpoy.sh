#!/bin/bash

# Check if process name argument was provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <process name>"
    exit 1
fi

# Find PID of the process
pid=$(pgrep "$1")

# Check if process exists
if [ -z "$pid" ]; then
    echo "Process not found: $1"
    exit 1
fi

# Kill the process
echo "Killing process $1 with PID $pid..."
kill "$pid"