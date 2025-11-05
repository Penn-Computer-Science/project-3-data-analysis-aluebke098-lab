import pandas as pd
import random

hour_sleep = []
subject = ["Math", "Math", "Math", "CS", "History", "English", "Science", 
           "Art", "Music", "Engineering"]
mood = ["Bored", "Bored", "Tired", "Tired", "Busy", "Mundane"]

for i in range(20):
    hour_sleep.append(random.randint(5,10))

junk_data = {
    "Hours Slept": hour_sleep,
    "Hours on Screens": [random.randint(1,10) for _ in hour_sleep],
    "Favorite Subject": [random.choice(subject) for _ in hour_sleep],
    "Mood at School": [random.choice(mood) for _ in hour_sleep],
    "GPA": [round(random.uniform(2.3,4.3),1) for _ in hour_sleep]
}

df = pd.DataFrame(junk_data)
df.to_csv("survey_data.csv", index = False)