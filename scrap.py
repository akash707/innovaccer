import pandas as pd
import sqlalchemy as sql
import pymysql
pymysql.install_as_MySQLdb()
import sys
import json 

# sheet URL 
MAIN_SHEET_URL = 'https://docs.google.com/spreadsheets/d/199haoLuNdcyaMdPcpVHWbcqPlLwYUA4XXHc0ExDS_9E/edit#gid=0'

# Database connection credentials
DATABASE_TABLE_NAME = 'sheet_data'
DATABASE_NAME = 'sheet'
DATABASE_HOST = 'localhost'
DATABASE_PORT = '3306'
DATABASE_USERNAME = 'root'
DATABASE_PASSWORD = 'shukla'

# function to convert spreadsheet default to csv URL
def create_spreadsheet_csv_url(sheet_url):
    return sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')

# function to insert data of spreadsheet inside the database after crawling the spreadsheets
def insert_spreadsheet_data():
    # reading data from main google spreadsheet as csv using URL
    main_sheet_data_frames = pd.read_csv(create_spreadsheet_csv_url(MAIN_SHEET_URL), index_col=False)
    # checking if Urls column present inside the main spreadsheet 
    if('Urls' in main_sheet_data_frames):
        print "Main sheet spreadsheet URL's {}".format(main_sheet_data_frames['Urls'].values)
        try:
            all_sheet_urls = main_sheet_data_frames['Urls'].values
            all_sheet_data_frame = []
            # checking if all_sheet_urls are present to read data 
            if len(all_sheet_urls) > 0 :
                for url in all_sheet_urls:
                    print 'Each URL {}'.format(url)
                    # reading data from spreadsheet as csv using URL
                    each_sheet_data = pd.read_csv(create_spreadsheet_csv_url(url), index_col=False)
                    each_sheet_data['sheet_url'] = url
                    print "Each sheet data {}".format(each_sheet_data)
                    all_sheet_data_frame.append(each_sheet_data)
                # concatenating each data frame 
                allData = pd.concat(all_sheet_data_frame, axis=0, sort=False)
                # connect to the database using connection URL
                engine = sql.create_engine('mysql://{0}:{1}@{2}:{3}/{4}'.format(DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_HOST, DATABASE_PORT, DATABASE_NAME))
                with engine.connect() as conn, conn.begin():
                    # saving dataframes of each sheet inside a single database table
                    allData.to_sql(DATABASE_TABLE_NAME, conn, if_exists='replace')
                    print("Spreadsheet data successfully added inside the database")
            else:
                print("No spreadsheet URL present")
        except Exception as e:
            print 'Error {}'.format(e)
    else:
        print("Not able to get URL's from main spreadsheet")


def get_sheet_data(sheets):
    try:
        engine = sql.create_engine('mysql://{0}:{1}@{2}:{3}/{4}'.format(DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_HOST, DATABASE_PORT, DATABASE_NAME))
        with engine.connect() as conn, conn.begin():
            query = 'SELECT * FROM {} WHERE sheet_url IN %s'.format(DATABASE_TABLE_NAME)
            result = conn.execute(query, [(sheets,)]).fetchall()
            print("Sheets response {}".format(len(result)))
            print(json.dumps([dict(r) for r in result]))
            
    except Exception as e:
        print "Error in getting sheet data {}".format(e)


if __name__ == '__main__':
   print "Command line argumnets - {}".format(len(sys.argv))
   print(len(sys.argv))
   params = []
   if(len(sys.argv) > 2):
       for i in range(2, len(sys.argv)):
           params.append(sys.argv[i])
       globals()[sys.argv[1]](params)
   else:
    globals()[sys.argv[1]]()
