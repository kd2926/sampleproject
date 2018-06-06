#Purpose - To read user_data.csv, readings.json file, merge the datasets, output the results to a folder in csv format
#Created on - 6/5/2018
#Created By - Kanya Daivam
#Main logic of the application

#### NOTE: Given problem can be solved in multiple ways - using data frames alone, loading data to tables in Postgres or MySQL. 
### Here i used a memory table in sqlite as the data is fairly less. I would prefer to create a table in MySQL database to load data.
### date-wise and aggregate the tables.
### time complexity is to be evaluated based on the input size. 
### bad records are not tested for in the logic below.  

# imported needed packages
from pandas.io.json import json_normalize
import pandas as pd
import json
import sqlite3
import os, sys
parentPath = os.path.abspath("..")
if parentPath not in sys.path:
    sys.path.insert(0, parentPath)
# import config to access configuration variables 
from config import config
import logging

# Function to read JSON file
# Parameters: json_file - readings.json file in input folder
def read_json(json_file):
    #read json file
    data = []  # List to append json data
    try:
        with open(json_file) as f:
            for line in f:
                data.append(json.loads(line))
    except IOError as e:
        logger.error("Unable to open JSON file")
        
    readings_data = json_normalize(data) # normalize data to flatten user id column
    readings_data['user.id'] = readings_data['user.id'].apply(int) # Change user id object to Int 
    readings_data.columns = ['date', 'temperature', 'user_id'] # Renaming columns in readings file so that user.id can be user_id
    return readings_data

# Function to merge datasets.
# Parameters: user_data - containing data from user_data.csv, readings_data - containing data from readings.json
def merge_datasets(user_data, readings_data, condition):
    # Creating db in memory
    conn = sqlite3.connect(':memory:')

    # writing to tables 
    user_data.to_sql('user_data', conn, index = False)
    readings_data.to_sql('readings_data',conn, index = False)
    qry =  ''' select  B.date, A.zip, count(*) as Fever_count from user_data A join
                readings_data B on A.user_id  = B.user_id where B.temperature > %s group by B.date, A.zip''' %condition
    result_dataset = pd.read_sql_query(qry, conn)
    return result_dataset

# Function to write resulting dataset to csv file
# config.py has Filename to output the results to
# Parameters: result_dataset - query results by merging 2 dataframes
def write_to_csv(result_dataset, output_file):    
    result_dataset.to_csv(output_file, index=False)

if __name__ == '__main__':
    logging.basicConfig(level=config.log_level)
    logger = logging.getLogger(__name__)

    #read csv file
    logger.info('Start reading the csv file')
    user_data = pd.read_csv(config.csvpath)

    #read json file
    logger.info('Start reading the json file')
    readings_data = read_json(config.jsonpath)

    #Merging data sets
    logger.info('Create sqlite db to merge datasets')
    result_dataset = merge_datasets(user_data, readings_data, config.temperature_filter)

    #Write to CSV in output folder
    output_filename = config.output_filename
    logger.info('Write results to csv file %s' %output_filename )
    write_to_csv(result_dataset, output_filename )

