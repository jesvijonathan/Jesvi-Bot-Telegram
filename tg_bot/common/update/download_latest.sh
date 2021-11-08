echo "Downloading Latest Release of Jesvi Bot From Source"
curl -s -L https://github.com/jesvijonathan/Jesvi-Bot-Telegram/releases/latest | egrep -o '/jesvijonathan/Jesvi-Bot-Telegram/releases/download/[v]?[0-9.]*/Release.zip' | wget --base=http://github.com/ -i - -O latest_release.zip
echo "Unpacking Package..."
unzip -o latest_release.zip -d latest_release