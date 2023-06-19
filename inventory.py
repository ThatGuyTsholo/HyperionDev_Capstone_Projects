from tabulate import tabulate

# Create a class called "Shoes"
class Shoes:
    # Initialize the class above with the given values
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # Define a method called "get_cost"
    def get_cost(self):
        return self.get_cost()
    
    # Define a method called "get_quanty"
    def get_quanty(self):
        return self.quanty
        
    # Define a method called "__str__"
    def __str__(self):
        return f"{self.country} - {self.product} ({self.code}): {self.quantity} available at {self.cost} each"
    
while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    menu = input('''Select one of the following Options below:
r - Read shoe list
c - Capture new shoes
va - View all shoes
re - Restock shoe list
s - Search shoe
v - Value per shoe
h - Highest quantity shoe
e - Exit
: ''').lower()
    

    shoes_list = []

    # Create an empty list "shoes_list"
    if menu == "r":
        def read_shoes_data():
            # Create a list to store each shoe detail in 
            shoes_list = []
            # Split the line into multiple parts
            try:
                with open("inventory.txt", "r") as inventory:
                    for line in inventory:
                        data = line.strip().split(",")
                        country = data[0]
                        code = data[1]
                        product = data[2]
                        cost = data[3]
                        quantity = data[4]
                        shoes_list.append(Shoes(country, code, product, cost, quantity))
                    for shoes in shoes_list:
                        print(shoes)
            except Exception as e:
                print(f"Error: {e}")
        print(read_shoes_data())
        
    elif menu == "c":
        def capture_shoes():
            try:
                # Ask the user to enter information about the shoe they want to enter
                print("Please enter the details of the new shoe.")
                country = input("Please enter the country the shoe originates from: ")
                code = input("Please enter the shoe's code: ")
                product = input("Please enter the shoe's name: ")
                cost = float(input("Please enter the price of the shoe: "))
                quantity = int(input("Please enter the amount of shoes you would like to enter into the system: "))

                # Add the new shoe information to the shoes list
                shoes_list.append((country, code, product, cost, quantity))

                # Add the new shoe information to "inventory.txt"
                with open("inventory.txt", "a") as inventory:
                    inventory.write(f"{country},{code},{product},{cost},{quantity}\n")
                print("New shoe details added successfully!")
            except ValueError:
                print("Error: Invalid input format. Please try again.")
        print(capture_shoes())
        
    elif menu == "va":
        # Create a function called "view_all()"
        def view_all():
            try:
                # Open and read from "inventory.txt"
                with open("inventory.txt") as file:
                    # Strip each line into different parts
                    data = [line.strip().split(",") for line in file.readlines()]
                    # Present the data in a table
                print(tabulate(data, headers=["Country", "Code", "Product", "Cost", "Quantity"], tablefmt="fancy_grid"))
            except:
                print("Error: Failed to read shoe details from inventory.txt file.")
        print(view_all())

    elif menu == "re":
        def re_stock():
            
            min_product = None
            min_quantity = float('inf')

            with open("inventory.txt") as inventory:
                header = inventory.readline()               
                for line in inventory:
                    columns = line.strip().split(",")
                    product = columns[2]
                    quantity = float(columns[4])
                    if quantity < min_quantity:
                        min_quantity = quantity
                        min_product = product
            print(f"The shoe with smallest quantity is: {min_product} - {min_quantity}")

            print(f"The product with the lowest quantity is {min_product}.")
            restock = input(f"Do you want to restock {min_product}? (y/n): ")
            if restock.lower() == 'y':
                new_quantity = int(input(f"What is the new quantity of {min_product}? "))
                with open("inventory.txt", "r") as inventory:
                    lines = inventory.readlines()
                    
                with open("inventory.txt", "w") as inventory:
                    inventory.write(header)
                    for line in lines[1:]:
                        columns = line.strip().split(",")
                        if columns[2] == min_product:
                            columns[4] = str(new_quantity)
                            line = ",".join(columns) + "\n"
                        inventory.write(line)
                        
                return f"{min_product} has been restocked to {new_quantity}."
            else:
                return f"No products were restocked."
        print(re_stock())


    elif menu == "s":   
        code = input("Please enter the code of the shoe that you are looking for: ")
        def search_shoe(code):
            with open("inventory.txt") as inventory:
                header = inventory.readline()
                for line in inventory:
                    columns = line.strip().split(",")
                    if columns[1] == code:
                        return {
                            "product": columns[2],
                            "country": columns[0],
                            "code": columns[1],
                            "cost": columns[3],
                            "quantity": columns[4]}
                return "Shoe not found"
        print(search_shoe(code))

    elif menu == "v":
        def value_per_item():
            with open("inventory.txt") as inventory:                        
                        header = inventory.readline()
                        for line in inventory:
                            columns = line.strip().split(",")
                            product = columns[2]
                            cost = float(columns[3])
                            quantity = int(columns[4])
                            value = cost * quantity
                            print(f"{product}: R{value}")
        print(value_per_item())

        
    elif menu == "h":
        def highest_qty():
            max_product = None
            max_quantity = float('-inf')

            with open("inventory.txt") as inventory:
                header = inventory.readline()               
                for line in inventory:
                    columns = line.strip().split(",")
                    product = columns[2]
                    quantity = int(columns[4])
                    if quantity > max_quantity:
                        max_quantity = quantity
                        max_product = product

            if max_product is not None:
                print(f"The shoe with the highest quantity is: {max_product} - {max_quantity} available for sale.")
        print(highest_qty())
    
    elif menu == "e":
        exit()
