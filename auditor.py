inventory = 0
count = ""
failedEntries = 0

while count != "quit":
    count = input("Enter the stock quantity (or type 'quit' to exit): ")
    
    if count.isdigit() and int(count) > 0:
        if int(count) > 500:
            print("Warning: Stock quantity exceeds 500!")
        else:
            inventory += int(count)
    elif count.lower() == "quit":
        print("Total Units Processed:", inventory)
        print("Failed Entries:", failedEntries)
    else:
        failedEntries += 1
        print("Invalid input. Please enter a number or 'quit'.")

