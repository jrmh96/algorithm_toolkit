Running app as a docker container:

Starting from this folder, navigate to /atkBaseImage

Build the atk base image: docker build . -t atk_base:master

where "atk_base" is the name of the image, and "master" is the tag
That should build a base image for the ATK with all the dependencies installed.
After this, we build a clean project in the docker folder and populate it with the example project in this folder.

Navigate to myproject folder, where the dockerfile for the example project lives

Build the deploy image:
docker build . -t atk_twitter_deploy:master, where again, "atk_twitter_deploy" is the name of the image, and "master" is the tag

Once the image is built, it can be run as a container with the following command:

docker run -p 5000:5000 atk_twitter_deploy:master

The -p 5000:5000 will expose port 5000 to the host machine.

Now go to a web browser on the host machine and type localhost:5000, you should see the atk running locally.

The starter docker project comes with some example chains. The example video as well as the pre-trained config files are all under myproject/assets/data, 
you can use the included chain called inferenceparammethod to run a simple chain
that outputs results to the browser with static twitter data.

To configure your own twitter api keys:

To ping the search endpoint we need to know: the twitter dev environment label, the consumer api key, and the consumer api secret.

While the atk_twitter_deploy:master container is running, open a new bash shell and in any folder run:
docker ps
and observe the container id of the atk container. Now run

docker exec -it [ID] /bin/bash 

replacing ID with the container ID. This will open an interactive bash shell within the container,
which will allow us to update the necessary components.
Within this bash shell, navigate to the /atk_project folder and run

echo "TWITTER_ENV_LABEL=\"[...]\"" >> .env
echo "TWITTER_CONSUMER_API_KEY=\"[...]\"" >> .env
echo "TWITTER_CONSUMER_API_SECRET\"[...]\"" >> .env

replacing [...] with your twitter developer environment label, app consumer api key, and app consumer api secret respectively. You can also find the ATK api key under ATK_API_KEY in the .env file


