# Innovaccer
Python script to scrap data from google spreasheets 

<b> Requirements :</b>
1. Python 2.7
2. Virtualenv ( python dependency to create isolated Python environments )
3. MySQL


<b> How to setup the project :</b>
1. Install virtualenv.
2. After installing the virtualenv, create a virtual environment by using this command : <br/>
   - virtualenv virtual_environment_name 
3. After creating the virtualenv, activate virtual environment by using this command : <br/>
   - source virtual_environment_name/bin/activate
4. After activating the virtualenv, go the directory level where requirements.txt file is present. Run this command inside that directory to install all python dependencies related to this project : <br/>
   - pip install -r requirements.txt 
5. After installing the dependencies, Now enter the configuration details inside the <b> scrap.py </b> file:
    <b>sheet URL:</b> 
    ( This is the URL of main spreadsheet that contains multiple rows with spreadsheets URL's inside the column name       <b>Urls</b>) <br/>
   
   MAIN_SHEET_URL = 'https://docs.google.com/spreadsheets/d/199haoLuNdcyaMdPcpVHWbcqPlLwYUA4XXHc0ExDS_9E/edit#gid=0'

    <b>Database connection credentials:</b> <br/>
    DATABASE_TABLE_NAME = 'sheet_data' <br/>
    DATABASE_NAME = 'sheet' <br/>
    DATABASE_HOST = 'localhost' <br/>
    DATABASE_PORT = '3306' <br/>
    DATABASE_USERNAME = 'root' <br/>
    DATABASE_PASSWORD = 'shukla' 
   
   
<b> How to run the script for different purposes :</b>

1. For scrapping the data from each spreadsheet URL's present inside the main spreadsheet and save it to database. Run this     command
   - python scrap.py insert_spreadsheet_data
   ( * Note - In this command, insert_spreadsheet_data is the function which will scrap data from URL's of multiple spreadsheets present inside the main spreadsheet and save that scrapped data inside the database). You can replace
 <b>MAIN_SHEET_URL</b> value with any spreadsheet URL that contains other spreadhsheet URL's.
 
2. For getting the sheet data from the database based on the data sheet's URL : <br/>
   - For getting the data of a single sheet from the datbase. Use this command : <br/>
     - python scrap.py get_sheet_data "https://docs.google.com/spreadsheets/d/1GhV-YU-aNCqpHUzpJbW5qf1OHKC-   
       vhlIn_0mSj4snxw/edit#gid=0"
       
   - For getting the data of multiple sheets from the database. Use this command : <br/>
     - python scrap.py get_sheet_data "https://docs.google.com/spreadsheets/d/1GhV-YU-aNCqpHUzpJbW5qf1OHKC- 
       vhlIn_0mSj4snxw/edit#gid=0"     
       "https://docs.google.com/spreadsheets/d/1oKPFS7gCsKWCSAQoeUT1Lwk1cKdUB6Z_LqHl7dMMFUE/edit#gid=0"
      
      ( * Note - You can pass any number of sheets URL's for retrieving data of each sheet URL)
  
 
