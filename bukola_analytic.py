''' 

Module 3 Project Work
 Fetch data from Websites
 Process files within Python
 Write data into files

'''

# Standard library imports
import math
import statistics as stats
import os
import csv
import json
import pathlib
 
# External Modules (Virt Environment Required)

import requests
import pandas as pd
import pathlib

# Local module imports
import bukola_utils
import bukola_analytic

# Fetched Text file from URL and writes into new file.
def fetch_and_write_txt_data(txt_folder_name, txt_filename, txt_url):
    try:
        # Get data from the Sherlock Holmes story URL
        response = requests.get(txt_url)
        response.raise_for_status()

        # Create file path
        text_folder_path = pathlib.Path(txt_folder_name)
        text_file_path = text_folder_path / txt_filename
        text_file_path.parent.mkdir(parents=True, exist_ok=True)

        # Write the fetched text data to the file
        text_file_path.write_text(response.text, encoding='utf-8')
        print(f"Text data successfully saved to {text_file_path}")

    except Exception as ex:
        print(f"Error fetching and writing text data: {ex}")

# Fetch CSV file from URL and write into new file.

def fetch_and_write_csv_data(csv_folder_name, csv_filename, csv_url):
    try:
        # Fetches data from URL
        response = requests.get(csv_url)
        response.raise_for_status()

        # Creating file path
        csv_folder_path = pathlib.Path(csv_folder_name)
        csv_file_path = csv_folder_path / csv_filename
        csv_file_path.parent.mkdir(parents=True, exist_ok=True)

        # Write to file
        csv_file_path.write_text(response.text, encoding='utf-8')
        print(f"CSV data successfully saved to {csv_file_path}")

    except Exception as ex:
        print(f"Error fetching and writing csv data: {ex}")

# Fetch Excel file from URL and writes into new file.
def fetch_and_write_excel_data(excel_folder_name, excel_filename, excel_url):
    try:
        # Fetches data from URL
        response = requests.get(excel_url)
        response.raise_for_status()  # Raise an error for bad status codes

        # Construct the full file path using pathlib
        excel_folder_path = pathlib.Path(excel_folder_name)
        excel_file_path = excel_folder_path / excel_filename
        excel_file_path.parent.mkdir(parents=True, exist_ok=True)

        # Write data into file
        excel_file_path.write_bytes(response.content)
        print(f"Excel data successfully saved to {excel_file_path}")

    except Exception as ex:
        print(f"Error fetching and writing excel data: {ex}")

# Fetch JSON from URL and writes into a new file.
def fetch_and_write_json_data(json_folder_name, json_filename, json_url):
    try:
        # Fetches data from URL
        response = requests.get(json_url)
        response.raise_for_status()

        # Validate that the response contains JSON data
        try:
            data = response.json()
        except json.JSONDecodeError as ex:
            print(f"Error decoding JSON: {ex}")
            return

        # Construct the full file path using pathlib
        json_folder_path = pathlib.Path(json_folder_name)
        json_file_path = json_folder_path / json_filename

        # Ensure the parent directory exists
        json_file_path.parent.mkdir(parents=True, exist_ok=True)

        # Write the fetched JSON data to the file
        json_file_path.write_text(json.dumps(data, indent=4), encoding='utf-8')
        print(f"JSON data successfully saved to {json_file_path}")

    except Exception as ex:
        print(f"Error fetching and writing JSON data: {ex}")


# Process Excel file to text file
def process_text_data(txt_folder_name, txt_filename, output_filename):
    try:
        # Read the text file
        text_folder_path = pathlib.Path(txt_folder_name)
        text_file_path = text_folder_path / txt_filename
        text_data = text_file_path.read_text(encoding='utf-8')

        # Split text into words and calculate word count
        words = text_data.split()
        word_count = len(words)
      
        # Format the results
        result = f"Word Count: {word_count}\n{text_data}"

        # Write to file
        output_file_path = text_folder_path / output_filename
        output_file_path.write_text(result, encoding='utf-8')
        print(f"Text data processed and saved to {output_file_path}")

    except Exception as ex:
        print(f"Error processing text data: {ex}")

