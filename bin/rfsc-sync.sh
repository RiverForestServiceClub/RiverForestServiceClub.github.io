#!/bin/bash

cd ~/Documents/River-Forest-Service-Club/
#lftp www.riverforestserviceclub.org -e "mirror --script=/home/razeh/foo -R --no-perms --exclude=".git" --exclude="stats""
lftp -e "set ftp:ssl-allow off;" www.riverforestserviceclub.org -e "mirror -R --no-perms --exclude=".git" --exclude="stats""

