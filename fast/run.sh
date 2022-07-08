#!/bin/bash
docker stop $(docker ps -a -q)
docker rm $(docker ps --filter status=exited -q)
docker build -t fast -f Dockerfile-local .
docker run -d --name mycontainer -p 80:80 -v /home/cyrill/blog/fast/app:/code/app fast
