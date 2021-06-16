#!/bin/bash


title="Jesvi Bot"
echo -e '\033]2;'$title'\007'

temp=${PWD}

s1(){
bash "${PWD}/bin/dir_test.sh" && cd ./bin
}

s2(){
bash "${PWD}/dir_test.sh"
}

s1 || s2 

cur=${PWD}

reset

da=(
[1]="bot_logging" 
[2]="sql_logging" 
[3]="minimise_log" 
[4]="fresh_log" 
[5]="general_log" 
[6]="coloured_text" 
[7]="auto_start")   



declare -A opti
readd(){

    while read -ra line; do
        for word in "${line[@]}"; do
            if [[ $flag = "1" ]] 
            then
                ans=$word
                #echo -e -n "" $que $ans "\n"
                opti["${que}"]="${ans}"
                flag="0"
            fi
            if [[ $word = ":" ]] 
            then 
                flag='1'
            else
                que=$word
            fi
        done

done < data.txt

}

readd

matrix(){
    if [[ ${opti["coloured_text"]} = "true" ]]
    then
    for ((i=0; i<=${#1}; i++)); do
        echo -n "${1:$i:1}"
        sleep ${2} #.$(( 0 ))   #(RANDOM % 5)
    done
    else
    echo -e -n $1
    fi
    echo ""
}

rst(){
    exec $0 && exit 0
}

del(){
    echo -e -n "\n\b""\e[1A\e[K\r"
    echo  ""
}

sle(){
    if [[ ${opti["coloured_text"]} = "true" ]]
    then
    sleep $1
    fi
}

col(){
    if [[ ${opti["${da[6]}"]} = "true" ]]
    then
    echo $1
    fi
        
}

log(){
    if [[ ${opti["${da[1]}"]} = "true" ]]
    then
    x-terminal-emulator -e ./bot_logger.sh 2> /dev/null
    fi
    if [[ ${opti["${da[2]}"]} = "true" ]]
    then
    x-terminal-emulator -e ./mysql_logger.sh 2> /dev/null
    fi
}

Red=$(col '\033[0;31m')
Green=$(col '\033[0;32m')
Yellow=$(col '\033[1;33m')
lYellow=$(col '\033[0;33m')
NC=$(col '\033[0m')
kYellow=$(col '\033[0;37m')
kYe=$(col '\033[0;37m')
YE=$(col '\033[0;36m')

echo ""
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
sle 0.1
matrix " -------------------------------  " 0
echo ""


echo "1. Start"; sle 0
echo "2. Open Resource Folder"; sle 0
echo "3. Install Requirements"; sle 0
echo "4. Restart Database"; sle 0
echo "5. Settings"; sle 0
echo "6. Refresh"; sle 0
echo "7. About"; sle 0
echo "8. Exit"; sle 0
echo -e "\n"


abt(){

echo ""
echo "        _______   _______         "
sleep 0
echo "   __  ___  __ \ / __  __ _____   "
sleep 0
echo "  |_ \| __/' _| | |  \/__|_   _|  "
sleep 0
echo "   _\ | _|\`._\`\` | | ~| \/ || | "
sleep 0
echo "  /___|___|___/ | |__/\__/ |_|    "
sleep 0
echo "        _______/ \_______         "
sleep 0
echo ""
sleep 0.1

echo ""
bold=$(tput bold)
normal=$(tput sgr0)

matrix "          Developed By" 0
sleep 0.5
echo -e -n "\b""\e[1A\e[K\r"
matrix "         ${bold}Jesvi Jonathan${normal}" 0
sleep 0.5 
echo -e -n "\b""\e[1A\e[K\r"
echo -e "        By ${YE}${bold}Jesvi Jonathan${normal}${NC}"

#col=([1]='\033[0;31m' [2]='\033[0;32m' [3]='\033[1;33m' [4]='\033[0m' [5]='\033[1;36m' [6]='\033[1;30m' [7]='\033[0;35m' [8]='\033[0;30m') 
#for ((i=1; i<=8; i++)); do
#        echo -e -n "\n\b""\e[1A\e[K"
#        echo -e -n "          ${col[$i]}Jesvi Jonathan"
#        sleep 0
#    Done
#matrix " -------------------------------  " 0

echo ""
matrix " _______________________________" 0
echo ""
matrix "        Version : 0.7" 0
matrix "        Release : 12.10.2020" 0
matrix "          State : Stable" 0
matrix "           Type : Full" 0
matrix " _______________________________" 0
sleep 0.4
echo ""
echo -e -n "\n Main Webpage-1   "; sleep 0;echo -e -n "2-Support Group"
sleep 0
echo -e -n "\n  Source code-3   "; sleep 0;echo -e -n "4-Jesvi Bot"
sleep 0
echo -e -n "\n    Donations-5   "; sleep 0;echo -e -n "6-Return\n"
echo -e "\n"

while true; do

    echo -n -e ${Yellow}"\e[1A\e[K: "${NC}
    read -n1 input
    
    if [[ $input = "1" ]]
        then 
        echo -e "\bRedirecting to Official Webpage.."
        xdg-open https://jesvijonathan.github.io/jesvijonathan/ &> /dev/null
        sleep 0.7
        echo -n -e "\e[1A\e[K"
    elif [[ $input = "2" ]]
        then 
        echo -e "\bRedirecting to @Bot_Garage group.."
        xdg-open https://telegram.me/bot_garage &> /dev/null
        sleep 0.7
        echo -n -e "\e[1A\e[K"
    elif [[ $input = "3" ]]
        then 
        echo -e "\bJesvi Bot Main GitHub repository.."
        xdg-open https://github.com/jesvijonathan/Jesvi-Bot &> /dev/null
        sleep 0.7
        echo -n -e "\e[1A\e[K"
    elif [[ $input = "4" ]]
        then 
        echo -e "\bViewing Jesvi Bot in person"
        xdg-open https://telegram.me/jesvi_bot &> /dev/null
        sleep 0.7
        echo -n -e "\e[1A\e[K"
    elif [[ $input = "5" ]]
        then 
        echo -e "\bDeveloper Donation link (I'm Broke :P)"
        xdg-open https://github.com/jesvijonathan/Jesvi-Bot &> /dev/null
        sleep 0.7
        echo -n -e "\e[1A\e[K"
    elif [[ $input = "6" ]]
        then 
        echo -e "\bReturning.."
        sleep 0.7
        rst
    else
        sleep 0.2
        echo -e -n "\n\b" ${Red}"\e[1A\e[K\rInvalid Input.."${NC}
        sleep 0.5
    fi
    

    echo ""
done

}

wrida(){

opt=$1

d1="bot_logging : ${opt["bot_logging"]}"
d2="sql_logging : ${opt["sql_logging"]}"
d3="minimise_log : ${opt["minimise_log"]}"
d4="fresh_log : ${opt["fresh_log"]}"
d5="general_log : ${opt["general_log"]}"
d6="coloured_text : ${opt["coloured_text"]}"
d7="auto_start : ${opt["auto_start"]}"

txt="$d1\n$d2\n$d3\n$d4\n$d5\n$d6\n$d7\n"

echo -e $txt > data.txt
}

settings(){
    declare -A opt
    que=0
    ans=0

    flag='0'
    
    while read -ra line; do
        for word in "${line[@]}"; do
            if [[ $flag = "1" ]] 
            then
                ans=$word
                #echo -e -n "" $que $ans "\n"
                opt["${que}"]="${ans}"
                flag="0"
            fi
            if [[ $word = ":" ]] 
            then 
                flag='1'
            else
                que=$word
            fi
            #echo "$word";
        done;
    done < data.txt
    #echo "${opt["init"]}"
    #echo "${opt[@]}"

#for key in ${!opt[@]}; do 
#echo -e $key " : " ${opt["$key"]} "\n" ; done

reset 

dam=(
[1]="Live Log Bot on start" 
[2]="Live Log SQL on start" 
[3]="Minimise log window  " 
[4]="Clean log on start   " 
[5]="Database general log " 
[6]="Cool Text            " 
[7]="Auto start on login  ")       


for ((i=1; i<=7; i++)); do
        echo -e "${i}." "${dam[$i]} : " "${opt[${da[$i]}]}"
        sle 0
    done

echo -e "9. Return"
echo -e "\n"

while true; do
echo -n -e ${Yellow}"\e[1A\e[K: "${NC}
read ut

    if [[ $ut = "9" ]]
    then
        echo "returing.."
        sleep 1
        rst
  
    elif [[ $ut = "1" ]]
    then
        echo ""
    elif [[ $ut = "2" ]]
    then
        echo ""
    elif [[ $ut = "3" ]]
    then
        echo "Not possible as of rn..."
       
        opt["${da[$ut]}"]="true"
        
        sleep 2
        echo ""
    elif [[ $ut = "4" ]]
    then
        echo ""
    elif [[ $ut = "5" ]]
    then
        echo -e -n "\nTurning on mysql database"
        service mysql start &> /dev/null
        cd ../
        cd ../
        cd ./common
        sudo python3 ./general_log_switch.py
        cd $cur
        echo ""
        sleep 2
    elif [[ $ut = "6" ]]
    then
        echo ""
    elif [[ $ut = "7" ]]
    then
        echo ""
    else
        sleep 0.2
        echo -e  "\b" ${Red}"\e[1A\e[K\rInvalid Input.."${NC}
        sleep 0.5
        settings
    fi

    if [[ "${opt["${da[$ut]}"]}" = "true" ]]
        then
            opt["${da[$ut]}"]="false"
        else
            opt["${da[$ut]}"]="true"
    fi

    wrida opt
    settings
done
}

while true; do

    echo -n -e ${Yellow}"\e[1A\e[K: "${NC}
    read -n1 input
    
    if [[ $input = "1" ]]
        then reset
        log
        km="0"
        if [[ ${opti["${da[6]}"]} = "true" ]]
        then
        km="1"
        fi
        
        bash "./bin/run.sh" $km  2> /dev/null || bash "./run.sh" $km
        rst
    elif [[ $input = "2" ]]
        then
        xdg-open . >/dev/null 2>&1
        del
    elif [[ $input = "3" ]]
        then  reset
        bash "./bin/requirements_installer.sh" 2> /dev/null || bash "./requirements_installer.sh"
        rst
    elif [[ $input = "4" ]]
        then 
        #reset
        del
        echo -e "###############################"
        bash "./bin/mysql_restart_database.sh" 2> /dev/null || bash "./mysql_restart_database.sh"
        rst
    elif [[ $input = "5" ]]
        then 
        settings
        rst
    elif [[ $input = "6" ]] 
        then
        rst
    elif [[ $input = "7" ]] 
        then reset
        abt
    elif [[ $input = "8" ]]
        then 
        del
        echo -e -n "\e[1A\e[KExiting.."
        sle 0.1
        del
        matrix "Jesvi Bot" 0
        sle 0.1
        matrix "By Jesvi Jonathan" 0
        sle 0
        echo -e "\n"
        exit 0
# python3 ./$PWD/main.py
    elif [[ $input = "l" ]]
        then
        printf '\033[8;24;34t'
    elif [[ $input = "d" ]]
    then
        echo -e -n "\bOpening Database Viewer"
        sle 0.2
        echo -n "."
        sle 0.2
        echo -n "."
        x-terminal-emulator -e ./mysql_db_view.sh
        sleep 0.3
        echo ""
    else
        sleep 0.2
        echo -e -n "\n\b" ${Red}"\e[1A\e[K\rInvalid Input.."${NC}
        sleep 0.5
        echo  ""
    fi
done
fi

sleep 20
