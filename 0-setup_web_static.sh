#!/usr/bin/env bash
##
# Install nginx if it doesn't Exists
##
echo "Setting up server"
prog="nginx"
if ! command -v "$prog" &> '/dev/null' 
then
		sudo apt-get -y  update
		sudo apt-get -y install nginx
		sudo service ufw start
		sudo ufw allow ssh
		sudo ufw allow 'Nginx HTTP'
		sudo chown -R "$USER":"$USER" '/var/www/html/'
		echo 'Hello World!' > '/var/www/html/index.html'

		# create  custom header
		search='server_name _;'
		repl="a \ \ \ \ \ \ \ \ add_header X-Served-By \$hostname;"
		sudo sed -i "/$search/$repl" /etc/nginx/sites-available/default
		sudo service nginx restart
fi

##
# Create project directories
##
sudo mkdir -p '/data/web_static/releases/test'
sudo mkdir -p '/data/web_static/shared'
sudo chown -R "$USER":"$USER" '/data/'
echo '<p>Welcome to Holberton</p>' > '/data/web_static/releases/test/index.html'
##
# Creating symbolix link
##
if [ -e '/data/web_static/current' ]
then
	rm -rf '/data/web_static/current'
else
	ln -s '/data/web_static/releases/test/' '/data/web_static/current'
fi
sudo chown -R "$USER":"$USER" '/etc/nginx/'
config_string="events {}\n\nhttp {\n\tserver {\n\t\tlocation /hbnb_static {\n\t\t\t\talias /data/web_static/current/;\n\t\t\t}\n\t\t}\n}"
echo -e "$config_string" > '/etc/nginx/nginx.conf'
echo -e 'Finished setting up project directories'
