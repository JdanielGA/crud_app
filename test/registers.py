import csv
from testing_tools import *


def read_csv(_file_path="./documents/registers.csv"):

    with open(_file_path, mode="r", encoding="utf-8") as csv_file:
        registers = list(csv.DictReader(csv_file))
        return registers


def search_by_name(registers,name_to_search):

    filtered_list = []
    idx_list=[]

    for idx, organization in enumerate(registers):
        if name_to_search.lower() in organization["Organization name"].lower():
            filtered_list.append(organization)
            idx_list.append(idx)


def search_exact_by_name(registers, name_to_search):

    filtered_list = []
    idx = 0

    for ref, organization in enumerate(registers):
        if name_to_search.lower() == organization["Organization name"].lower():
            filtered_list.append(organization)
            idx = ref
    
    if filtered_list:
        client_dict = filtered_list
        return client_dict, idx
    
    else:
        client_dict = None
        idx = None
        return client_dict, idx


def search_exact_by_id(registers, id_to_search):
    
    filtered_list = []
    idx = 0

    for ref, organization in enumerate(registers):
        if id_to_search == organization["ID Number"]:
            filtered_list.append(organization)
            idx = ref


    if filtered_list:
        client_dict = filtered_list
        return client_dict, idx
    else:
        client_dict = None
        idx = None
        return client_dict, idx


# clean_screen()
# _data = read_csv()
# information, idx = search_exact_by_id(_data,'100200006')
# print(information)
# print(idx)
# cliets_dicts, idx_list = zip(*information)
# cliets_dicts = list(cliets_dicts)
# print(type(cliets_dicts))
# show_registers(cliets_dicts)

