#mysql
echo "Database viewer"
echo ""
echo "0 To show all tables"
echo "1 user_base"
echo "2 chat_base"
echo "3 link_base"
echo "4 note_base"
echo "5 settings_base"
echo "6 warn_base"
echo "7 cit_timetable_base"
echo "8 cit_subjects_base"
echo ""

table="chat_base"

read input

echo "--------------------"
echo ""

if [ $input = "0" ]
    then
    mysql -Bse "USE jesvi_bot_database_main;SHOW TABLES;"
    else
    if [ $input = "1" ]
        then
        table="user_base"
    fi
    if [ $input = "2" ]
        then
        table="chat_base"
    fi
    if [ $input = "3" ]
        then
        table="link_base"
    fi
    if [ $input = "4" ]
        then
        table="note_base"
    fi
    if [ $input = "5" ]
        then
        table="settings_base"
    fi
    if [ $input = "6" ]
        then
        table="warn_base"
    fi
    if [ $input = "7" ]
        then
        table="cit_timetable_base"
    fi
    if [ $input = "8" ]
        then
        table="cit_subjects_base"
    fi  


    mysql -Bse "USE jesvi_bot_database_main;SELECT * FROM $table;"
fi  



echo ""
echo "--------------------"
echo "press 'r' to restart and any other button to quit"

read input

if [ $input = "r" ]
    then
    reset
    exec "$PWD/database_view.sh"
    else
    exit 0  
fi  
