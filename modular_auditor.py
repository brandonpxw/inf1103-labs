def get_valid_input():
    user_input = input("Enter the stock quantity (or type 'quit' to exit): ")
    if user_input.isdigit():
        if int(user_input) > 500:
            print("Warning: Stock quantity exceeds 500!")
        elif int(user_input) > 0:
            return int(user_input)
    elif user_input.lower() == "quit":
        return "quit"
    else:
        print("Invalid input. Please enter a number or 'quit'.")
        return None

def process_delivery(current_total, new_value):
    return current_total + new_value

def calculate_tax(amount):
    tax_rate = 0.10
    return amount * tax_rate

def generate_report(total_units, failed_attempts):
    """Prints the final summary report."""
    print("\n----- Delivery Report -----")
    print("Total Units Processed:", total_units)
    print("Failed/Rejected Entries:", failed_attempts)
    print("----------------------------")

def main():
    total_inventory = 0
    failed_entries = 0
    total_tax = 0.0

    while True:
        result = get_valid_input()

        if result == "quit":
            break
        elif result is None:
            failed_entries += 1
        else:
            total_inventory = process_delivery(total_inventory, result)
            delivery_tax = calculate_tax(result)
            total_tax += delivery_tax
            print(f"Processed: {result} units | Delivery Tax: ${delivery_tax:.2f} | Running Total: {total_inventory}")

    generate_report(total_inventory, failed_entries)


main()