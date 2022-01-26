#!/bin/bash

docker run --rm --volume="/home/demo/blog/web:/srv/jekyll" -it jekyll/jekyll:3.8 jekyll build

