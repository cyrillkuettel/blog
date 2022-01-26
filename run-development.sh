#!/bin/bash
# first, remove all exited containers
docker stop $(docker ps -a -q)
docker rm $(docker ps --filter status=exited -q)

docker run --name cyrill_blog --volume="/home/demo/blog/web:/srv/jekyll" -p 4000:4000 -it jekyll/jekyll:3.8 jekyll serve --watch --drafts
