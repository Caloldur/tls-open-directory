# tls-open-directory
A simple way to deploy a directory listing. 

### Building
```
git clone https://github.com/Caloldur/tls-open-directory.git
cd ./tls-open-directory
mkdir ./data
mkdir ./ssl
docker build -t tls-open-directory .
```

### Running
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
      - SERVER_ADDRESS=0.0.0.0
      - PORT=44431
      - DATA_DIRECTORY=/data
      - CERT_FILE=/ssl/fullchain.pem
      - KEY_FILE=/ssl/privatekey.pem
    volumes:
      - /<Your-Data-Directory>:/data #Change this to the directory you wish to serve
      - /<Your-Certs-Directory>/certs:/ssl #Change this to the location of your fullchain.pem and privatekey.pem
```