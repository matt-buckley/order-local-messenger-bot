# order-local-messenger-bot
Facebook Messenger bot with easy setup to support local food delivery during COVID-19 crisis

## Setup file

To prevent writing a load of constants in the file and hardcoding passwords, create a file `setup.conf` and set it up as a 
normal .ini file. Add any extra configuration that's required, but be sure to add an example in setup.conf.sample. As setup.conf is in .gitignore.  


## Dev setup

With Docker:

    docker build -t order-local-messenger:latest ./server
    docker run -ti --env FLASK_ENV=development -p 127.0.0.1:5000:5000 -v $PWD/server:/usr/src/server order-local-messenger:latest
    
Without docker:

Use Python 3. Set up and activate a virtual environment if required

    python3 -m venv venv
    source venv/bin/activate    

Then:
    
    pip install --user -r server/requirements.txt
    export FLASK_APP="server.app"  
    export FLASK_HOST="127.0.0.1"
    export FLASK_ENV="development"
    flask run 
    
## Running on a server

In order to test the interactions with the page in Facebook, a real server is required, with SSL.  The simplest way is to
use letsencrypt, but any way will do.  To make letsencrypt work, we have an NGINX proxy in front of the Flask app and some
convenience Docker containers to set up SSL. The `$DOMAIN` and `$EMAIL` fields are expected in the docker-compose.yaml file:

    export DOMAIN=mydomain.example.com
    export EMAIL=myemail@example.com
    docker-compose up -d
    docker-compose logs -f --tail=100

When this is not in production, you may want to change the bind mounts for Flask in docker-compose.yaml so you do not need
to keep rebuilding the Flask image:

    volumes:
      - ./letsencrypt:/etc/letsencrypt
      - ./:/usr/src/
      
      