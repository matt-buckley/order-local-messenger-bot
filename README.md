# order-local-messenger-bot
Facebook Messenger bot with easy setup to support local food delivery during COVID-19 crisis

## Dev setup

With Docker:

    docker build -t order-local-messenger:latest ./server
    docker run -ti --env FLASK_ENV=development -p 127.0.0.1:5000:5000 -v $PWD/server:/usr/src/server order-local-messenger:latest
    
Without docker:

Use Python 3. Set up and activate a virtual environment if required

    python3 -m venv venv
    source venv/bin/activate    

Then:

    cd server
    pip install --user -r requirements.txt
    export FLASK_APP="server.app"  
    export FLASK_HOST="127.0.0.1"
    export FLASK_ENV="development"
    cd ..
    flask run 
    
