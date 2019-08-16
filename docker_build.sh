#!/bin/sh
cd atkBaseImage
docker build . -t atk_base:master
cd ../myproject
docker build . -t atk_twitter_deploy:master
docker run -p 5000:5000 atk_twitter_deploy:master
