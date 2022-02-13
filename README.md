# tls-open-directory
A simple way to deploy a directory listing.
#Systemd
```
git clone https://github.com/Caloldur/tls-open-directory.git
cd ./tls-open-directory
```
Set the environment variables for the user that this service will be running as.
```
vi /home/USERNAME/.bash_profile
```
Modify and/or append these lines to the bash_profile
```
TOD_DATA_DIRECTORY=/directory_to_serve
TOD_SERVER_ADDRESS=0.0.0.0 #This can be set to the ip you wish to listen on
TOD_PORT=4443 #This can be any port you wish to listen on
TOD_CERT_FILE=/ssl/fullchain.pem #Set this to the location of your tls fullchain.pem file
TOD_KEY_FILE=/ssl/privatekey.pem #Set this to the location of your tls privatekey.pem file
```
Open and modify tls-open-directory.service to include the username and path to the script.
```
vi ./tls-open-directory.service
User=ChangeMe
ExecStart=/usr/bin/python <location of main.py>
```
copy the service file to systemd
````
$ cp ./tls-open-directory.service /etc/systemd/system/tls-open-directory.service
````
Run and enable the service
````
$ systemctl start tls-open-directory.service
$ systemctl enable tls-open-directory.service
````
#Docker
### Building Docker Image
```
git clone https://github.com/Caloldur/tls-open-directory.git
cd ./tls-open-directory
mkdir ./data
mkdir ./ssl
docker build -t tls-open-directory .
```
### Running Docker Image
docker-compose.yaml
```
version: '2'
services:
  openDirectory:
    image: caloldur/tls-open-directory
    container_name: open-directory-service
    ports:
      - "44431:44431"
    restart: always
    environment:
      - TOD_SERVER_ADDRESS=0.0.0.0
      - TOD_PORT=44431
      - TOD_DATA_DIRECTORY=/data
      - TOD_CERT_FILE=/ssl/fullchain.pem
      - TOD_KEY_FILE=/ssl/privatekey.pem
    volumes:
      - /<Your-Data-Directory>:/data #Change this to the directory you wish to serve
      - /<Your-Certs-Directory>/certs:/ssl #Change this to the location of your fullchain.pem and privatekey.pem
```