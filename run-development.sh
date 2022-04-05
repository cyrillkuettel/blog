 #!/bin/bash
# first, remove all exited containers
docker stop $(docker ps -a -q)
docker rm $(docker ps --filter status=exited -q)

blog="blog/web:/srv/jekyll"

full_path="$HOME/$blog"

docker run --name cyrill_blog --volume=$full_path -p 4000:4000 -it jekyll/jekyll:3.8 jekyll serve --watch --drafts --incremental
