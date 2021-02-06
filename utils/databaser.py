
from pymongo import MongoClient
from decouple import config
import os

class MakeMongo():
    def __init__(self):
        self.pw = config('PASSWORD')
        self.db_name = config('DATABASE_NAME')
        self.un = config('USERNAME')
        self.host = config('HOST')
        """ References
        https://able.bio/rhett/how-to-set-and-get-environment-variables-in-python--274rgt5
        
        from terminal -> touch .env -> creates .env file
        then, edit .env to have the following. 
        
        PASSWORD=<username>
        DATABASE_NAME=<username>
        USERNAME=<username>
        HOST=<username>
        
        export the above to your environment
        """
        pass

    def insert_df(self, database=None, collection=None, df=None):
        header = "mongodb+srv://"

        connection_string = str(header+self.un+":"+self.pw+"@"+self.host+"/"+"?retryWrites=true&w=majority")

        client = MongoClient(connection_string)

        if database:
            db = client[database]
        else:
            db = client[self.db_name]

        if df is not None and collection:
            # print(mongo_collection)
            # print(df.head())
            data_dict = df.to_dict("records")
            # print(data_dict)
            db[collection].delete_many({})
            db[collection].insert(data_dict)
            print('Inserted DB to Collection')





