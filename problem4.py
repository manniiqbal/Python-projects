# these are a few sample items for the inventory.
inventory = {
    "Summer Dress": {"quantity": 15, "price": 49.99},
    "Denim Jeans": {"quantity": 25, "price": 39.99},
    "Floral Blouse": {"quantity": 20, "price": 29.99}
}

# this is a while loop which will display the menu showing all the available options.
while True:
    # The display menu will display all the different choices.
    print("\n Sophie's Boutique Inventory System ") 
    print("1. Add Item")
    print("2. Update Item")
    print("3. Remove Item")
    print("4. Display Inventory")
    print("5. Calculate Total Value")
    print("6. Exit")
    
    choice = input("\nEnter your choice (1-6): ") # the variable choice will take one of the above 6 options from the user.
    
    # Shows what 
    if choice == '1':   # shows what will happen if the user selects 1 as their choice.
        name = input("Enter item name: ") # name is the variable for the new item being added to the inventory management system.
        if name in inventory:   
            print("Item already exists! Use update option instead.") # lines 24-25 explain what will happen if the user enters a pre-existing item
        else: 
            try:
                quantity = int(input("Enter quantity: ")) # Will add the quantity of that item is integer because can only have whole number of items.
                price = float(input("Enter price: £"))    # Will add price and price is in float as can have float prices.
                if quantity < 0 or price < 0:             # Evaluates that the numbers are positive.
                    print("Quantity and price must be positive numbers!") # Shows the user that they should enter positive numbers.
                else:
                    inventory[name] = {"quantity": quantity, "price": price}   # This will add the item along with its price and quantity to the inventory.
                    print(f"{name} has been added to inventory.")              # This will display the item being added to the inventory.
            except ValueError:                                                 # This will allow the user to retry if they do not choose a number between the range 1-6.
                print("Please enter valid numbers!")                           
    
    # This block of code shows what will happen if the user picks option 2.
    elif choice == '2': #checks if the user selected option 2
        name = input("Enter item name to update: ") # Asks the user to enter the name of the item they wish to update and assigns it to the variable name.
        if name not in inventory:                   # Checks if the item is in the inventory.
            print("Item not found in inventory!")   # If item isnt in the inventory then this message will be displayed.
        else:                                       # If the item is found then it will carry onto the rest of the code.
            try:                                    # This will handle any errors that arise.
                quantity = int(input("Enter new quantity: ")) # Asks the user to input the new quantity of the item and is integer as cannot have half of an item.
                price = float(input("Enter new price: £"))    # Asks the user to input the new price of the item and is a float as prices can be decimals.
                if quantity < 0 or price < 0:  # Ensures that the the number entered for the quantity and price are positive.
                    print("Quantity and price must be positive numbers!") # If they are not positive an error message is displayed telling the user to enter positive numbers.
                else: # Shows what will happen if the numbers entered are positive.
                    inventory[name] = {"quantity": quantity, "price": price} # Will update the item's price and quantity to what the user entered. 
                    print(f"{name} has been updated.") # prints a message showing that the item has been updated.
            except ValueError:  #Handles any input errors.
                print("Please enter valid numbers!") # Displays an error message if there is any error.
    
    # This block of code shows what will happen if the user picks option 3.
    elif choice == '3': # Checks if the user picked option 3
        name = input("Enter item name to remove: ") # Will assign the item the user wants to remove to the variable name.
        if name not in inventory:                   # This checks if the item is in the inventory.
            print("Item not found in inventory!")   # If the item isnt in the inventory this will print a message showing this.
        else:
            del inventory[name]                     # Will delete the item from the inventory if is in the inventory.
            print(f"{name} has been removed from inventory.") # Will print a message explaining to the user that the item has been removed from the inventory.
    
    # This block of code shows what will happen if the user picks option 4.
    elif choice == '4': # Checks if the user selected option 4.
        print("\nCurrent Inventory:")  #will print all the items in the inventory.
        print("Item Name , Quantity, Price") # will print the names of different items along with their prices.
        print("-" * 40) # This will visually seperate the individual items in the inventory by 40 characters.
        for item, details in inventory.items():  # Item will assign to the individual items in the dictionary and details will be the dictionary.
            print(f"{item} , {details['quantity']} , £{details['price']}") #Will print each individual item in the inventory with its quantity and price.
    
    # This block of code shows what will happen if the user selects option 5.
    elif choice == '5':
        total = 0            #starts the the total at 0.
        for item in inventory.values():  # will iterate over the values in inventory.
            total += item['quantity'] * item['price']  #Will give us the total for each specific item and will keep going for each item in the inventory.
        print(f"\nTotal Inventory Value: £{total}")  # Will display the total price for all the items in the inventory.
    
    # This block of code shows what will happen if the user selects option 6.
    elif choice == '6': # What will happen if the user selects option 6.
        print("Thank you for using the inventory system!") # Displays a thank you message for using the inventory
        break                                              # Will exit the loop.
    
    # What will happen if the user picks a number which isnt 1-6.
    else:
        print("Invalid choice! Please enter a number between 1 and 6.") # Will display a message telling the user to select a number between 1 and 6.
