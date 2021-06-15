#!/bin/bash
# chkconfig: 2345 20 80
# description: Description comes here....

# Source function library.
. /etc/init.d/functions

start() {
    sudo /root/Documents/GitHub/Jesvi-Bot-Telegram/bin/start.sh 
}

stop() {
    # code to stop app comes here 
    # example: killproc program_name
}

case "$1" in 
    start)
       start
       ;;
    stop)
       stop
       ;;
    restart)
       stop
       start
       ;;
    status)
       echo "Jesvi Bot Service Running Here.."
       echo "You can stop this by using"
       ;;
    *)
       echo "Usage: $0 {start|stop|status|restart}"
esac

exit 0 

