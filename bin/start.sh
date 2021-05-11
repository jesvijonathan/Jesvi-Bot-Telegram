#!/bin/bash

title="Jesvi Bot Status"
echo -e '\033]2;'$title'\007'

# Color Code
Red='\033[0;31m'
Green='\033[0;32m'
Yellow='\033[1;33m'
NC='\033[0m' # No Color


echo Checking internet connection..


if detection_out=$(wget -q http://detectportal.firefox.com/success.txt --timeout=10 -O - 2> $PWD/null);
then
echo -e -n '\e[1A\e[KInternet |' ${Green}Connected${NC}
#iw dev | grep ssid | awk '{print $2}'
else
echo -e '\e[1A\e[KInternet |' ${Red}No Internet${NC} '\n'

while true; do
    
    echo -n -e ${Yellow}"\e[1A\e[KPress 'q' to quit or 'r' to restart the script.."${NC}
    read -n1 input
    
    if [[ $input = "q" ]] || [[ $input = "Q" ]]
        then exit 0
    
    elif [[ $input = "r" ]] || [[ $input = "R" ]] 
        then reset
        exec "$PWD/start.sh"
# python3 ./$PWD/main.py
    else
        echo -e -n "\n\b" ${Red}"\e[1A\e[K\rInvalid Input.."${NC}
        sleep 0.5
        echo  ""
    fi
done
fi

echo -e -n "\nChecking memory usage.."
sleep 0.5
echo -e -n "\rMemory   | ${Green}"
free -m | awk 'NR==2{printf "%s/%sMB (%.2f%%)\n", $3,$2,$3*100/$2 }'

echo -e -n "${NC}Service start time.."
sleep 0.5
echo -e "\rTime     | ${Green}"$(date +'%r')

echo -e -n "\n--Live Status--\n\n" ${NC}

sudo service mysql start
python3 $(dirname `pwd`)/scripts/main.py


sleep 5