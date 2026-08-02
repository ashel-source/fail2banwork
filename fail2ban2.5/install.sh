#!/bin/bash


sudo apt update
sudo apt install ipset -y
cd /www/fail2ban2.5
sudo cp -rf ./fail2banpy/* /www/server/panel/plugin/fail2ban/
sudo cp -rf ./fail2ban/action.d/* /etc/fail2ban/action.d
sudo cp -rf ./sh/* /usr/local/bin
sudo cp -rf ./log/* /etc/logrotate.d
sudo chmod 644 /etc/fail2ban/action.d/nginx-block-iptables-ipset.conf
sudo chmod 644 /etc/fail2ban/action.d/iptables-ipset.conf
sudo chmod 644 /etc/fail2ban/jail.local
sudo chmod 644 /www/server/panel/plugin/fail2ban/fail2ban_main.py
sudo chmod 644 /www/server/panel/plugin/fail2ban/index.html
sudo chmod 644 /etc/logrotate.d/fail2ban
sudo chmod 755 /usr/local/bin/check-ip.sh
sudo chmod 755 /usr/local/bin/unban-ip.sh
sudo chmod 755 /usr/local/bin/ban-ip.sh
sudo chown root:root /etc/fail2ban/action.d/nginx-block-iptables-ipset.conf
sudo chown root:root /etc/fail2ban/action.d/iptables-ipset.conf
sudo chown root:root /etc/fail2ban/jail.local
sudo chown root:root /www/server/panel/plugin/fail2ban/fail2ban_main.py
sudo chown root:root /www/server/panel/plugin/fail2ban/index.html
sudo chown root:root /usr/local/bin/check-ip.sh
sudo chown root:root /usr/local/bin/unban-ip.sh
sudo chown root:root /usr/local/bin/ban-ip.sh
sudo chown root:root /etc/logrotate.d/fail2ban



sudo sed -i '/^\[DEFAULT\]/,/^\[/{s/^[# ]*banaction *= *.*/banaction = nginx-block-iptables-ipset/}' /etc/fail2ban/jail.local
sudo systemctl restart fail2ban
sudo chattr -R -i /www/wwwroot
sudo chown -R www:www /www/wwwroot
sudo find /www/wwwroot -type d -exec chmod 755 {} \;
sudo find /www/wwwroot -type f -exec chmod 644 {} \;
sudo find /www/wwwlogs -type f -name "*.log" -exec chown www:www {} \; -exec chmod 644 {} \;




sudo apt update && \
sudo apt install ipset -y && \
cd /www/fail2ban2.5 && \
sudo cp -rf ./fail2banpy/* /www/server/panel/plugin/fail2ban/ && \
sudo cp -rf ./fail2ban/action.d/* /etc/fail2ban/action.d && \
sudo cp -rf ./sh/* /usr/local/bin && \
sudo cp -rf ./log/* /etc/logrotate.d && \
sudo chmod 644 /etc/fail2ban/action.d/nginx-block-iptables-ipset.conf && \
sudo chmod 644 /etc/fail2ban/jail.local && \
sudo chmod 644 /www/server/panel/plugin/fail2ban/fail2ban_main.py && \
sudo chmod 644 /www/server/panel/plugin/fail2ban/index.html && \
sudo chmod 644 /etc/logrotate.d/fail2ban && \
sudo chmod 755 /usr/local/bin/check-ip.sh && \
sudo chmod 755 /usr/local/bin/unban-ip.sh && \
sudo chmod 755 /usr/local/bin/ban-ip.sh && \
sudo chown root:root /etc/fail2ban/action.d/nginx-block-iptables-ipset.conf && \
sudo chown root:root /etc/fail2ban/jail.local && \
sudo chown root:root /www/server/panel/plugin/fail2ban/fail2ban_main.py && \
sudo chown root:root /www/server/panel/plugin/fail2ban/index.html && \
sudo chown root:root /usr/local/bin/check-ip.sh && \
sudo chown root:root /usr/local/bin/unban-ip.sh && \
sudo chown root:root /usr/local/bin/ban-ip.sh && \
sudo chown root:root /etc/logrotate.d/fail2ban && \
sudo sed -i '/^\[DEFAULT\]/,/^\[/{s/^[# ]*banaction *= *.*/banaction = nginx-block-iptables-ipset/}' /etc/fail2ban/jail.local && \
sudo chattr -R -i /www/wwwroot && \
sudo chown -R www:www /www/wwwroot && \
sudo find /www/wwwroot -type d -exec chmod 755 {} \; && \
sudo find /www/wwwroot -type f -exec chmod 644 {} \; && \
sudo find /www/wwwlogs -type f -name "*.log" -exec chown www:www {} \; -exec chmod 644 {} \; && \
sudo systemctl restart fail2ban
