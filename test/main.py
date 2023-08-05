from utils.registers import read_csv
from utils.seconds_screens import search_screen
    


def search_by_name(registers):
    
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


def show_registers(data):

    print(("-----"*20)+"\n")

    for key, value in data.items():
        print(f"{key}: {value}")

    print("\n"+('-----'*20)+"\n")


while True:

    registers = read_csv()
    choice = search_screen()


    if choice == '1':
        client, idx = search_by_name(registers)

        if client == None:
            print("\n"+"The register entered has not been created yet!"+"\n")
        
        elif client is not None:
            show_registers(client)

        new_search = input('Do you want to do another search? (Y/N): ').lower()
        
        if new_search == 'n' or new_search =='no':
            break

    elif choice == '2':
        client, idx = search_by_id(registers)

        if client == None:
            print("\n"+"The register entered has not been created yet!"+"\n")
        
        elif client is not None:
            show_registers(client)

        new_search = input('Do you want to do another search? (Y/N): ')

        if new_search == 'n' or new_search =='no':
            break
    
    elif choice == '3':
        break

    else:
        print('Wrong input value! Pleas, choose a valid option')