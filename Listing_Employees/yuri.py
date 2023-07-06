from creates import creates
from listings import listings
from menu import menu
from updates import updates

# Log-in
print("========== Enter your access credentials ==========")
rut = input("RUT: ")
validate_rut = menu.check_rut_exists(rut)
if validate_rut == (1,):
    password_attempts = 3
    while password_attempts > 0:
        password = input("Password: ")

        # Validate password
        validate_password = (menu.confirm_pswrd(rut))
        if validate_password == password:

        # Access to menu
            print("--------Access approved!--------")

        # Validate Position
            position = (menu.set_position(rut))

        # Manager Menu
            if position == "manager":
                menu.show_manager_menu()
                option = int(input())
                while option != '4':
                    option = input("Enter an option: ")
                    if option == '1':
                        print("List employees...")
                        listings.see_list_employees()
                    elif option == '2':
                        print("Manage employees...")
                        rut_modify = input("Enter the employee rut you want to modify")
                        print("What do you want to change about the employee?")
                        menu.modify_employee()
                        while opt != '5':
                            opt = input("Enter an option: ")
                            if opt == '1':
                                salary = input("Enter the new salary")
                                updates.update_employee_salary(salary, rut_modify)
                            elif opt == '2':
                                position = input("Enter the new position")
                                updates.update_employee_position(position, rut_modify)
                            elif opt == '3':
                                area = input("Enter the new area")
                                updates.update_employee_area(area, rut_modify)
                            elif opt == '4':
                                area = input("Enter the new area")
                                updates.update_employee_area(area, rut_modify)
                            elif opt == '5':
                                print("Exit...")
                            else:
                                print("Invalid option")
                    elif option == '3':
                        print("My personal data...")
                        menu.personal_data()
                        while opt != '3':
                            opt = input("Enter an option: ")
                            if opt == '1':
                                address = input("Enter the new address")
                                updates.update_employee_address(address, rut)
                            elif opt == '2':
                                phone = input("Enter the new phone")
                                updates.update_employee_phone(phone, rut)
                            elif opt == '3':
                                print("Exit...")
                            else:
                                print("Invalid option")
                    elif option == '4':
                        print("Exit...")
                    else:
                        print("Invalid option")

        # HH.RR Manager Menu
            elif position == "HHRR_manager":
                menu.show_HHRR_manager_menu()
                while option != '3':
                    option = input("Enter an option: ")
                    if option == '1':
                        print("According to what do you want to filter the employees?")
                        menu.filter()
                        while opt != '5':
                            opt = input("Enter an option: ")
                            if opt == '1':
                                menu.sex()
                                while opti != '2':
                                    opti = input("Enter an option: ")
                                    if opti == '1':
                                        print("list female employees")
                                        listings.list_female_employees()
                                    elif opti == '2':
                                        print("list male employees")
                                        listings.list_male_employees()
                                    elif opti == '3':
                                        print("Exit...")
                                    else:
                                        print("Invalid option")
                            elif opt == '2':
                                menu.position()
                                while opti != '5':
                                    opti = input("Enter an option: ")
                                    if opti == '1':
                                        print("listing managers")
                                        listings.list_manager()
                                    elif opti == '2':
                                        print("listing HH.RR Manager")
                                        listings.list_HHRR_manager()
                                    elif opti == '3':
                                        print("listing HH.RR")
                                        listings.list_HHRR()
                                    elif opti == '4':
                                        print("listing Workers")
                                        listings.list_worker()
                                    elif opti == '5':
                                        print("Exit...")
                                    else:
                                        print("Invalid option")
                            elif opt == '3':
                                menu.area()
                                while opti != '6':
                                    opti = input("Enter an option: ")
                                    if opti == '1':
                                        print("Listing the Reception and classification of packages")
                                        listings.list_RCP()
                                    elif opti == '2':
                                        print("listing the Customer Support")
                                        listings.list_CS()
                                    elif opti == '3':
                                        print("listing the Logistics and distribution")
                                        listings.list_LD()
                                    elif opti == '4':
                                        print("listing the Administrative and financial")
                                        listings.list_AF()
                                    elif opti == '5':
                                        print("listing the information technology")
                                        listings.list_IT()
                                    elif opti == '6':
                                        print("Exit...")
                                    else:
                                        print("Invalid option")
                            elif opt == '4':
                                menu.departament()
                                while opti != '6':
                                    opti = input("Enter an option: ")
                                    if opti == '1':
                                        print("Listing the Operations department")
                                        listings.list_RCP_D()
                                    elif opti == '2':
                                        print("listing the Customer Support department")
                                        listings.list_CS_D()
                                    elif opti == '3':
                                        print("listing the Logistics and distribution department")
                                        listings.list_LD_D()
                                    elif opti == '4':
                                        print("listing the Administrative and financial department")
                                        listings.list_AF_D()
                                    elif opti == '5':
                                        print("listing the information technology department")
                                        listings.list_IT_D()
                                    elif opti == '6':
                                        print("Exit...")
                                    else:
                                        print("Invalid option")
                            elif opt == '5':
                                print("Exit...")
                    elif option == '2':
                        print("My personal data...")
                        menu.personal_data()
                        while opt != '2':
                            opt = input("Enter an option: ")
                            if opt == '1':
                                address = input("Enter the new address")
                                updates.update_employee_address(address, rut)
                            elif opt == '2':
                                phone = input("Enter the new phone")
                                updates.update_employee_phone(phone, rut)
                            else:
                                print("Invalid option")
                    elif option == '3':
                        print("Exit...")
                    else:
                        print("Invalid option")

        # HH.RR Menu
            elif position == "HHRR":
                menu.show_HHRR_manager_menu()
                while option != '3':
                    option = input("Enter an option: ")
                    if option == '1':
                        print("New employee form...")
                        creates.create_new_employee(input("Name: "),input("Last name: "),input("Rut: "),input("Sex: "),input("Address: "),input("Phone: "),input("Date Entry: "),input("Area: "), input("Departament: "))
                        print("---------------------------------------------------------")
                        creates.create_emergency_contact(input("Name: "),input("Relationship: "),input("Phone: "), input("Rut employee: "))
                        print("---------------------------------------------------------")
                        Cf = input("Do you have a family burden? Y/N")
                        if Cf == "y" or "Y":
                            creates.create_family_burden(input("Name: "),input("Last name: "),input("Relationship: "),input("Phone: "), input("Rut employee: "))
                        print("---------------------------------------------------------")
                        creates.create_new_credentials(input("Name: "),input("Password: "),input("Rut employee"))
                        print("---------------------------------------------------------")
                        go_back = input("Press 'B' to go back to the main menu or any other key to continue: ")
                        
                        if go_back.lower() == 'b':
                            break
                    elif option == '2':
                        print("My personal data...")
                        menu.personal_data()
                        while opt != '2':
                            opt = input("Enter an option: ")
                            if opt == '1':
                                address = input("Enter the new address")
                                updates.update_employee_address(address, rut)
                            elif opt == '2':
                                phone = input("Enter the new phone")
                                updates.update_employee_phone(phone, rut)
                            else:
                                print("Invalid option")
                    elif option == '3':
                        print("Exit...")
                    else:
                        print("Invalid option")

        # Worker Menu
            elif position == "worker":
                menu.show_worker_menu()
                while option != '3':
                    option = input("Enter an option: ")
                    if option == '1':
                        print("Depending on what you want to filter your coworkers?")
                        menu.filter_worker()
                        while opt != '3':
                            opt = input("Enter an option: ")
                            if opt == '1':
                                menu.sex()
                                while opti != '2':
                                    opti = input("Enter an option: ")
                                    if opti == '1':
                                        print("list female employees")
                                        listings.list_female_employees()
                                    elif opti == '2':
                                        print("list male employees")
                                        listings.list_male_employees()
                                    elif opti == '3':
                                        print("Exit...")
                                    else:
                                        print("Invalid option")
                            elif opt == '2':  
                                print       
                    elif option == '2':
                        print("My personal data...")
                        menu.personal_data()
                        while opt != '2':
                            opt = input("Enter an option: ")
                            if opt == '1':
                                address = input("Enter the new address")
                                updates.update_employee_address(address, rut)
                            elif opt == '2':
                                phone = input("Enter the new phone")
                                updates.update_employee_phone(phone, rut)
                            else:
                                print("Invalid option")
                    elif option == '3':
                        print("Exit...")
                    else:
                        print("Invalid option")

        # No position
            else:
                print("You do not have any position in this company")

        # Invalid Password
        else:
            password_attempts -= 1
            print("Invalid password. Attempts remaining:", password_attempts)

    # Exceeded maximum
    else:
        print("Exceeded maximum password attempts. Access denied.")

# Invalid RUT
else:
    print("Invalid RUT. Access denied.")