from create_new_client import *

# def full_register_update(_registers, idx):

#     new_list = _registers
#     client_to_update = new_list.pop(idx)
#     updated_client = pre_register(new_list)
#     new_list.append(updated_client)
#     new_list.sort(key=lambda x:x['Organization name'])
#     print('The client was update successfully')
#     return new_list


def simple_register_update(_registers, client_dict):


        print('What information do you want to update: '+'\n')
        options = list(client_dict.keys())

        for number, option in enumerate(options, start=1):
    
            print(f'#   {number}>  {option}: {client_dict[option]}')
            
        chosen_option = input(f'#\n#    choose one option between 1 and {len(client_dict)}:\n#\n# => ')

        if chosen_option.isdigit():
            chosen_option = int(chosen_option)
            
            if 1 <= chosen_option <= len(options):
                chosen_option = options[chosen_option - 1]
                new_value = input(f'\nEnter the new value for {chosen_option}: ')
                
                if chosen_option == 'Organization name':
                    comprobation = search_exact_by_name(_registers,new_value)[0]
                    if comprobation is not None:
                        input(f'\nThat reagister already exist or you are using the same {chosen_option}! Press -Enter key- to continue: ')
                        return None
                    
                elif chosen_option == 'ID Number':
                    comprobation = search_exact_by_id(_registers,new_value)[0]
                    if comprobation is not None:
                        input(f'\nThat reagister already exist or you are using the same {chosen_option}! Press -Enter key- to continue: ')
                        return None
                
                client_dict[chosen_option] = new_value
                clean_screen()
                print('The client was update successfully')
                return _registers

            else:
                print('Invalid option number.')
        else:
            print('Invalid input.')