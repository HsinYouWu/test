# Input
ticket_amount = float(input("Enter the ticket amont: "))
membership_level = str(input("Enter the membership level (General or Premium): "))
supperter_code = str(input("Enter the supporter code: "))

# Check membership level either "General" or "Premium"
while membership_level != "General" and membership_level != "Premium":
    print("Invalid membership level. Please enter 'General' or 'Premium'.\n")
    exit()

# Discount rules
# 1: Membership level, 2: Discount for purchases
if membership_level == "General":
    if 2000 < ticket_amount <= 4000:
        ticket_amount *= 0.95
    elif 4000 < ticket_amount <= 6000:
        ticket_amount *= 0.90
    elif 6000 < ticket_amount:
        ticket_amount *= 0.85
    else:
        pass

if membership_level == "Premium":
    if 2000 < ticket_amount <= 4000:
        ticket_amount *= 0.90
    elif 4000 < ticket_amount <= 6000:
        ticket_amount *= 0.85
    elif 6000 < ticket_amount:
        ticket_amount *= 0.80
    else:
        pass

# Get rid of "-"
supperter_code = supperter_code.replace("-", "")

# Output
print(f"{membership_level} ${ticket_amount}")
print(f"Cheer code: {supperter_code}\n")