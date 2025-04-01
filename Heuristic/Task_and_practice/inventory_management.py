title = "Welcome to the Inventory Management System by Aniket Maurya"
print(title.center(100))

print("-"*(100))

inventory = { 
    "product_id" : [],
    "product_name" : [],
    "price" : [],
    "stock" : []
}

while True:
    print("\n1.Add a product\n2. Update the existing product\n3. Remove the existing product\n4. Display the whole inventory ")
    choice = int(input("Enter inventory action: "))
    if choice != choice:
        break
    if choice == 1:
        p_id = int(input("Enter the product ID: "))

        for product_id, entry in inventory.items():
            if p_id in entry:
                print("The following product ID already exist.\n Please create a unique product ID.")
                break
            else:
                if p_id not in entry:
                   product_name = str(input("Enter the Product: ")) 
                   price = float(input("Enter the Product prize: "))
                   stock = int(input("Enter the Product stock: "))
                   inventory["product_id"].append(p_id)
                   inventory["product_name"].append(product_name)
                   inventory["price"].append(price)
                   inventory["stock"].append(stock)
                   print(f"Product_ID: {p_id} ")
                   print(f"Product_name: {product_name}")
                   print(f"Price: {price}" )
                break

    elif choice == 2:
        update_product = int(input("Enter the Product ID to update: "))
        print(f"{inventory}")
        for product_id, entry in inventory.items():
            if update_product not in entry:
                print("Product ID doesn't exist in database.")
            else:
                if update_product in entry:
                    product_name = str(input("Enter the Product: ")) 
                    price = float(input("Enter the Product prize: "))
                    stock = int(input("Enter the Product stock: "))
                    inventory["product_id"].append(p_id)
                    inventory["product_name"].append(product_name)
                    inventory["price"].append(price)
                    inventory["stock"].append(stock)
                    print(f"Product_ID: {p_id} ")
                    print(f"Product_name: {product_name}")
                    print(f"Price: {price}" )
                    break

    elif choice ==3:
        rem_id = int(input("Enter the Product Id which you want to remove from inventory: "))
        if rem_id != p_id:
            print("This product ID doesn't exist in inventory.")
            break
        else:
            print(f"{inventory}")
            if rem_id == p_id:
                for p_id, entry in inventory.items():
                    print(f"{p_id} : {product_name}")
                    inventory["product_name"].remove(product_name)
                    inventory["price"].remove(price)
                    inventory["stock"].remove(stock)
                    print(f"{inventory}")
                    break

    elif choice == 4:
            print("Do you want to print the inventory (yes/no)? ")
            chahie = input("Yes/No?:  ")
            print("Here'a ur inventory")
            if chahie == "yes":
                print(f"{inventory}")
                break 
            else:
                print("Did u miss soemthing?")
                break 
        

