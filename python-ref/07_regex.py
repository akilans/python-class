import re
# + - 1 or more
# * - 0 or more
# ^ - Starts with
# $ - Ends with
# [] - Allowed characters
# [^] - Not Allowed Characters
# ? - 0 or 1 character - Optional
# () - group of characters
# (?: - ignore matches from the list of returned values

# Validate email
def validate_email():
    email = input("Enter email : ")

    # Before @ alphanumeric _ and . allowed
    # After @ 
    matches = re.search(r"^[a-zA-Z0-9\.]+@+[a-zA-Z0-9]+\.+[a-zA-Z]{2,10}$",email)

    if matches:
        print("Valid Email")
    else:
        print("Invalid Email")

# validate string & get matching values
# possible inputs 
# - Akilan Subramanian
# - Subramanian, Akilan
# - Subramanian,Akilan     
def validate_string():
    full_name = input("Enter your full name: ")
    matches = re.search(r"^([a-zA-Z]+),+ ?([a-zA-Z]+)$",full_name)
    if matches:
        print("Provides in Lastname, Firstname format")
        print(f"Fullname - {matches[2]} {matches[1]}")
    else:
        print(f"Fullname - {full_name}")

# Validate url
# Parse only username from twitter url
# Possible inputs
# - https://twitter.com/Akilan468
# - https://www.twitter.com/Akilan468
# - http://twitter.com/Akilan468
# - http://www.twitter.com/Akilan468
# - twitter.com/Akilan468
def validate_url():
    url = input("Enter your twitter URL: ")
    matches = re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(.+)$",url)
    if matches:
        print("Valid URL")
        print(f"Twitter Username - {matches[1]}")
    else:
        print("Invalid URL")


# main function to call all validators
def main():
    #validate_email()
    #validate_string()
    validate_url()

# call main function
if __name__ == "__main__":
    main()








# Validate url