import pandas as pd
import numpy as np
import random
import datetime
import itertools

from pytz import timezone

from faker import Faker
fake = Faker()
pd.set_option('display.max_columns', None)


n_observations = 5000
n_judges = 389
n_no_judges= int(np.floor(n_judges * .3))
n_observers = 100
n_attorneys = 302
n_no_attorneys = int(np.floor(n_attorneys * .3))

def make_random_date(start_times, court_room):

    central = timezone('US/Central')

    start_range = datetime.date(2021, 1, 1)
    end_range = datetime.date(2021, 12, 31)
    time_between_dates = end_range - start_range
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)

    weekdays = [0,1,2,3,4]
    counter = 0
    flag = 100

    while 1:
        counter +=1
        random_date = start_range + datetime.timedelta(days=random_number_of_days)

        if random_date.weekday() in weekdays:
            random_date_string = str(random_date)

            if "Bridgeview" in court_room or "Markham" in court_room:
                random_time = "9:30:00"
            else:
                random_time = random.choice(start_times)

            date_string = random_date_string + ' ' + random_time
            date_time_obj = datetime.datetime.strptime(date_string
                                                       , '%Y-%m-%d %H:%M:%S')

            date_time_obj = central.localize(date_time_obj)
            #TODO add central time as 'CT'
            date_time_string = date_time_obj.strftime("%Y/%m/%d %H:%M:%S")
            date_string = date_time_obj.strftime("%Y/%m/%d")

            return date_time_string, random_time, date_string

        if counter > 50:
            add_days = datetime.timedelta(days=2)
            random_date = random_date + add_days
            random_date_string = str(random_date)
            random_time = random.choice(start_times)
            date_string = random_date_string + ' ' + random_time
            date_time_obj = datetime.datetime.strptime(date_string
                                                       , '%Y-%m-%d %H:%M:%S')

            date_time_obj = central.localize(date_time_obj)
            # TODO add central time as 'CT'
            date_time_string = date_time_obj.strftime("%Y/%m/%d %H:%M:%S")
            date_string = date_time_obj.strftime("%Y/%m/%d")

            return date_time_string, random_time, date_string


responses = ['Strongly Agree', 'Strongly Agree', 'Strongly Agree', 'Agree', 'Agree', 'Agree', 'Neutral', 'Neutral', 'Disagree', 'Strongly Disagree']

judge_names = []
for _ in range(n_judges):
    judge_names.append(fake.name())

empty_judges = list(itertools.repeat(None, n_no_judges))

judge_names.extend(empty_judges)
# Faker.seed(42)
observers = []

for _ in range(n_observers):
    observers.append((fake.email(), fake.name()))

# Faker.seed(3)
attorney_names = []

for _ in range(n_attorneys):
    attorney_names.append(fake.name())

empty_attorneys = list(itertools.repeat(None, n_no_attorneys))
attorney_names.extend(empty_attorneys)

form_cols = { "Timestamp" : []
             , "Username" : []
             , "Name" : []
             , "Email" : []
             , "Phone Number" : []
             , "Date" : []
             , "Time Start" : []
             , "Court Room Number" : []
             , "Judge Name 1" : []
             , "Judge Name 2" : []
             , "Notes" : []
             , "Attorneys Present" : []
             , "The judge was impartial" : []
             , "Explanation" : []
             , "The judge was professional" : []
             , "Explanation.1" : []
             , "The judge was rational" : []
             , "Explanation.2" : []
             , "The judge was compassionate" : []
             , "Explanation.3" : []
             , "The judge was respectful" : []
             , "Explanation.4" : []
             , "The judge was unbiased" : []
             , "Explanation.5" : []
             , "The judge was patient" : []
             , "Explanation.6" : []
             , "The judge was audible" : []
             , "Explanation.7" : []
             , "The judge was intelligible" : []
             , "Explanation.8" : []
             , "The judge's questions were relevant" : []
             , "Explanation.9" : []
             , "The judge's decision was understandable" : []
             , "Explanation.10" : []
             , "The judge was considerate" : []
             , "Explanation.11" : []
             , "The judge was punctual" : []
             , "Explanation.12" : []
             , "The judge was attentive" : []
             , "Explanation.13" : []
             , "The judge was prepared" : []
             , "Explanation.14" : []
             , "The judge was authoritative" : []
             , "Explanation.15" : []
             , "Is there anything else you wish to address?" : []
             , "Unnamed: 45": []
              }

