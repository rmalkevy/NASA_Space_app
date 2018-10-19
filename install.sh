#!/bin/bash
docker-machine rm Char -y;
rm -rf /tmp/.docker;
rm -rf ~/Library/*42_cache*;
mkdir /tmp/.docker;
ln -s /tmp/.docker/ ~/.docker;
docker-machine create --driver virtualbox --virtualbox-memory 4096 Char;
eval "$(docker-machine env Char)";
docker-compose up --build --no-start;
docker-compose run frontend npm install;
docker-compose up -d;
open -a "/Applications/Google Chrome.app" 'http://192.168.99.100:4000/';
