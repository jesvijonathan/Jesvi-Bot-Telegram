#!/bin/bash

title="BOT Debugger"
echo -e '\033]2;'$title'\007'


echo ""
echo "Logging MYSQL Bot db (logs/log_bot_runtime.log)"
echo "Press Ctrl + C to stop logging..."
echo ""

sudo tail -f $(dirname `pwd`)/logs/log_bot_runtime.log

sleep 5