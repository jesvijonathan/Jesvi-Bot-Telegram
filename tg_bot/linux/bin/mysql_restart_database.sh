#!/bin/bash

#title="restart_database"
#echo -e '\033]2;'$title'\007'

echo ""
echo "Restarting MYSQL Database (~30sec)-"
echo ""

#service mysql stop
#service mysql start

service mysql restart
#sudo /etc/init.d/mysql restart

echo ""
echo -n "Done"
sleep 0.4
echo -n "."
sleep 0.4
echo -n "."
sleep 0.4 
echo -n "."
sleep 1