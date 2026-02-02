# Initial Flow Chart.
# Data Entry (Variable in Python).

while True: # Loop to validate the name of the product to be added.
    name = input("Enter the name of the product: ").strip() # Strip = Remove leading and trailing spaces.
    if not name:
        print("The name cannot be empty. Please try again.")
        continue
    if name.isdigit(): # Isdigit = Check that the characters in a string are digits.
        print("The name cannot be a number. Please try again.")
        continue
    break

while True: # Loop to validate th price of the added product.
    price_str = input("Enter the price of the product: ").strip()
    if price_str == "":
        print("The price cannot be empty. Please try again.")
        continue
    try:
        price = float(price_str)
    except ValueError:
        print("Invalid value. Please enter a number for the price.")
        continue
    if price < 0:
        print("The price cannot be negative. Please try again.")
        continue
    break

while True: # Loop to validate the quantity of the added product.
    quantity_str = input("Enter the quantity of the product: ").strip()
    if quantity_str == "":
        print("The quantity cannot be empty. Please try again.")
        continue
    try:
        quantity = int(quantity_str)
    except ValueError:
        print("Invalid value. Please enter an integer for the quantity.")
        continue
    if quantity < 0:
        print("The quantity cannot be negative. Please try again.")
        continue
    break

# Mathematical operation (total_cost).
total_cost = price * quantity # Calculation of total cost using the function (price * quantity).

# Display results in console.
print(f"Product: {name} | Price: {price:,.2f} | Quantity: {quantity} | Total Cost: {total_cost:,.2f}")