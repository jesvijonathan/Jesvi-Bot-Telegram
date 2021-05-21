#!/bin/bash
#Scripted by @jesvi
#Requirements_make tools also available

title="Requirements Installer"
echo -e '\033]2;'$title'\007'

echo Requirements Installer

echo
echo
echo Installing dependencies listed on requirements.txt
echo
echo

python3 -m pip install wheel
python3 -m pip install -r ../requirements.txt

sleep 5