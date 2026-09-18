
def get_valid_input():
    inventory = 0
    count = ""
    failedEntries = 0
    while True:
        count = input("Enter the stock quantity (or type 'quit' to exit): ")
        
        if count.isdigit() and int(count) > 0:
            if int(count) > 500:
                print("Warning: Stock quantity exceeds 500!")
            else:
                inventory += int(count)
                print("Total Units Processed:", inventory)
        elif count.lower() == "quit":
            print("Total Deliveries Processed:", inventory)
            print("Failed/Rejected Entries:", failedEntries)
            break
        else:
            failedEntries += 1
            print("Invalid input. Please enter a number or 'quit'.")
    return inventory, failedEntries


def process_delivery(current_total, new_value):
    return current_total + new_value

def calculate_tax(amount):
    tax_rate = 0.10
    return amount * tax_rate

def generate_report(total_units, failed_entries):
    print("----- Delivery Report -----")
    print("Total Units Processed:", total_units)
    print("Failed/Rejected Entries:", failed_entries)
    print("----------------------------")

def main():
    total_units, failed_entries = get_valid_input()
    process_delivery(total_units, 0)  # Assuming no new deliveries to process in this context
    calculate_tax(total_units)  # Assuming tax calculation is needed for the total units
    generate_report(total_units, failed_entries)   

main()