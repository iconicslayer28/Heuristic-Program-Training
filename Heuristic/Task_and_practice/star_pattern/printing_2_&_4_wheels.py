# Problem statement = Print Two wheeler & Four wheeler vehicles as stars (*), in rows and columns format. 
# ( end=' '  ) this type of statement is used for spacing in between the stars.  

while True:
    print("Pick the type of vehicle you wanna choose:")
    print("\n1. Car. \n 2. Jeep.")
    
    choice_veh = int(input("Enter the type of vehicle you wanna choose:"))
    print("Pick the number of wheels you want:")
    print("\n1. Two Wheeler \n 2. Four wheeler")
    choice = int(input("Enter the Number of wheels:"))
    if choice_veh == 1:

        if choice == 1:
            import car
            import Two_Tyre
            break 
        elif choice == 2:
            import jeep
            import Two_Tyre
            break 
        else: 
            print("Invalid choice.")

    elif choice_veh == 2:
        if choice == 1:
            import car
            import Two_Tyre

        elif choice == 2:
            import jeep
            import Four_Tyre
        else: 
            print("Invalid choice.")


