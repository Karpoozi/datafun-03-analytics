# project start
'''This project involves fetching data from the web, processing it using appropriate Python collections, and writing the processed data to files.'''

# import dependencies 
import json
import pathlib
import requests
import pandas as pd

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
    try:
        response = requests.get(url, timeout=15)  # kept getting error so timeout after 15 seconds
        if response.status_code == 200:
            write_json_file(folder_name, filename, response.text)
        else:
            print(f"Failed to fetch JSON data: {response.status_code}")
    except requests.exceptions.Timeout:
        print("Connection timed out. Please check your network connection.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def fetch_and_write_excel_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_excel_file(folder_name, filename, response.content)
    else:
        print(f"Failed to fetch Excel data: {response.status_code}")

def write_txt_file(folder_name, filename, data):
    folder_path = pathlib.Path(folder_name)
    folder_path.mkdir(parents=True, exist_ok=True)  # Ensure the directory exists
    file_path = folder_path / filename
    with file_path.open('w') as file:
        file.write(data)
        print(f"Text data saved to {file_path}")

def write_csv_file(folder_name, filename, data):
    folder_path = pathlib.Path(folder_name)
    folder_path.mkdir(parents=True, exist_ok=True)  # Ensure the directory exists
    file_path = folder_path / filename
    with file_path.open('w', newline='') as file:
        file.write(data)
        print(f"CSV data saved to {file_path}")

def write_json_file(folder_name, filename, data):
    folder_path = pathlib.Path(folder_name)
    folder_path.mkdir(parents=True, exist_ok=True)  # Ensure the directory exists
    file_path = folder_path / filename
    with file_path.open('w') as file:
        try:
            json_data = json.loads(data)
            json.dump(json_data, file, indent=4)
            print(f"JSON data saved to {file_path}")
        except json.JSONDecodeError as e:
            print(f"Invalid JSON data: {e}")

def write_excel_file(folder_name, filename, data):
    folder_path = pathlib.Path(folder_name)
    folder_path.mkdir(parents=True, exist_ok=True)  # Ensure the directory exists
    file_path = folder_path / filename
    with file_path.open('wb') as file:
        file.write(data)
        print(f"Excel data saved to {file_path}")

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
    try:
        df = pd.read_csv(input_file_path)
        num_rows, num_columns = df.shape
        with output_file_path.open('w') as output_file:
            output_file.write(f"Number of rows: {num_rows}\n")
            output_file.write(f"Number of columns: {num_columns}\n")
        print(f"Processed CSV data saved to {output_file_path}")
    except pd.errors.ParserError as e:
        print(f"Error parsing CSV file: {e}")

def process_json_file(folder_name, input_filename, output_filename):
    input_file_path = pathlib.Path(folder_name) / input_filename
    output_file_path = pathlib.Path(folder_name) / output_filename
    try:
        with input_file_path.open('r') as input_file:
            data = json.load(input_file)
            if 'people' in data and isinstance(data['people'], list):
                relevant_info = {
                    "Total": len(data['people']),
                    "People": [person.get('name', 'Unknown') for person in data['people']]
                }
                with output_file_path.open('w') as output_file:
                    json.dump(relevant_info, output_file, indent=4)
                print(f"Processed JSON data saved to {output_file_path}")
            else:
                print("Invalid JSON data format")
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"An error occurred: {e}")

def process_excel_file(folder_name, input_filename, output_filename):
    input_file_path = pathlib.Path(folder_name) / input_filename
    output_file_path = pathlib.Path(folder_name) / output_filename
    try:
        df = pd.read_excel(input_file_path)
        # Perform analysis or extract information
        # Example: Calculate mean of a column
        mean_value = df['c1'].mean()
        with output_file_path.open('w') as output_file:
            output_file.write(f"Mean value of Column_Name: {mean_value}\n")
        print(f"Processed Excel data saved to {output_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Define folder names and filenames for each type of data
    txt_folder_name = 'txt_data'
    csv_folder_name = 'csv_data'
    json_folder_name = 'json_data'
    excel_folder_name = 'excel_data'
    
    txt_filename = 'data.txt'
    csv_filename = 'data.csv'
    json_filename = 'data.json'
    excel_filename = 'data.xls'

    # URLs for fetching data
    txt_url = 'https://www.gutenberg.org/cache/epub/1513/pg1513-images.html'
    csv_url = 'https://raw.githubusercontent.com/MainakRepositor/Datasets/master/World%20Happiness%20Data/2020.csv'
    json_url = 'http://api.open-notify.org/astros.json'
    excel_url = 'https://github.com/bharathirajatut/sample-excel-dataset/raw/master/cattle.xls'

    # Fetch and write text data
    fetch_and_write_txt_data(txt_folder_name, txt_filename, txt_url)

    # Fetch and write CSV data
    fetch_and_write_csv_data(csv_folder_name, csv_filename, csv_url)

    # Fetch and write JSON data
    fetch_and_write_json_data(json_folder_name, json_filename, json_url)

    # Fetch and write Excel data
    fetch_and_write_excel_data(excel_folder_name, excel_filename, excel_url)

    # Process text file
    process_txt_file(txt_folder_name, txt_filename, 'processed_data.txt')

    # Process CSV file
    process_csv_file(csv_folder_name, csv_filename, 'processed_data.txt')

    # Process JSON file
    process_json_file(json_folder_name, json_filename, 'processed_data.json')

    # Process Excel file
    process_excel_file(excel_folder_name, excel_filename, 'processed_data.txt')

if __name__ == '__main__':
    main()