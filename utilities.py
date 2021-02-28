import pandas as pd
from utils.databaser import MakeMongo


# uncomment the next two lines to generate fake data
# from utils.make_data import *
# make_form_data()

df = pd.read_csv("data/observation_forms_2.csv")

# remove any invalid characters from df cols
df.columns = df.columns.str.replace(".", "_")

# create a databaser object for mongoDB
monger = MakeMongo()

# before running next, configure env variables for database access
monger.insert_df(collection='hci', df=df)



