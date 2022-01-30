#!/bin/bash

git fetch origin
git pull origin main
/bin/bash ../stop.sh
/bin/bash ./run-prod.sh
