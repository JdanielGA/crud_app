import csv
from utils.tools import show_one_register, clean_screen
from utils.seconds_screens import search_screen


def read_csv(_file_path="./documents/registers.csv"):

    with open(_file_path, mode="r", encoding="utf-8") as csv_file:
        registers = list(csv.DictReader(csv_file))
        return registers


def search_by_name(registers):
    
    clean_screen()
    name_to_search = input("Type the organization name: ")

    filtered_list = list(filter(lambda organization: name_to_search.lower() in organization["Organization name"].lower(), registers))
    
    if filtered_list:
        client_dict = filtered_list[0]
        idx = registers.index(client_dict)
        return client_dict, idx
    
    else:
        client_dict = None
        idx = None
        return client_dict, idx


def search_by_id(registers):
    
    clean_screen()
    id_to_search = input("Type the ID number: ")

    filtered_list = list(filter(lambda id_number: id_to_search in id_number["ID Number"], registers))

    if filtered_list:
        client_dict = filtered_list[0]
        idx = registers.index(client_dict)
        return client_dict, idx
    
    else:
        client_dict = None
        idx = None
        return client_dict, idx


def search_register(registers):

    while True:

        clean_screen()
        choice = search_screen()

        if choice == '1':
            client, idx = search_by_name(registers)

            if client == None:
                print("\n"+"The register entered has not been created yet!"+"\n")
            
            elif client is not None:
                show_one_register(client)

            new_search = input('Do you want to do another search? (Y/N): ').lower()
            
            if new_search == 'n' or new_search =='no':
                break

        elif choice == '2':
            client, idx = search_by_id(registers)

            if client == None:
                print("\n"+"The register entered has not been created yet!"+"\n")
            
            elif client is not None:
                show_one_register(client)

            new_search = input('Do you want to do another search? (Y/N): ')

            if new_search == 'n' or new_search =='no':
                break
        
        elif choice == '3':
            break

        else:
            print('Wrong input value! Pleas, choose a valid option')