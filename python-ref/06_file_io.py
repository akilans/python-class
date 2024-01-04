import sys
import csv

# create csv file
def create_csv():
    friends = [
        {'name': 'Alex', 'place': 'Bangalore'},
        {'name': 'Jegan', 'place': 'Coimbatore'},
        {'name': 'Kumar', 'place': 'Chennai'}
    ]

    headers = friends[0].keys()
    print(headers)

    with open("new_friends.csv","w") as file:
        writer = csv.DictWriter(file,fieldnames=headers)

        writer.writeheader()
        writer.writerows(friends)

# write data into file
def write_names():
    with open("names.txt","a") as f:
        for name in sys.argv[1:]:
            f.write(f"{name}\n")

# read data from file
def read_names():
    with open("names.txt","r") as f:
        for line in f:
            print(line.rstrip())

# read csv file
def read_friends():
    friends = []
    with open("friends.csv","r") as f:
        for line in f:
            name, place = line.strip().split(",")
            friends.append(f"{name} is living in {place}")
    
    for friend in sorted(friends):
        print(friend)

# read csv file and sort
def sort_friends():
    friends = []
    with open("friends.csv","r") as f:
        for line in f:
            name, place = line.strip().split(",")
            if name == "NAME": # ignoring heading
                continue
            friends.append({"name": name, "place": place})
    
    for friend in sorted(friends,key=lambda x: x["name"]):
        print(friend)

# Best way to read a csv file
def csv_reader():
    friends = []
    with open("friends.csv","r") as f:
        reader = csv.DictReader(f)

        for row in reader:
            friends.append({"name": row["NAME"], "place": row["PLACE"]})

        for friend in sorted(friends,key=lambda x: x["name"]):
            print(friend)


#write_names()
#read_names()
#read_friends()

#sort_friends()
#print(sorted(["Kumar","Jegan","Alex"]))

#csv_reader()
create_csv()