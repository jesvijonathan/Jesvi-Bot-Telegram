echo "Downloading Latest Release of Jesvi Bot From Source"
curl -s -L https://github.com/jesvijonathan/Jesvi-Bot-Telegram/releases/latest | egrep -o '/jesvijonathan/Jesvi-Bot-Telegram/releases/download/[v]?[0-9.]*/Release.zip' | wget --base=http://github.com/ -i - -O latest_release.zip
echo "Unpacking Package..."
unzip -o latest_release.zip -d latest_release

cd ../../

echo "Backup in progress.."
cp ./scripts/config.py ./common/update/backup

cp ./linux/bin/data.txt ./common/update/backup
cp ./windows/bin/data.txt ./common/update/backup


echo "Replacing with Latest files..."
cp -r ./common/update/latest_release/* ../

echo "Adding user config.."
cp ./common/update/backup/config.py ./scripts/ 

echo "Finished, Plz Check if everything went well..."
#mv /latest_release/* ../