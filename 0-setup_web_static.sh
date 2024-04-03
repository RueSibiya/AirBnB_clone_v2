#!/usr/bin/env bash
#Script to set up web servers for deployment of web_static

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

# Create necessary directories if they don't exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/current/

# Create fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of /data/ to ubuntu user and group
sudo chown -R kathy2470:kathy2470 /data/

# Update Nginx configuration
config_content=$(cat <<EOF
server {
    listen 80;
    server_name _;

    location /hbnb_static {
        alias /data/web_static/current/;
    }

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    error_page 404 /404.html;
    location = /404.html {
        root /usr/share/nginx/html;
        internal;
    }

    add_header X-Served-By $HOSTNAME;

    location / {
        try_files $uri $uri/ =404;
    }
}
EOF
)
echo "$config_content" | sudo tee /etc/nginx/sites-available/default > /dev/null

# Restart Nginx
sudo service nginx restart

exit 0
