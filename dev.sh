#!/bin/bash 

echo "Setting up env"

source /home/nicky/.cache/pypoetry/virtualenvs/canbuscollectionmodule-2LESvuvc-py3.8/bin/activate

echo "Starting program..."

poetry run python3 Canbuscollectionmodule/__main__.py