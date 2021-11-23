import json

with open("containers.json", "r") as container:
    container_list = json.loads(container.read())
    for container in container_list:
        print("Conatiner name {} - Container status - {}".format(
            container["Names"], container["State"]))
