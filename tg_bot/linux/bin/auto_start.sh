#!/bin/bash
### BEGIN INIT INFO
# Provides:          haltusbpower
# Required-Start:    $all
# Required-Stop:
# Default-Start:     2 3 4 5
# Default-Stop:
# Short-Description: Halts USB power...
### END INIT INFO

PATH=/sbin:/usr/sbin:/bin:/usr/bin

sudo cp jesvi_bot_service.sh /etc/systemd/system/
chmod +x  /etc/systemd/system/jesvi_bot_service.sh+-*
# sudo systemctl add jesvi_bot_service.sh
sudo systemctl enable jesvi_bot_service.sh

#systemctl enable jesvi_bot_service.sh

read -p "press any key to exit"