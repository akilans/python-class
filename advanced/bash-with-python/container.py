with open("containers.txt", "r") as container:
    lines = container.readlines()

    for line in lines:
        data_list = line.split(",")
        print(
            "Container name - {} and container status - {}".format(data_list[0], data_list[2]))
        print(
            "Container name - %s and container status - %s" % (data_list[0], data_list[2]))
        print(
            f"""Container name - {data_list[0]} and container status - {data_list[2]}""")
