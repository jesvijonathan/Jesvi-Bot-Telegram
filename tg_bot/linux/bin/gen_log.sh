echo "Press 'y' to turn ON & 'n' to turn OFF mysql general logging (increases bg cpu usage) : "
read i

n="ON"
if [ $i = "y" ]
then
    n="ON"
else
    n="OFF"
fi

echo "\nTurning on mysql database"
sudo service mysql start &> /dev/null
sleep 4

cd ../
cd ../
cd ./common
python3 ./general_log_switch.py $n
cd $cur

echo ""
sleep 2