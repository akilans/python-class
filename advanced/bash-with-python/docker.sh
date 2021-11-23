#! /bin/bash
set -ex # prints all the command while executing

echo "getting all the docker containers"

docker container ls -a --format "{{.Names}},{{.ID}},{{.Status}}" > containers.txt
docker container ls -a --format "{{ json .}}" | jq -s > containers.json

python container.py 
python container-json.py

