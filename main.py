import pandas as pd
from utils.databaser import MakeMongo
from utils.make_data import *

# starter code to get going

# read in a copy of the google form csv
# df = pd.read_csv('data/gform.csv')
# print(df.head())

# create a databaser object for mongoDB
# monger = MakeMongo()

# before running next, configure env variables for database access
# monger.insert_df(collection='hci', df=df)

make_form_data()

