from utils.screens import *
from utils.tools import *
from utils.seconds_screens import *
from utils.create_registers import *
from utils.read_registers import *
from utils.update_register import *
from utils.delete_registers import *



def run ():

    clean_screen()
    welcome_screen()
    wait(2)

    while True:

        clean_screen()
        choice_main_menu = main_screen()

        if choice_main_menu == "1":
            while True:
                clean_screen()
                question = input("Do yo want to creat a new register? (Y/N): ").lower()
                
                if question == 'y':
                    registers = read_csv()
                    client_data = pre_register(registers)

                    if client_data is not None:
                        _csv_file_path = './documents/registers.csv'
                        create_client(_csv_file_path, client_data)
                        input('\n'+'Press -Enter key- to continue:')
                
                elif question == 'n' or question == 'no':
                    break

                else:
                    input('Invalid input! press -Enter key- to continue: ')

        elif choice_main_menu == "2":
            while True:
                clean_screen()
                choice = registers_screen()

                if choice == "1":
                    clean_screen()
                    search_register(read_csv())

                elif choice == "2":
                    clean_screen()
                    registers = read_csv()                    
                    show_registers(registers)
                    
                    input("Press Enter key for return: ")

                elif choice == "3":
                    break

                else:
                    input('\n'+'Invalid input! press -Enter key- to continue: ')
                    
        elif choice_main_menu == "3":
            while True:
                clean_screen()
                choice = update_screen()

                if choice == '1':
                    clean_screen()
                    method_of_search = search_screen()
                    while True:
                        if method_of_search == '1':
                            clean_screen()
                            registers = read_csv()
                            name_to_search = input('Enter the name of the company you want to update: ')
                            client_dict, idx = search_exact_by_name(registers, name_to_search)

                            if client_dict is not None:
                                full_update(registers, idx)
                                break

                            else:
                                input(f'\n{name_to_search} does not exit! Press -Enter key- to continue: ')
                                break

                        elif method_of_search == '2':
                            clean_screen()
                            registers = read_csv()
                            name_to_search = input('Enter the ID number of the company you want to update: ')
                            client_dict, idx = search_exact_by_id(registers, name_to_search)

                            if client_dict is not None:
                                full_update(registers, idx)
                                break

                            else:
                                input(f'\n{name_to_search} does not exit! Press -Enter key- to continue: ')
                                break

                        elif method_of_search == '3':
                            break

                        else:
                            input('\n'+'Invalid input! press -Enter key- to continue: ')

                elif choice == '2':
                    clean_screen()
                    method_of_search = search_screen()
                    while True:
                        if method_of_search == '1':
                            registers = read_csv()
                            name_to_search = input('\nEnter the name of the company you want to update: ')
                            client_dict, idx = search_exact_by_name(registers, name_to_search)

                            if client_dict is not None:
                                simple_update(registers, idx)
                                break

                            else:
                                input(f'\n{name_to_search} does not exit! Press -Enter key- to continue: ')
                                break

                        elif method_of_search == '2':
                            registers = [client.copy() for client in read_csv()]
                            name_to_search = input('\nEnter the ID number of the company you want to update: ')
                            client_dict, idx = search_exact_by_id(registers, name_to_search)

                            if client_dict is not None:
                                simple_update(registers, idx)
                                break

                            else:
                                input(f'\n{name_to_search} does not exit! Press -Enter key- to continue: ')
                                break

                        elif method_of_search == '3':
                            break

                        else:
                            input('\n'+'Invalid input! press -Enter key- to continue: ')

                elif choice == '3':
                    break

                else:
                    input('\n'+'Invalid input! press -Enter key- to continue: ')

        elif choice_main_menu == "4":
            while True:
                clean_screen()
                choice = delete_screen()

                if choice == '1':
                    while True:
                        clean_screen()
                        method_of_search = search_screen()

                        if method_of_search == '1':
                            clean_screen()
                            registers = read_csv()
                            name_to_search = input('Enter the name of the company you want to delete: ')
                            client_dict, idx = search_exact_by_name(registers, name_to_search)
                            
                            if client_dict is not None:
                                delete_register(registers, idx)

                            else:
                                input(f'\n{name_to_search} does not exit! Press -Enter key- to continue: ')
                            

                        elif method_of_search == '2':
                            clean_screen()
                            registers = read_csv()
                            uid_to_search = input('Enter the ID number of the company you want to delete: ')
                            client_dict, idx = search_exact_by_id(registers, uid_to_search)
                            
                            if client_dict is not None:
                                delete_register(registers, idx)

                            else:
                                input(f'\n{name_to_search} does not exit! Press -Enter key- to continue: ')

                        elif method_of_search == '3':
                            break

                        else:
                            input('\n'+'Invalid input! press -Enter key- to continue: ')

                elif choice == '2':
                    clean_screen()
                    delete_all_registers()

                elif choice == '3':
                    break

                else:
                    input('\n'+'Invalid input! press -Enter key- to continue: ')

        elif choice_main_menu.lower() == "exit":
            clean_screen()
            print("Session ended, good bye")
            wait(2)
            clean_screen()
            break

        else:
            print("\n"+"Invalid input")
            wait(1)


if __name__ == "__main__":
    run()