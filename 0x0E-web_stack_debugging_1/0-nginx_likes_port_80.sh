#!/bin/bash

# Update package list and install nginx
apt-get update
apt-get install -y nginx

# Ensure Nginx is enabled to start on boot and start it immediately
systemctl enable nginx
systemctl start nginx

# Ensure Nginx is configured to listen on port 80
NGINX_CONF="/etc/nginx/sites-available/default"
if ! grep -q "listen 80;" $NGINX_CONF; then
    sed -i 's/listen 80 default_server;/listen 80;/g' $NGINX_CONF
    sed -i 's/listen \[::\]:80 default_server;/listen \[::\]:80;/g' $NGINX_CONF
    systemctl restart nginx
fi

# Allow traffic on port 80 through the firewall
ufw allow 80/tcp
ufw reload

# Verify Nginx is running and listening on port 80
if curl -s 0:80 | grep -q "Welcome to nginx!"; then
    echo "Nginx is successfully installed and running on port 80"
else
    echo "Nginx is not running on port 80"
fi

