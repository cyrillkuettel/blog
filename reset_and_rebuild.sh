#!/bin/bash

git fetch origin
git reset --hard origin/main
docker-compose -f docker-compose-prod.yml down
sudo /bin/bash ./run-prod.sh
