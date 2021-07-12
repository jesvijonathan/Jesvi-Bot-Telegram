echo "Creating bot launcher shortcut-"

sleep 0.2
echo "Setting directories"
cur=${PWD}
cd ../
cd ../
res=${PWD}

cd $cur 

sleep 0.2
echo "Creating .desktop content"

txt="[Desktop Entry]
Version=6.1
Name=Jesvi Bot
Comment=Bot Developed By Jesvi
Exec=$cur/jesvi_bot.sh
Icon=$res/common/res/icon.ico
Terminal=true
Type=Application
Categories=Utility;Application;"

echo "$txt" > JesBot.desktop

sleep 0.2
echo "Setting permission"
chmod +x JesBot.desktop

sleep 0.2
echo "Placing shortcut"
cp JesBot.desktop ~/Desktop

nx="$res/linux"
cd $cur

cp JesBot.desktop ${nx}

#mv JesBot.desktop ~/Desktop
sleep 0.2
echo "Launcher succeesfully created !"
sleep 1