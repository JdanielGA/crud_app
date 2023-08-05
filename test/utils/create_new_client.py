import csv


def create_new_client():

    _csv_file_path = './documents/registers.csv'


    clients ={
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

        for key in clients:
            
            while True:
                value = input(f'Enter the {key}: ')
                confirmation = input(f'is {value} correct for the {key}, (Y/N): ').lower()

                if confirmation == 'yes' or confirmation == 'y':
                    pre_dict[key] = value
                    break        
                else:
                    print(f'The {key} has not been added')

        print('Please check the data: '+'\n')

        for key, value in pre_dict.items():
            print(f'{key}: {value}')

        final_confirmation = input(f'\n'+'is the data correct? (Y/N): ').lower()

        if final_confirmation == 'yes' or final_confirmation == 'y':
            clients = pre_dict
            print('This client was created:'+'\n')

            for key, value in clients.items():
                print(f'{key}: {value}')
            break
        else:
            print('\n'+'The client was not created:')
            pre_dict = {}


    header = list(clients.keys())


    try:
        with open(_csv_file_path, 'r', newline='') as file:
            reader = csv.DictReader(file)
            data = list(reader)

    except FileNotFoundError:
        with open(_csv_file_path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
            data = []


    data.append(clients)


    with open(_csv_file_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        writer.writerows(data)


    print("The client was created successfully")
