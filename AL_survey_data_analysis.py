import pandas as pd

df = pd.read_csv("survey_data.csv")
survey_data = pd.DataFrame(df)

print("-_"*20)
print(survey_data.head())

# print("-_"*20)
# print(survey_data.info())

# print("-_"*20)
# print(survey_data.head().info())

print("-_"*20)
print("Summary Total")
print(round(survey_data.describe()))

print("-_"*20)
print("Summary Head")
print(round(survey_data.head().describe()))

print("-_"*20)
print(survey_data["Mood at School"].value_counts())

print("-_"*20)
print("Average GPA by Mood")
print(round(survey_data.groupby("Mood at School")["GPA"].mean()))

print("-_"*20)
print("Real Survey Data Set")
print(survey_data.iloc[0:6])