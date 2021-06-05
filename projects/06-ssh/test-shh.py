import paramiko
import json
import random

ssh = paramiko.SSHClient()

# Below we set the policy to auto add hosts to known_hosts
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

with open("servers.json") as f:
    servers = json.load(f)

    for server in servers:
        print(server["cmd"])
        ssh.connect(server["server_ip"], 22,
                    server["user_name"], server["password"])
        stdin, stdout, stderr = ssh.exec_command(server["cmd"])

        list1 = [1, 2, 3, 4, 5, 6]
        random_number = str(random.choice(list1))

        with open("server_output"+random_number+".txt", "w") as contentfile:
            contentfile.write(str(stdout.readlines()))
