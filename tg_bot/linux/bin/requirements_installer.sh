#!/bin/bash
#Scripted by @jesvi
#Requirements_make tools also available

title="Requirements Installer-"
echo -e '\033]2;'$title'\007'

echo "Requirements Installer-"


Yellow='\033[1;33m'
NC='\033[0m' # No Color

echo ""
echo -e "${Yellow}(Installing dependencies listed on requirements.txt)${NC}"
echo ""
echo ""

cd ../
cd ../
cd ../

python3 -m pip install wheel
python3 -m pip install -r ./requirements.txt

echo -e -n "\nQuiting"
sleep 0.7
echo -n "."
sleep 0.7
echo -n "."
sleep 0.7 
echo -n "."

#read input
sleep 5