# Process CSV file to text file
def process_csv_data(csv_folder_name, csv_filename, output_filename):
    try:
        # Read the CSV data from the file
        csv_folder_path = pathlib.Path(csv_folder_name)
        csv_file_path = csv_folder_path / csv_filename
        csv_data = csv_file_path.read_text(encoding='utf-8').splitlines()

        # Parse the CSV data
        reader = csv.reader(csv_data)
        header = next(reader)
        rows = list(reader)

        # Example: Calculate average of a numeric column (assuming the last column is numeric)
        numeric_column = [float(row[-1]) for row in rows]
        average_value = sum(numeric_column) / len(numeric_column)
        result = f"Average of last column: {average_value:.2f}\n"

        # Write to file
        output_file_path = csv_folder_path / output_filename
        output_file_path.write_text(result, encoding='utf-8')
        print(f"CSV data processed and saved to {output_file_path}")

    except Exception as ex:
        print(f"Error processing CSV data: {ex}")


# Process Excel data to file
def process_excel_data(excel_folder_name, excel_filename, output_filename):
    try:
        # Read the Excel data from the file
        excel_folder_path = pathlib.Path(excel_folder_name)
        excel_file_path = excel_folder_path / excel_filename
        excel_data = pd.read_excel(excel_file_path)
        
        # Sum of data and results
        summary = excel_data.describe()
        result = summary.to_string()

        # Write to file
        output_file_path = excel_folder_path / output_filename
        output_file_path.write_text(result, encoding='utf-8')
        print(f"Excel data processed and saved to {output_file_path}")

    except Exception as ex:
        print(f"Error processing Excel data: {ex}")


# Process JSON data to file
def process_json_data(json_folder_name, json_filename, output_filename):
    try:
        # Read JSON from file
        json_folder_path = pathlib.Path(json_folder_name)
        json_file_path = json_folder_path / json_filename

        # JSON file contains data
        try:
            json_data = json_file_path.read_text(encoding='utf-8')
            if not json_data.strip():
                raise ValueError("JSON data is empty")
            data = json.loads(json_data)
        except json.JSONDecodeError as ex:
            print(f"Error decoding JSON: {ex}")
            return
        except ValueError as ex:
            print(ex)
            return

        if "people" not in data:
            raise KeyError("'people' key not found in JSON data")

        number_of_crafts= data.get('number', 0)
        astronaut_crafts = [person['craft'] for person in data['people']]

        result = f"Number of Spacecrafts: {number_of_crafts}\nSpacecrafts:\n"
        result += "\n".join(astronaut_crafts)

        # Write to file
        output_file_path = json_folder_path / output_filename
        output_file_path.write_text(result, encoding='utf-8')
        print(f"JSON data processed and saved to {output_file_path}")

    except KeyError as ex:
        print(ex)
    except Exception as ex:
        print(f"Error processing JSON data: {ex}")


#  Define main function
def main():

    print(f"Name: {bukola_utils}")

    #URLs to capture data from the web
    txt_url = 'https://sherlock-holm.es/stories/plain-text/cano.txt'
    csv_url = 'https://raw.githubusercontent.com/MainakRepositor/Datasets/master/World%20Happiness%20Data/2020.csv' 
    excel_url = 'https://github.com/bharathirajatut/sample-excel-dataset/raw/master/cattle.xls' 
    json_url = 'http://api.open-notify.org/astros.json'

    #Output folder names
    txt_folder_name = 'data-txt'
    csv_folder_name = 'data-csv'
    excel_folder_name = 'data-excel' 
    json_folder_name = 'data-json'

    #Output file names
    txt_filename = 'Sherlock_holmes.txt'
    csv_filename = 'Country_scores.csv'
    excel_filename = 'Cattle.xlsx' 
    json_filename = 'Astronauts.json' 

    #Fetch data from web and write the files
    fetch_and_write_txt_data(txt_folder_name, txt_filename, txt_url)
    fetch_and_write_csv_data(csv_folder_name, csv_filename,csv_url)
    fetch_and_write_excel_data(excel_folder_name, excel_filename,excel_url)
    fetch_and_write_json_data(json_folder_name, json_filename,json_url)

    #Process file data
    process_text_data('data-txt', 'Sherlock_holmes.txt', 'Sherlock_holmes_analysis.txt')
    process_csv_data('data-csv', 'Country_scores.csv', 'Country_scores_analysis.txt')
    process_excel_data('data-excel', 'Cattle.xlsx', 'Cattle_analysis.txt')
    process_json_data('data-json', 'Astronauts.json', 'Astronauts_analysis.txt')

# Call Main Function
if __name__ == '__main__':
    main()        