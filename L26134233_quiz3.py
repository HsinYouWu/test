# Welcome!
print("Welcome to the SpaceX Rocket Fueling Cost Estimator!")

ans = "yes" # Always yes in the begining

while ans == "yes":
    # Input current percentage and target percentage
    current_percent = float(input("\nEnter current fuel percentage (0-100): "))
    target_percent = float(input("Enter target fuel percentage (0-100): "))

    # Target percentage should be greater than current percentage
    while current_percent >= target_percent:
        print("Target percentage must be greater than current percentage.")
        current_percent = float(input("\nEnter current fuel percentage (0-100): "))
        target_percent = float(input("Enter target fuel percentage (0-100): "))

    # Select fueling mode
    print("\nSelect a fueling mode:")
    print("1. Standard Ground Fueling")
    print("2. Rapid Launch Fueling")
    print("3. Cryogenic Precision Fueling")
    choice = input("Enter your choice (1-3): ")
    # Connect number and correspond fueling mode
    fueling_mode = ["", "Standard Ground Fueling", "Rapid Launch Fueling", "Cryogenic Precision Fueling"]

    # Each mode cost and efficiency
    if choice == "1":
        cost_per_ton = 18; efficiency = 0.95
    elif choice == "2":
        cost_per_ton = 25; efficiency = 0.90
    elif choice == "3":
        cost_per_ton = 30; efficiency = 0.92

    # Calculate by formula
    required_fuel = (target_percent - current_percent)/100*1200 / efficiency
    total_cost = required_fuel * cost_per_ton

    # Output
    print("\n--- Fueling Summary ---")
    print(f"Fueling Mode: {fueling_mode[int(choice)]}")
    print(f"Estimated Fuel Required: {required_fuel:.2f} tons")
    print(f"Estimate Fueling Cost: ${total_cost:.2f}")
    
    # Warning
    if choice == "2" and required_fuel > 500:
        print("Warning: Large rapid fueling operation detected.")

    # If user want to estimate again, input ans = "yes" to restart the while
    # If user doesn't want to estimate again, input ans = "no" (actually only except "yes") to close the while
    ans = input("\nWould you like to estimate another fueling session? (yes/no): ")

# Thank you!
print("Thank you for using the SpaceX Rocket Fueling Cost Estimator!\n")