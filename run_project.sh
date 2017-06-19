#!/usr/bin/env bash

#build and run server
cd url_shortener
docker build -t pyxpyx/url_shortener .
docker run --name url_server -d -p 4000:5000 pyxpyx/url_shortener
container_id=$(docker ps -qf "name=url_server")
cd ..

#build and run database
cd postgresql
docker build -t pyxpyx/url_db .
docker run -e POSTGRES_USER=root -e POSTGRES_PASSWORD=root --name url_db -v /var/lib/postgresql/9.4/main:/var/lib/postgresql/data --link "$container_id":pyxpyx/url_db postgres


