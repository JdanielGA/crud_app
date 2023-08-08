from testing_tools import *
from registers import *


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



def _delete_one_register(clients_list, idx):
    
    _pre_list = clients_list
    register_eliminated = _pre_list.pop(idx)
    print('\n'+'You are going to eliminate the following register:'+'\n')
    show_one_register(register_eliminated)
    confirmation = input('\n'+'Type "Confirm" to continue: ').lower()
    if confirmation == 'confirm':
        return _pre_list
    else:
        return None


def run (clients_list):

    clean_screen()
    show_registers(clients_list)
    _find_register = input('Type the name of the register to eliminate: ')
    register_dict, idx = search_exact_by_name(clients_list, _find_register)
    _prelist = _delete_one_register(clients_list, idx)

    if _prelist is not None:
        clients_list = _prelist
        print('The register was eliminated successfully. This is the new list: '+'\n')
        show_registers(clients_list)
        input('press -Enter key- to continue: ')
        return clients_list

    else:
        print('\n'+'The register was not eliminated successfully.')
        register_dict = None
        idx = None
        return register_dict, idx



if __name__ == "__main__":
    run(clients_list)