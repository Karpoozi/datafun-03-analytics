# project start
'''This project involves fetching data from the web, processing it using appropriate Python collections, and writing the processed data to files.'''

# import dependencies
import csv
import json
import pathlib
import requests
import pandas as pd

# data acquisition and write data functions
def fetch_and_write_txt_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_txt_file(folder_name, filename, response.text)
    else:
        print(f"Failed to fetch data: {response.status_code}")

def fetch_and_write_csv_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_csv_file(folder_name, filename, response.text)
    else:
        print(f"Failed to fetch CSV data: {response.status_code}")

def fetch_and_write_json_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_json_file(folder_name, filename, response.text)
    else:
        print(f"Failed to fetch JSON data: {response.status_code}")

def fetch_and_write_excel_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_excel_file(folder_name, filename, response.content)
    else:
        print(f"Failed to fetch Excel data: {response.status_code}")

def write_txt_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name) / filename
    with file_path.open('w') as file:
        file.write(data)
        print(f"Text data saved to {file_path}")

def write_csv_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name) / filename
    with file_path.open('w', newline='') as file:
        file.write(data)
        print(f"CSV data saved to {file_path}")

def write_json_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name) / filename
    with file_path.open('w') as file:
        json.dump(data, file)
        print(f"JSON data saved to {file_path}")

def write_excel_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name) / filename
    with file_path.open('wb') as file:
        file.write(data)
        print(f"Excel data saved to {file_path}")

# processing functions
def process_txt_file(folder_name, input_filename, output_filename):
    input_file_path = pathlib.Path(folder_name) / input_filename
    output_file_path = pathlib.Path(folder_name) / output_filename
    with input_file_path.open('r') as input_file:
        text = input_file.read()
        words = len(text.split())
        lines = text.count('\n') + 1
        with output_file_path.open('w') as output_file:
            output_file.write(f"Number of words: {words}\n")
            output_file.write(f"Number of lines: {lines}\n")
    print(f"Processed text data saved to {output_file_path}")

def process_csv_file(folder_name, input_filename, output_filename):
    input_file_path = pathlib.Path(folder_name) / input_filename
    output_file_path = pathlib.Path(folder_name) / output_filename
    
    # Initialize variables for statistics
    num_rows = 0
    num_columns = 0

    with input_file_path.open('r') as input_file:
        csv_reader = csv.reader(input_file)
        
        # Iterate over rows in the CSV file
        for row in csv_reader:
            num_rows += 1
            num_columns = max(num_columns, len(row))  # Update max number of columns
        
        # Write statistics to output file
        with output_file_path.open('w') as output_file:
            output_file.write(f"Number of rows: {num_rows}\n")
            output_file.write(f"Number of columns: {num_columns}\n")
    
    print(f"Processed CSV data saved to {output_file_path}")

def process_json_file(folder_name, input_filename, output_filename):
    input_file_path = pathlib.Path(folder_name) / input_filename
    output_file_path = pathlib.Path(folder_name) / output_filename
    try:
        with input_file_path.open('r') as input_file:
            data = json.load(input_file)
            # Example: Accessing specific information
            if 'people' in data and isinstance(data['people'], list):
                relevant_info = {
                    "Total": len(data['people']),
                    "People": [person.get('name', 'Unknown') for person in data['people']]
                }
                with output_file_path.open('w') as output_file:
                    json.dump(relevant_info, output_file)
                print(f"Processed JSON data saved to {output_file_path}")
            else:
                print("Invalid JSON data format")
    except Exception as e:
        print(f"An error occurred: {e}")

def process_excel_file(folder_name, input_filename, output_filename):
    input_file_path = pathlib.Path(folder_name) / input_filename
    output_file_path = pathlib.Path(folder_name) / output_filename
    try:
        # Depending on the structure of your Excel file, you may use libraries like pandas or xlrd to read the data
        # Here's a basic example using pandas
        df = pd.read_excel(input_file_path)
        # Perform analysis or extract information
        # Example: Calculate mean of a column
        mean_value = df['Column_Name'].mean()
        with output_file_path.open('w') as output_file:
            output_file.write(f"Mean value of Column_Name: {mean_value}\n")
        print(f"Processed Excel data saved to {output_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# main function
def main():
    txt_url = 'https://www.gutenberg.org/cache/epub/1513/pg1513-images.html'
    csv_url = 'https://raw.githubusercontent.com/MainakRepositor/Datasets/master/World%20Happiness%20Data/2020.csv'
    json_url = 'http://api.open-notify.org/astros.json'
    excel_url = 'https://github.com/bharathirajatut/sample-excel-dataset/raw/master/cattle.xls'
