from testing_tools import *
from test_registers import *
from create_new_client import *
from test_update import *


clients_list = [
    {
        'Organization name': 'Company 01',
        'ID Number': '100200001',
        'Email': 'info@Company01.com',
        'Phone number': '300400101',
        'City': 'Bogotá',
        'Adress': 'Calle 123 #45-67',
        'Contact name': 'Sebastián López Gómez',
        'Contact phone number': '3215551234',
        'Other information': 'additional info 1'
    },
    {
        'Organization name': 'Company 02',
        'ID Number': '100200002',
        'Email': 'info@Company02.com',
        'Phone number': '300400102',
        'City': 'Medellín',
        'Adress': 'Carrera 78A #23-45',
        'Contact name': 'Valentina Mendoza',
        'Contact phone number': '3104445678',
        'Other information': 'additional info 2'
    },
    {
        'Organization name': 'Company 03',
        'ID Number': '100200003',
        'Email': 'info@Company03.com',
        'Phone number': '300400103',
        'City': 'Cali',
        'Adress': 'Avenida 456 #67-89',
        'Contact name': 'Andrés Ramirez',
        'Contact phone number': '3001112222',
        'Other information': 'additional info 3'
    },
    {
        'Organization name': 'Company 04',
        'ID Number': '100200004',
        'Email': 'info@Company04.com',
        'Phone number': '300400104',
        'City': 'Cartagena',
        'Adress': 'Calle 987 #12-34',
        'Contact name': 'María Rodriguez',
        'Contact phone number': '3502223333',
        'Other information': 'additional info 4'
    },
    {
        'Organization name': 'Company 05',
        'ID Number': '100200005',
        'Email': 'info@Company05.com',
        'Phone number': '300400105',
        'City': 'Barranquilla',
        'Adress': 'Carrera 56 #78-90',
        'Contact name': 'Carlos Perez',
        'Contact phone number': '3203334444',
        'Other information': 'additional info 5'
    }
]

## Option 1:
# if client_dict is not None:
#         print('\n'+'You are going to update the following information: ')
#         show_registers(client_dict)
#         confirmation = input('\n'+'type (Y/N) to continue: ').lower()
#         if confirmation == 'y' or confirmation == 'yes':
#             full_register_update(_registers, idx)


def run():
    
    clean_screen()
    _registers = [client.copy() for client in clients_list]
    name_to_search = 'Company 05'
    client_dict, idx = search_exact_by_name(_registers, name_to_search)

    if client_dict is not None:
        
        new_list = simple_register_update(_registers, client_dict)

    else:
        input('That register does not exit! Press -Enter key- to continue: ')

    show_registers(new_list)
    

if __name__ == "__main__":
    run()
    show_registers(clients_list)