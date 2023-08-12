#
We will use a channel layer that uses Redis as its backing store. 
To start a Redis server on port 6379, run the following command (press Control-C to stop it):

$ docker run --rm -p 6379:6379 redis:7