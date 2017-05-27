#!/bin/bash

cd ~/src/RiverForestServiceClub.github.io/
#lftp www.riverforestserviceclub.org -e "mirror --script=/home/razeh/foo -R --no-perms --exclude=".git" --exclude="stats""
lftp -e "set ftp:ssl-allow off;" www.riverforestserviceclub.org -e "mirror -R --no-perms --exclude=".git" --exclude="stats""

