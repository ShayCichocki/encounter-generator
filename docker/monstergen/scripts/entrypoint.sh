#!/bin/bash

cd /monstergen/app/ux && npm install
cd /monstergen/app/ux && ionic build
exec /usr/bin/supervisord -c /etc/supervisor/supervisord.conf
