#!/usr/bin/env bash
# Sets up webservers for deployment: (Run script on both servers)
# If not done, does the following:
#     installs Nginx; creates folders /data/, /data/web_static/,
#     /data/web_static/releases/, /data/web_static/shared,
#     /data/web_static/releases/test
#     /data/web_static/releases/test/index.html (with some content)
# Create symbolic link /data/web_static/current to data/web_static/releases/test
#     delete and recreate symbolic link each time script's ran
# Recursively assign ownership of /data/ folder to user and group 'ubuntu'
# Update the Nginx config to serve content of /data/web_static/current/ to hbnb_static (ex: https://mydomainname.tech/hbnb_static)
#     restart Nginx
# curl localhost/hbnb_static/index.html should return sample text"
FAKE_HTML="<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>"
SERVER_BLOCK_PATH="/etc/nginx/sites-available/default"
ROOT_DIR="/data"
RELEASES="$ROOT_DIR/web_static/releases/test"
SHARED="$ROOT_DIR/web_static/shared"
LINK="$ROOT_DIR/web_static/current"
ADD_WEBSTATIC="\n\tlocation /hbnb_static/ {\n\t\talias $LINK/;\n\t}\n"

sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo mkdir -p "$RELEASES" "$SHARED"
echo -e "$FAKE_HTML" | sudo tee "$RELEASES/index.html"
sudo ln -sf "$RELEASES" "$LINK"
sudo chown -hR ubuntu:ubuntu "$ROOT_DIR"
sudo sed -i "46 a\ $ADD_WEBSTATIC" "$SERVER_BLOCK_PATH"
sudo service nginx restart
