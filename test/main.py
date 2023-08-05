from testing_tools import *
from registers import *


def search_by_name(registers):
    
    clean_screen()
    name_to_search = input("Type the organization name: ")

    filtered_list = list(filter(lambda organization: name_to_search.lower() in organization["Organization name"].lower(), registers))
    
    if filtered_list:
        client_dict = filtered_list
        return client_dict
    
    else:
        client_dict = None
        return client_dict


registers = read_csv()
clients_dicts = search_by_name(registers)
show_registers(clients_dicts)


# def run ():
#     pass


# if __name__ == "__main__":
#     run()