def make_observations():
    start_times = ["9:00:00"
                           , "10:00:00"
                           , "10:30:00"
                           , "12:00:00"
                           , "9:30:00"
                           , "9:30:00"
                           , "9:30:00"
                           , "11:00:00"
                           , "12:30:00"
                           , "12:30:00"
                           , "12:30:00"
                           ]
    court_rooms = [
                  "Chicago Courtroom 100"
                , "Chicago Courtroom 100"
                , "Chicago Courtroom 100"
                , "Chicago Courtroom 100"
                , "Chicago Courtroom 100"
                , "Chicago Courtroom 100"
                , "Chicago Courtroom 100"
                , "Chicago Courtroom 100"
                , "Chicago Courtroom 100"
                , "Chicago Courtroom 100"
                , "Chicago Courtroom 100"
                , "Chicago Courtroom 100"
                , "Chicago Courtroom 100"
                , "Chicago Courtroom 100"
                , "Chicago Courtroom 100"
                , "Chicago Courtroom 100"
                , "Chicago Courtroom 100"
                , "Chicago Courtroom 100"
                , "Chicago Courtroom 100"
                , "Chicago Courtroom 100"
                , "Chicago Courtroom 100"
                , "Chicago Courtroom 100"
                , "Chicago Courtroom 100"
                , "Chicago Courtroom 100"
                , "Chicago Courtroom 100"
                , "Chicago Courtroom 100"
                , "Chicago Courtroom 100"
                , "Chicago Courtroom 100"
                , "Chicago Courtroom 100"
                , "Chicago Courtroom 100"
                , "Chicago Courtroom 100"
                , "Chicago Courtroom 100"
                , "Chicago Courtroom 100"
                , "Chicago Courtroom 100"
                , "Chicago Courtroom 100"
                , "Chicago Courtroom 100"
                , "Chicago Courtroom 100"
                , "Chicago Courtroom 100"
                , "Chicago Courtroom 100"
                , "Chicago Courtroom 100"
                , "Chicago Courtroom 100"
                , "Chicago Courtroom 100"
                , "Chicago Courtroom 100"
                , "Chicago Courtroom 100"
                , "Chicago Courtroom 100"
                , "Chicago Courtroom 101"
                , "Chicago Courtroom 102"
                , "Chicago Courtroom 102"
                , "Chicago Courtroom 102"
                , "Chicago Courtroom 102"
                , "Chicago Courtroom 102"
                , "Chicago Courtroom 102"
                , "Chicago Courtroom 102"
                , "Chicago Courtroom 102"
                , "Chicago Courtroom 202"
                , "Chicago Courtroom 203"
                , "Chicago Courtroom 204"
                , "Chicago Courtroom 205"
                , "Chicago Courtroom 205"
                , "Chicago Courtroom 205"
                , "Chicago Courtroom 205"
                , "Chicago Courtroom 206"
                , "Chicago Courtroom 208"
                , "Chicago Courtroom 3A15"
                , "Chicago Courtroom 301"
                , "Chicago Courtroom 302"
                , "Chicago Courtroom 304"
                , "Chicago Courtroom 305"
                , "Chicago Courtroom 306"
                , "Chicago Courtroom 307"
                , "Chicago Courtroom 308"
                , "Chicago Courtroom 400"
                , "Chicago Courtroom 404"
                , "Chicago Courtroom 500"
                , "Chicago Courtroom 502"
                , "Chicago Courtroom 504"
                , "Chicago Courtroom 506"
                , "Chicago Courtroom 600"
                , "Chicago Courtroom 602"
                , "Chicago Courtroom 604"
                , "Chicago Courtroom 606"
                , "Chicago Courtroom 700"
                , "Chicago Courtroom 700"
                , "Chicago Courtroom 700"
                , "Chicago Courtroom 700"
                , "Chicago Courtroom 700"
                , "Chicago Courtroom 702"
                , "Chicago Courtroom 704"
                , "Chicago Courtroom 706"
                , "Bridgeview Courtroom 101"
                , "Bridgeview Courtroom 103"
                , "Markham Courtroom 101"
                   ]

    data = form_cols.copy()

    evaluated_fields = ["The judge was impartial"
                        , "The judge was professional"
                        , "The judge was rational"
                        , "The judge was compassionate"
                        , "The judge was respectful"
                        , "The judge was unbiased"
                        , "The judge was patient"
                        , "The judge was audible"
                        , "The judge was intelligible"
                        , "The judge's questions were relevant"
                        , "The judge's decision was understandable"
                        , "The judge was considerate"
                        , "The judge was punctual"
                        , "The judge was attentive"
                        , "The judge was prepared"
                        , "The judge was authoritative"
                        ]

    empty_fields = list(data.keys())

    for i in evaluated_fields:
        empty_fields.remove(i)

    data_fields = ['Timestamp'
                    , 'Username'
                    , 'Name'
                    , 'Email'
                    , 'Time Start'
                    , 'Court Room Number'
                    , 'Attorneys Present'
                    , 'Judge Name 1'
                    , 'Date'
                    , 'Is there anything else you wish to address?'
                   ]

    for i in data_fields:
        empty_fields.remove(i)

    empty_list = list(itertools.repeat(None, n_observations))

    def make_fake_text():
        return fake.paragraph(nb_sentences=1)

    random_text = [None, make_fake_text, None, None]

    counter = 0
    for i in range(n_observations):
        counter += 1
        court_room = random.choice(court_rooms)
        name, email = random.choice(observers)
        judge_name = random.choice(judge_names)
        attorney_name = random.choice(attorney_names)
        date_timestamp, timestamp, date_string = make_random_date(start_times, court_room)
        random_notes = random.choice(random_text)

        for key, value in data.items():

            if key == 'Timestamp':
                value.append(date_timestamp)
            if key == 'Username':
                value.append(email)
            if key == 'Name':
                value.append(name)
            if key == 'Date':
                value.append(date_string)
            if key == 'Email':
                value.append(email)
            if key == 'Time Start':
                value.append(timestamp)
            if key == 'Court Room Number':
                value.append(court_room)
            if key == 'Attorneys Present':
                value.append(attorney_name)
            if key == 'Judge Name 1':
                value.append(judge_name)
            if key == 'Is there anything else you wish to address?':
                if random_notes is not None:
                    text = random_notes()
                    value.append(text)
                else:
                    value.append(random_notes)
            if key in evaluated_fields:
                value.append(random.choice(responses))

        for key, value in data.items():
            if not value:
                value.extend(empty_list)

    return data


def make_form_data():

    fake_data = make_observations()

    df = pd.DataFrame.from_dict(fake_data)

    print(df.head())
    df.to_csv('data/observation_forms_2.csv', index=False)

    

    




    






