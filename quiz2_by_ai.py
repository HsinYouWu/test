# pe2.py
# Taiwan Team Ticket Discount and Cheer Code

# (1) Ask user to enter the ticket amount
amount = float(input("Enter the ticket amount: "))

# (2) Ask user to enter the membership level
level = input("Enter the membership level (General or Premium): ")

# (3) Ask user to enter the supporter code
supporter_code = input("Enter the supporter code: ")

# (4) Use while loop and string indexing to build the cheer code
#     Copy every character except '-'
cheer_code = ""
i = 0
while i < len(supporter_code):
    if supporter_code[i] != "-":
        cheer_code = cheer_code + supporter_code[i]
    i = i + 1

# (5) Check whether the membership level is valid
if level != "General" and level != "Premium":
    print("Invalid membership level. Please enter 'General' or 'Premium'.")
else:
    # (6) Calculate the final amount based on membership level and ticket amount
    if level == "General":
        if amount > 6000:
            final_amount = amount * 0.85
        elif amount > 4000:
            final_amount = amount * 0.90
        elif amount > 2000:
            final_amount = amount * 0.95
        else:
            final_amount = amount

    elif level == "Premium":
        if amount > 6000:
            final_amount = amount * 0.80
        elif amount > 4000:
            final_amount = amount * 0.85
        elif amount > 2000:
            final_amount = amount * 0.90
        else:
            final_amount = amount

    # (7) Output the membership level and final amount payable
    print(level + " $" + str(final_amount))

    # (8) Output the cheer code
    print("Cheer code: " + cheer_code)