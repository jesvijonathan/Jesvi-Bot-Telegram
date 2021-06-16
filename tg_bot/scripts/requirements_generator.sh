title="Requirements Generator"
echo -e '\033]2;'$title'\007'

echo Powered by pigar
echo
echo Started Requirements.bat
echo
echo Installing pigar..
echo
echo
sudo python3 -m pip install pigar
echo
echo
echo Creating list..
echo
sudo python3 -m pigar
echo
echo Done listing dependencies to "requirements.txt"
#start notepad "requirements.txt"
cat ./requirements.txt
sleep 10