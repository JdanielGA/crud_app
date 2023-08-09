from utils.tools import show_one_register, clean_screen
from utils.create_registers import pre_register
from utils.read_registers import search_exact_by_name, search_exact_by_id
import csv


def full_update(registers, idx):
    ref_list = [client.copy() for client in registers]
    client_to_update = ref_list.pop(idx)
    print('\nYou are goun to update the following client:')
    show_one_register(client_to_update)
    confirmation = input('Do you want to continue? (Y/N): ')

    if confirmation.lower() == 'y' or confirmation.lower() == 'yes':
        updated_client = pre_register(ref_list)
        if updated_client is not None:
            ref_list.append(updated_client)
            ref_list.sort(key=lambda x:x['Organization name'])
            _csv_file_path = './documents/registers.csv'
            header = list(updated_client)

            with open(_csv_file_path, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=header)
                writer.writeheader()
                writer.writerows(ref_list)
            
            input('The client was update successfully!, press -Enter key- to continue: ')

        else:
            input('The client was not update successfully!, press -Enter key- to continue: ')
    
    elif confirmation.lower() == 'n' or confirmation.lower() == 'no':
        input('\nThe client was not update successfully!, press -Enter key- to continue: ')

    else:
        input('\n'+'Invalid input! press -Enter key- to continue: ')


def simple_update(registers, idx):
    
    ref_list = [client.copy() for client in registers]
    client_to_update = ref_list[idx]
    print('\nYou are goun to update the following client:')
    show_one_register(client_to_update)   
    confirmation = input('Do you want to continue? (Y/N): ')

    if confirmation.lower() == 'y' or confirmation.lower() == 'yes':
        clean_screen()
        print('What information do you want to update: '+'\n')
        options = list(client_to_update.keys())

        for number, option in enumerate(options, start=1):    
            print(f'#   {number}>  {option}: {client_to_update[option]}')
            
        chosen_option = input(f'#\n#    choose one option between 1 and {len(client_to_update)}:\n#\n# => ')
        if chosen_option.isdigit():
            chosen_option = int(chosen_option)            
            if 1 <= chosen_option <= len(options):
                chosen_option = options[chosen_option - 1]
                new_value = input(f'\nEnter the new value for {chosen_option}: ')

                if chosen_option == 'Organization name':
                    comprobation = search_exact_by_name(ref_list,new_value)[0]
                    if comprobation is not None:
                        input(f'\nThat reagister already exist or you are using the same {chosen_option}! Press -Enter key- to continue: ')
                        return None
                    
                elif chosen_option == 'ID Number':
                    comprobation = search_exact_by_id(ref_list,new_value)[0]
                    if comprobation is not None:
                        input(f'\nThat reagister already exist or you are using the same {chosen_option}! Press -Enter key- to continue: ')
                        return None
                
                client_to_update[chosen_option] = new_value
                _csv_file_path = './documents/registers.csv'
                header = list(client_to_update)
                with open(_csv_file_path, 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=header)
                    writer.writeheader()
                    writer.writerows(ref_list)

                clean_screen()
                input('\nThe client was updated successdully! Press -Enter key- to continue: ')
            
            else:
                input('\nInvalid option number! Press -Enter key- to continue: ')

        else:
            input('\nInvalid option number! Press -Enter key- to continue: ')

    
    elif confirmation.lower() == 'n' or confirmation.lower() == 'no':
        input('\nThe client was not update successfully!, press -Enter key- to continue: ')

    else:
        input('\n'+'Invalid input! press -Enter key- to continue: ')