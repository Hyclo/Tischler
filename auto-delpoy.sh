#!/bin/sh

pid=$(ps -ef | grep -E "/root\W{1,}\d{1,}.*\Wpython3\Wmain.py/gm" | grep -E "/\d{3,}/gm")

echo "$pid"