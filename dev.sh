#!/bin/bash 

echo "Setting up env"

source /home/nicky/.cache/pypoetry/virtualenvs/canbuscollectionmodule-2LESvuvc-py3.8/bin/activate

echo "setting up network interface "

sudo slcand -o -c -s6 /dev/ttyACM1 can0   
sudo ip link set can0 up   

echo "Starting program..."


poetry run python3 Canbuscollectionmodule/__main__.py