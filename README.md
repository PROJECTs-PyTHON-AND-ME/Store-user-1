# Inventory User History 1,

## Description .
This Python script allows you to add a product to the inventory.
It asks the user to enter the product name, price and quantity, validates the entries to ensure they are correct.
Calculates the total cost and displays the results in the console.

## Requirements.
- Python 3 installed on the system.

## Usage.
1. Run the script `inventory_h1.py` in a Python environment.
2. Follow th on-screen instructions to enter:
    - Product name:
    - Product price:
    - Product quantity:
3. The script will calculate the total cost (price * quantity) and dispaly the product information.

## Example of Execution.

```
Enter the product name: Apple
Enter the product price: 2.50
Enter the product quantity: 10
Product: Apple | Price: 2.50 | Quantity: 10 | Total: 25.00
```

## Validations.
- The name cannot be empty or consist of numbers.
- The price must be a positive number with decimals.
- The quantity must be a positive integer.

## Notes.
- The script uses a loop to validates each entry until it is correct.
- The results are dispalyed in a formatted manner in the console.