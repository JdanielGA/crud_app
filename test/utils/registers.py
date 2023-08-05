import csv


def read_csv(_file_path="./documents/registers.csv"):

    with open(_file_path, mode="r", encoding="utf-8") as csv_file:
        registers = list(csv.DictReader(csv_file))
        return registers