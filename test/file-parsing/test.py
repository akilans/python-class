import csv
from sys import exit

where_to_append = "Emulator2"
host_name_to_append = "NewHostName01"
content = ""


with open('test', newline='') as netGps:
    ng_reader = csv.reader(netGps, delimiter='\n')
    for ng in ng_reader:

        if len(ng) > 0 and ng[0][0:len(where_to_append)] == where_to_append:
            # find last character
            emulator2_string = ng[0]
            emulator2_string_len = len(ng[0])
            last_char = emulator2_string[emulator2_string_len - 1]

            if last_char == "\\":
                print("Error - Please remove \ from ", where_to_append)
                exit(1)
            else:
                print(".....Found.......")
                content = content + ng[0] + " "+host_name_to_append + "\n"

        else:
            if len(ng) > 0:
                content = content + ng[0] + "\n"
            else:
                content = content + "\n"

        # print(ng)

# print(content)

with open("test", "w") as f:
    f.write(content)

print("Wrote file successfully")
