#!/bin/bash

cd /encountergenux && npm install
exec /usr/bin/supervisord -c /etc/supervisor/supervisord.conf
