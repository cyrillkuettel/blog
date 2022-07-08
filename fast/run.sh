#!/bin/bash
docker stop $(docker ps -a -q)
docker rm $(docker ps --filter status=exited -q)
docker-compose -f /home/cyrill/blog/docker-compose-prod.yml up -d python
