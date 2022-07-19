#!/bin/bash

git fetch origin
git reset --hard origin/main
docker-compose -f docker-compose-prod.yml down

# rebuild, not very efficent, but it works
docker stop $(docker ps -a -q)
docker rm $(docker ps --filter status=exited -q)
docker run --rm --volume="/home/cyrill/blog/web:/srv/jekyll" -it jekyll/jekyll:3.8 jekyll build
docker run --name cyrill_blog --volume="/home/cyrill/blog/web:/srv/jekyll" -p 4000:4000 -it jekyll/jekyll:3.8 jekyll serve --watch --drafts

sudo /bin/bash ./run-prod.sh
