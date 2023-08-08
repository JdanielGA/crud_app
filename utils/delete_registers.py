from utils.tools import clean_screen, show_one_register
import csv

def delete_register(registers, idx):

    clean_screen()
    _pre_list = registers
    register_eliminated = _pre_list.pop(idx)
    print('\n'+'You are going to eliminate the following register:'+'\n')
    show_one_register(register_eliminated)
    confirmation = input('\n'+'Type "Confirm" to continue: ')

    if confirmation == 'Confirm':
        _csv_file_path = './documents/registers.csv'
        
        with open(_csv_file_path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=_pre_list[0].keys())
            writer.writeheader()
            writer.writerows(_pre_list)

        input('\n'+'The client was eliminated successfully!, press -Enter key- to continue: ')

    else:
        return print('The client was not eliminated successfully!')
    

def delete_all_registers():
    
    empty_data ={
        'Organization name': None,
        'ID Number': None,
        'Email': None,
        'Phone number': None,
        'City': None,
        'Adress': None,
        'Contact name': None,
        'Contact phone number': None,
        'Other information': None
    }

    confirmation = input('WARNING! you are going to eliminate all registers. type "Eliminate all" to continue: ')

    if confirmation == 'Eliminate all':
        _csv_file_path = './documents/registers.csv'
        
        with open(_csv_file_path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=empty_data.keys())
            writer.writeheader()
            writer.writerows([empty_data])

        input('\n'+'All registers were eliminated successfully!, press -Enter key- to continue: ')

    else:
        input('\n'+'No register was eliminated!, press -Enter key- to continue: ')