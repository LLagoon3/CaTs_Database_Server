#!/bin/bash

OS=$(uname -s)

if [ "$OS" == "Linux" ]; then
    DISTRO=$(lsb_release -is)
    if [ "$DISTRO" == "Ubuntu" ]; then
        echo "Ubuntu"
        apt-get install -y cron
    elif [ "$DISTRO" == "Darwin" ]; then
        echo "Mac OS"
        brew install cron 
    else
        echo "Not Linux"
    fi
else
    echo "OS Not Found"
fi

mkdir /tmp/mysql
SCRIPT_DIR=$(pwd)
{ crontab -l && echo "* * * * * $SCRIPT_DIR/mysql_backup.sh > /tmp/mysql/mysql_backup.log 2>&1"; } | crontab -

