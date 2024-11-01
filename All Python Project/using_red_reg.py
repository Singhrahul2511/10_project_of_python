import re
def validate_email(emails):
    email_reg = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'


    if(re.match(email_reg, emails)):
        return True
    else:
        return False
    

emails = input("Enter Email: ")

if validate_email(emails):
    print(f"{emails} is valid: ")
else:
    print(f"{emails} is invalid: ")