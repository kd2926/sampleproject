# /usr/bin/env python
#config.py
import time
import logging

class config:
        # timestamp for the output file
        time_stamp = time.strftime("%Y%m%d_%H%M%S")

        #path for input csv file - user_data.csv
        csvpath = './input/user_data.csv'

        #path for input json file - readings.json
        jsonpath = './input/readings.json'

        #path where the output file is to be placed
        output_filename = './output/results_'+time_stamp+'.csv'

        # temperature filter to denote fever - while merging data sets
        temperature_filter = 99.5

        # log level in logging - INFO/DEBUG
        log_level = logging.INFO
