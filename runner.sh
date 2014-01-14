#!/bin/bash
# Run the webserver, run the tests and kill the webserver!
python server.py &
ID=$!

# Sleep is necessary to setup the server
sleep 0.5

python freetests.py
python not-free-tests.py
kill $ID
#pkill -P $$
