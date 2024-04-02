#!/bin/bash

OS=$(uname -s)

if [ "$OS" == "Linux" ]; then
    echo "Linux"
    sudo apt-get install -y cron
elif [ "$DISTRO" == "Darwin" ]; then
    echo "Mac OS"
    brew install cron 
else
    echo "Not Linux"
fi


SCRIPT_DIR=$(pwd)
{ crontab -l && echo "0 * * * * $SCRIPT_DIR/mysql_backup.sh > /tmp/mysql_backup.log 2>&1"; } | crontab -
sudo usermod -aG docker $USER
docker exec mysql-server GRANT PROCESS ON *.* TO 'cats'@'localhost'
