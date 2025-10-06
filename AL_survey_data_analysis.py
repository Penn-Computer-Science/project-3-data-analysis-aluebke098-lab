import pandas as pd
import matplotlib as plt

df = pd.read_csv("survey_data.csv")
survey_data = pd.DataFrame(df)

# print("-_"*20)
# print(survey_data.info())

# print("-_"*20)
# print(survey_data.head().info())

print("-_"*20)
print("Summary")
print(round(survey_data.describe()))

print("-_"*20)
print("Head")
print(survey_data.head())

# print("-_"*20)
# print("Summary Head")
# print(round(survey_data.head().describe()))

print("-_"*20)
print("Tail")
print(survey_data.tail())

# print("-_"*20)
# print("Summary Tail")
# print(round(survey_data.tail().describe()))

# print("-_"*20)
# print(survey_data["Mood at School"].value_counts())

print("-_"*20)
print("Average GPA by Mood")
GPA_mood = survey_data.groupby("Mood at School")["GPA"].mean()
print(round(GPA_mood)) #bar

# print("-_"*20)
# print("Real Survey Data Set")
# print(survey_data.iloc[0:6])

print("-_"*20)
print("GPA by Hours of Sleep")
GPA_sleep = survey_data.groupby("Hours Slept")["GPA"]
print(GPA_sleep) #scatterplot

print("-_"*20)
print("GPA by Hours on Screens")
GPA_screens = survey_data.groupby("Hours on Screens")["GPA"]
print(GPA_screens) #scatterplot

print("-_"*20)
print("Average GPA by Favorite Subject")
GPA_subject = survey_data.groupby("Favorite Subject")["GPA"].mean()
print(round(GPA_subject)) #bar

print("-_"*20)
print("Overall GPA") 
GPA = survey_data["GPA"]
print(GPA) #box

# graphs all down here

survey_data["GPA"].plot(kind='hist',bins=5,edgecolor='black')
# plt.show()