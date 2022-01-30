#!/bin/bash

git fetch origin
git pull origin main
docker-compose -f docker-compose-prod.yml down
docker-compose -f docker-compose-prod.yml up --build --detach
