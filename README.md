# A Sample Project in Python

This sample project aim is to read data from CSV file, JSON file and join the data (using a key and group by) and output the results in csv. 

Structure of the project - 
  1. sample - folder which contains the logic 
  2. sample/input - folder with input data 
  3. sample/output - folder where the output data will be placed after the python program is executed
  4. tests/ - folder to hold the testcases. To be added.

Files and their significance - 
  1. config.py - config variables which can be tweaked/changed when needed to without changing the logic in the main file - fever_count_per_day_zip.py
  2. setup.py - metadata about the project

Steps to be followed -
  1. virtualenv kinsa
  2. source kinsa/bin/activate
  3. git clone https://github.com/kd2926/sampleproject.git
  2. cd sampleproject
  3. python setup.py install 
  4. cd sample 
  5. python fever_count_per_day_zip.py
 
 Output will be generated to sample/output with current timestamp appended.
