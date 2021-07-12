#!/bin/bash

title="BOT Debugger"
echo -e '\033]2;'$title'\007'

s1(){
bash "${PWD}/bin/dir_test.sh" && cd ./bin
}
s2(){
bash "${PWD}/dir_test.sh"
}
s1 || s2
cur=${PWD}
reset

echo ""
echo "Logging MYSQL Bot db (logs/log_bot_runtime.log)"
echo "Press Ctrl + C to stop logging..."
echo ""

cd ../
cd ../

sudo tail -f ${PWD}/logs/log_bot_runtime.log

cd "${cur}"
sleep 5