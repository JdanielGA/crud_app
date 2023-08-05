import csv
from testing_tools import *
from registers import *


_csv_file_path = './documents/registers.csv'


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
            while True:
                clean_screen()
                print('You can return if you type "exit".'+'\n')
                value = input(f'Enter the {key}: ')
                
                if value.lower() == 'exit':
                    return None
                
                elif key == 'Organization name':
                    assessment, idx = search_exact_by_name(read_csv(), value)
                    if assessment is not None:
                        input(f'This register "{value}" already exists in tne index {idx}! press -Enter key- to continue')
                        return None
                    
                elif key == 'ID Number':
                    assessment, idx = search_exact_by_id(read_csv(), value)
                    if assessment is not None:
                        input(f'This register "{value}" already exists in tne index {idx}! press -Enter key- to continue')
                        return None
                    
                clean_screen()
                print('You can return if you type "exit".'+'\n')
                confirmation = input(f'is "{value}" correct for the {key}, (Y/N): ').lower()

                if confirmation == 'yes' or confirmation == 'y':
                    pre_dict[key] = value
                    break

                elif confirmation == 'exit':
                    return None

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
            print('This client was created:'+'\n')
            show_one_register(client_data)
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



if __name__ == "__main__":

    while True:
        clean_screen()
        question = input("Do yo want to creat a new register? (Y/N): ").lower()

        if question == 'y':
            client_data = pre_register()

            if client_data is not None:
                create_client(_csv_file_path, client_data)
                
        else:
            break




# def run ():
#     pass


# if __name__ == "__main__":
#     run()