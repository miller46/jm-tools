import os
import json
import csv

from jm_tools.strings import camel_to_snake

def create_file_if_not_exists(filename):
    if not os.path.isfile(filename):
        with open(filename, 'w'):
            pass

class LazyKeystoreWrapper:
    def __init__(self, **kwargs):
        self.keys = []
        for key, value in kwargs.items():
            attribute_name = camel_to_snake(key)
            setattr(self, attribute_name, value)
            self.keys.append(attribute_name)

    def get_keys(self):
        return self.keys

class LazyKeystore:

    def __init__(self, filename):
        self.filename = filename
        self.data = {}
        create_file_if_not_exists(filename)
        self.init_data()

    def init_data(self):
        if not os.path.isfile(self.filename):
            print(f'Error: File {self.filename} does not exist.')
        try:
            with open(self.filename, 'r') as file:
                json_object = json.load(file)
            self.data = json_object
        except Exception as e:
            print(f'Error occurred while loading JSON from file {self.filename}: {str(e)}')

    def set(self, key, value):
        self.data[key] = value
        self.save_file()

    def get(self, key, default_value=None):
        if key in self.data:
            return self.data[key]
        else:
            return default_value

    def save_file(self):
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.data, file)
        except Exception as e:
            print(f'Error occurred while writing JSON to file {self.filename}: {str(e)}')

    @staticmethod
    def complex_handler(obj):
        if hasattr(obj, '__json__'):
            return obj.__json__()
        elif isinstance(obj, list):
            return [LazyKeystore.complex_handler(i) for i in obj]
        elif isinstance(obj, dict):
            return {key: LazyKeystore.complex_handler(value) for key, value in obj.items()}
        else:
            raise TypeError(f'Object of type {type(obj).__name__} is not JSON serializable')


class LazyCsvStore:

    def __init__(self, filename, headers, primary_key_index=0):
        self.filename = filename
        self.headers = headers
        self.primary_key_index = primary_key_index
        create_file_if_not_exists(filename)
        if ".csv" not in filename:
            print(f'NOTE: this class is intended to be used with .csv files')

    def add_single_record(self, data):
        with open(self.filename, 'a') as file:
            line = self._make_line_for_record(data)
            file.write(line)

    def update_single_record(self, key, data):
        record_found = False
        temp_filename = self.filename.replace('.csv', '_temp.csv')
        with open(self.filename, 'r') as file, open(temp_filename, 'w') as temp_file:
            reader = csv.reader(file)
            writer = csv.writer(temp_file)

            for row in reader:
                primary_key = row[self.primary_key_index]
                if key == primary_key:
                    record_found = True
                    line = self._make_line_for_record(data)
                    temp_file.write(line)
                else:
                    writer.writerow(row)
        if not record_found:
            print(f"Record {key} not found")
            if os.path.exists(temp_filename):
                os.remove(temp_filename)
        else:
            os.remove(self.filename)
            os.rename(temp_filename, self.filename)

    def _make_line_for_record(self, data):
        line = ""
        for header in self.headers:
            column = data[header]
            line += f"{column},"
        if line.endswith(','):
            line = line[:-1]
        return f"{line}\n"

    def add_many_records(self, records):
        with open(self.filename, 'a') as file:
            for data in records:
                line = self._make_line_for_record(data)
                file.write(line)

    def search_records(self, key):
        with open(self.filename, 'r') as file:
            reader = csv.reader(file)
            all_rows = list(reader)
            for row in all_rows:
                primary_key = row[self.primary_key_index]
                if key == primary_key:
                    record = self._parse_single_record(row)
                    return record
        return None

    def _parse_single_record(self, record):
        row_data = {}
        index = 0
        for header in self.headers:
            if len(record) > index:
                row_data[header] = record[index]
            else:
                row_data[header] = None
            index = index + 1
        return row_data

    def get_all_records(self):
        replies = {}
        with open(self.filename, 'r') as file:
            reader = csv.reader(file)
            all_rows = list(reader)
            row_number = 0
            for row in all_rows:
                if row_number > 0:
                    record = self._parse_single_record(row)
                    primary_key = row[0]
                    replies[primary_key] = record
                row_number = row_number + 1
        return replies

    def get_all_records_as_objects(self):
        records = []
        with open(self.filename, 'r') as file:
            reader = csv.reader(file)
            all_rows = list(reader)
            row_number = 0
            for row in all_rows:
                if row_number > 0:
                    record = self._parse_single_record(row)
                    new_object = self.create_object_from_record(record)
                    records.append(new_object)
                row_number = row_number + 1
        return records

    def create_object_from_record(self, record):
        new_record = {}
        for attribute in record:
            value = record[attribute]
            new_attribute = camel_to_snake(attribute)
            new_record[new_attribute] = value
        # data = dict(zip(self.headers, record))
        new_object = dict(**new_record)
        return new_object
