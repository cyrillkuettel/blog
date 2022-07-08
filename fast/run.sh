#!/bin/bash
docker stop $(docker ps -a -q)
docker rm $(docker ps --filter status=exited -q)
# docker build -t fast -f Dockerfile-local .
# docker run -d --name fastcontainre -p 80:80 fast /start-reload.sh | xargs -I{} docker logs -f {}
docker-compose -f /home/cyrill/blog/docker-compose-prod.yml up -d python
