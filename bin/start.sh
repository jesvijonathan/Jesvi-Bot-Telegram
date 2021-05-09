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
echo -e '\e[1A\e[KInternet |' ${Green}Connected${NC}

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

    else
        echo -e -n "\n\b" ${Red}"\e[1A\e[K\rInvalid Input.."${NC}
        sleep 0.5
        echo  ""
    fi
done
fi


sleep 10