email = input("Enter your Email: ")
k, j, d = 0, 0, 0  # Flags initialized for space, uppercase, invalid character

if len(email) >= 6:  # Step 1: Email must be at least 6 characters long
    if email[0].isalpha():  # Step 2: First character must be an alphabet
        if ("@" in email) and email.count('@') == 1:  # Step 3: Must contain exactly one '@'
            if email.index(".") > email.index("@"):  # Step 4: Period must come after '@'
                for i in email:  # Step 5: Iterate through each character
                    if i.isspace():  # Step 6: Check for spaces
                        k = 1
                    elif i.isalpha():  # Step 7: Check if character is an alphabet
                        if i.isupper():  # Step 8: Check for uppercase letters
                            j = 1
                    elif i.isdigit():  # Step 9: Allow digits
                        continue
                    elif i in ["_", "-", ".", "@"]:  # Step 10: Allow certain special characters
                        continue
                    else:  # Step 11: Set flag if any other invalid character is found
                        d = 1

                # Step 12: Final validation based on flags
                if k == 1 or j == 1 or d == 1:
                    print("Wrong Email")
                else:
                    print("Right Email")
            else:
                print("Wrong Email: Invalid domain format")
        else:
            print("Wrong Email: Invalid or missing '@'")
    else:
        print("Wrong Email: First character should be an alphabet")
else:
    print("Wrong Email: Too short")
