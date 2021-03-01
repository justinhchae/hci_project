from utils.databaser import MakeMongo

from utils.make_data import *
make_form_data()

df = pd.read_csv("data/observation_forms_2.csv")

# remove any invalid characters from df cols
df.columns = df.columns.str.replace(".", "_")

temperament = ["The judge was professional"
              , "The judge was compassionate"
              , "The judge was respectful"
              , "The judge was patient"]

df[temperament] = df[temperament].replace({'Strongly Agree':5
                                           ,'Agree':4
                                           ,'Neutral':3
                                           ,'Disagree':2
                                           ,'Strongly Disagree':1})

# create a databaser object for mongoDB
monger = MakeMongo()

# before running next, configure env variables for database access
monger.insert_df(collection='hci', df=df)

communication = []

