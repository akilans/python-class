import re

name = input("What is your name? ").strip()

# Subramanian, Akilan | Subramanian,Akilan
# matches = re.search(r"^.+, .+$", name)
# output <re.Match object; span=(0, 19), match='Subramanian, Akilan'>

# get fname and lname provide ()
matches = re.search(r"^(.+), ?(.+)$", name)

if matches:
    # print(matches)
    lname, fname = matches.groups()
    name = f"{fname} {lname}"
else:
    print("Gave correct format")


print(f"Hello, {name}")

# Get username from twitter URL

url = "https://twitter.com/akilan468"
# url = "https://www.twitter.com/akilan468"
# (?:) - ignore group value
matches = re.search(
    r"^(?:https?://)?(?:www\.)?twitter\.com/([a-zA-Z0-9_]+)", url)

if matches:
    print(matches)
    username = matches.group(1)
    print(f"username is {username}")
else:
    print("URL is not valid")
