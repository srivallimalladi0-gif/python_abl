
email = input("Enter student email: ")
reg_id = input("Enter registration ID: ")

# Email validation
if email.count("@") != 1:
    print("Invalid Email: Missing or extra @")
elif " " in email:
    print("Invalid Email: Spaces are not allowed")
elif "." not in email.split("@")[1]:
    print("Invalid Email: Missing domain extension")
elif email.startswith("@") or email.endswith("."):
    print("Invalid Email: Missing components")
else:
    print("Valid Email")

# Registration ID validation
if len(reg_id) != 10:
    print("Invalid Registration ID: Length must be 10")
else:
    valid = True

    for ch in reg_id:
        if not ch.isalnum():
            valid = False

    if valid:
        print("Valid Registration ID")
    else:
        print("Invalid Registration ID: Special characters found")

