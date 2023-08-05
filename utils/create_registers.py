from utils.tools import clean_screen, show_one_register, wait
import csv

def pre_register():


    client_data ={
            'Organization name': '',
            'ID Number': '',
            'Email': '',
            'Phone number': '',
            'City': '',
            'Adress': '',
            'Contact name': '',
            'Contact phone number': '',
            'Other information': ''
        }

    pre_dict = {}


    while True:

        for key in client_data:
            
            clean_screen()

            while True:
                print('Type "exit" if you wat to return')
                value = input(f'Enter the {key}: ')
                stop_adding = value.lower()
                if stop_adding == 'exit':
                    return None

                confirmation = input(f'is {value} correct for the {key}, (Y/N): ').lower()
                if confirmation == 'yes' or confirmation == 'y':
                    stop_adding = confirmation.lower()
                    if stop_adding == 'exit':
                        return None
                    
                    pre_dict[key] = value
                    break  

                else:
                    print(f'The {key} has not been added')

        clean_screen()
        print('Please check the data: '+'\n')

        for key, value in pre_dict.items():
            print(f'{key}: {value}')

        final_confirmation = input(f'\n'+'is the data correct? (Y/N): ').lower()

        if final_confirmation == 'yes' or final_confirmation == 'y':
            clean_screen()
            client_data = pre_dict
            print('This client is being adding:'+'\n')
            show_one_register(client_data)
            wait(1)
            break

        else:
            clean_screen()
            print('\n'+'The client was not created!')
            wait(2)
            pre_dict = {}
    
    return client_data


def create_client(_csv_file_path, client_data):

    header = list(client_data.keys())

    try:
        with open(_csv_file_path, 'r', newline='') as file:
            reader = csv.DictReader(file)
            data = list(reader)

    except FileNotFoundError:
        with open(_csv_file_path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
            data = []


    data.append(client_data)


    with open(_csv_file_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        writer.writerows(data)


    print("The client was created successfully")