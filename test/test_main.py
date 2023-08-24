from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from typing import List, Dict
import csv, os


#models
from test_models.clients import ClientRegister


app = FastAPI()
app.title = 'CRUD API'
app.description = 'A CRUD API for managing clients'
app.version = '0.1.0'


#Read all registers
def read_registers(_data_path):
    

    if not _data_path:
        return {'message': 'File not found'}

    try:
        with open(_data_path, 'r', encoding='utf-8') as file:
            registers = list(csv.DictReader(file))
            return registers
    except:
        return {'message': 'An error has ocurred'}


#Creation of home page for the API
@app.get('/', tags=['home'])
def home_page():
    message = HTMLResponse('''
    <html>
        <head>
            <title>CRUD API</title>
        </head>
        <body>
            <h1>WELCOME TO THE CRUD API</h1>
            <h2>Here you can manage your clients</h2>
            <h3>Go to <a href="/docs">/docs</a> to see the documentation</h3>
            <h3>Go to <a href="/clients">/clients</a> to see the clients list</h3>
        </body>
    </html>
    ''')
    return message

#Show all registers in the API
@app.get('/clients', tags=['clients'], status_code=200, response_model=List)
def get_clients():
    _data_path = os.path.abspath('./test_documents/test_data.csv')
    registers = read_registers(_data_path)
    return registers

#Read a client by id
@app.get('/clients/{client_id}', tags=['clients'], status_code=200)
def get_client(client_id: str):
    _data_path = os.path.abspath('./test_documents/test_data.csv')
    try:
        registers = read_registers(_data_path)
        for register in registers:
            if register['ID Number'] == client_id:
                return register
        return {'message': 'Client not found'}
    except FileNotFoundError:
        return {'message': 'The file could not be found'}
    except Exception as e:
        return {'message': f'An error occurred: {str(e)}'}

#Create a new client
@app.post('/clients', tags=['clients'], status_code=201)
def create_client(client: ClientRegister):
    _data_path = os.path.abspath('./test_documents/test_data.csv')
    try:
        registers = read_registers(_data_path)
        for register in registers:
            if register['ID Number'] == client.id_number:
                return {'message': 'Client already exists'}
        with open(_data_path, 'a', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames= client.model_dump().keys())
            writer.writerow(client.model_dump())
        return {'message': 'Client created successfully'}
    except FileNotFoundError:
        return {'message': 'The file could not be found'}
    