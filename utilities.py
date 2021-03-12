from utils.databaser import MakeMongo

from utils.make_data import *
make_form_data()

df = pd.read_csv("data/observation_forms_2.csv")

# remove any invalid characters from df cols
df.columns = df.columns.str.replace(".", "_", regex=True)

df = df.dropna(axis='columns', how='all')

temperament = ["The judge was professional"
              , "The judge was compassionate"
              , "The judge was respectful"
              , "The judge was patient"]

df[temperament] = df[temperament].replace({'Strongly Agree':4
                                           ,'Agree':3
                                           ,'Neutral':2
                                           ,'Disagree':1
                                           ,'Strongly Disagree':0})

# create a databaser object for mongoDB
monger = MakeMongo()

# before running next, configure env variables for database access
monger.insert_df(collection='hci', df=df)

# df = pd.DataFrame()
# df = df.rename(columns={'Judge Name 1':'Judge Name'})
# df = df.dropna(subset=['Judge Name'])

df = df.groupby('Judge Name 1')[temperament].agg('mean')

df = df.agg(['mean', 'std', 'min', 'max', 'count'], axis='columns').reset_index()
df = df.round(2)
df = df.rename(columns={'index':'Judge Name 1'
                       , 'mean': 'Temperament Score'})


print(df)

# create a databaser object for mongoDB
monger = MakeMongo()
monger.insert_df(collection='agg_temperament_scores', df=df)
