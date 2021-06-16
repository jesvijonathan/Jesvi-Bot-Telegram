#!/bin/bash

title="Jesvi Bot Status"
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

co=$1

sle(){
    if [[ ${co} = "1" ]]
    then
    sleep $1
    fi
}

col(){
    if [[ $co = "1" ]]
    then
    echo $1
    fi
        
}

Red=$(col '\033[0;31m')
Green=$(col '\033[0;32m')
Yellow=$(col '\033[1;33m')
lYellow=$(col '\033[0;33m')
NC=$(col '\033[0m')
kYellow=$(col '\033[0;37m')

#echo "The current working directory: $PWD"
: '
Black        0;30     Dark Gray     1;30
Red          0;31     Light Red     1;31
Green        0;32     Light Green   1;32
Brown/Orange 0;33     Yellow        1;33
Blue         0;34     Light Blue    1;34
Purple       0;35     Light Purple  1;35
Cyan         0;36     Light Cyan    1;36
Light Gray   0;37     White         1;37
'

#reset

echo "        _______   _______         "
sle 0
echo "   __  ___  __ \ / __  __ _____   "
sle 0
echo "  |_ \| __/' _| | |  \/__|_   _|  "
sle 0
echo "   _\ | _|\`._\`\` | | ~| \/ || | "
sle 0
echo "  /___|___|___/ | |__/\__/ |_|    "
sle 0
echo "        _______/ \_______         "
sle 0
echo ""
sle 0
echo " -------------------------------  "


#echo -e " ${NC}1-${Yellow}Stop    ${NC}2-${Yellow}Log Bot    ${NC}3-${Yellow}LogSQL\n ${NC}4-${Yellow}Test    ${NC}5-${Yellow}Restart    ${NC}6-${Yellow}Folder${NC}"
echo -e " ${NC}1-Stop    2-Log Bot    3-LogSQL\n 4-Test    5-Restart    6-Folder"

echo " -------------------------------  "

#pyon3: can't open file '/root/Documents/GitHub/Jesvi-Bot-Telegram/scripts/main.py': [Errno 2] No such file or directory

echo -e "\n"Checking internet connection..


if detection_out=$(wget -q http://detectportal.firefox.com/success.txt --timeout=10 -O - 2> /dev/null) 2> /dev/null;
then
echo -e -n '\e[1A\e[K' "     " 'Internet :' ${Green}Connected${NC}
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
        exec "$PWD/run.sh" $co
# python3 ./$PWD/main.py
    else
        echo -e -n "\n\b" ${Red}"\e[1A\e[K\rInvalid Input.."${NC}
        sleep 0.4
        echo  ""
    fi
done
fi

echo -e -n "\nChecking memory usage.."
sle 0.5
echo -e -n "\r" "     " "Memory   : ${Green}"
free -m | awk 'NR==2{printf "%s/%sMB\n", $3,$2 }'
#free -m | awk 'NR==2{printf "%s/%sMB (%.2f%%)\n", $3,$2,$3*100/$2 }'

echo -e -n "${NC}Service start time.."
sle 0.5
echo -e "\r" "     " "Time     : ${Green}"$(date +'%r')

#echo -e -n "\n--Live Status--\n\n" ${NC}

echo -e -n "\n${NC}---------- ${Yellow}Live Status ${NC}---------\n\n" ${NC}

#echo -e -n "starting mysql.."
sle 0.5
echo -e -n "\r"

sudo service mysql start 1> /dev/null



a1(){
#echo ${PWD}
#echo "running 1"
cd ../
cd ../
#append mode
#python3 ${PWD}/scripts/main.py 2>> ${PWD}/logs/log_bot_runtime.log &
python3 ${PWD}/scripts/main.py 2> ${PWD}/logs/log_bot_runtime.log &
}

a1
cd "${cur}"
echo ""

del(){
    echo -e -n "\n\b""\e[1A\e[K\r"
    echo  ""
}
rst(){
    reset
    exec "${cur}/run.sh" ${co}
    #bash "${PWD}/run.sh" 
    #exit 0
}

while true; do

echo -n -e ${Yellow}"\e[1A\e[K"${NC}
read -n1 i

if [[ $i = "1" ]]
        then 
        echo -e -n "\bStopping"
        sleep 0.2
        echo -n "."
        pkill -f main.py
        sleep 0.2
        echo -n "."
        sleep 1
        exit 0
elif [[ $i = "6" ]]
        then
        echo -e -n "\bOpening resource folder"
        xdg-open . >/dev/null 2>&1 &
        sle 0.2
        echo -n "."
        sle 0.2
        echo -n "."
        sle 0.3
elif [[ $i = "2" ]]
        then
        echo -e -n "\bOpening Bot Logger terminal"
        sle 0.2
        echo -n "."
        sle 0.2
        echo -n "."
        x-terminal-emulator -e ./bot_logger.sh 2> /dev/null
        sleep 0.3

elif [[ $i = "3" ]]
        then
        echo -e -n "\bOpening MYSQL Logger terminal"
        sle 0.2
        echo -n "."
        sle 0.2
        echo -n "."
        x-terminal-emulator -e ./mysql_logger.sh 2> /dev/null
        sleep 0.3
elif [[ $i = "d" ]]
        then
        echo -N "'ON' or 'OFF' : "
        read ii
        python3 ${cur}/general_log_switch.py ${ii}
elif [[ $i = "5" ]]
        then
        echo -e -n "\bRestarting Bot"
        sle 0.2
        echo -n "."
        pkill -f main.py
        sleep 0.2
        echo -n "."
        sleep 1
        echo -n "."
        pkill -f main.py
        sleep 0.4
        rst
else
        sle 0.2
        echo -e -n "\n\b" ${Red}"\e[1A\e[K\rInvalid Input.."${NC}
        sleep 0.4
fi
  echo "" 
done

#pkill -f b.sh

####have to add, live function for logging and stopping, etc

sleep 10
