import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("survey_data.csv")
survey_data = pd.DataFrame(df)

# print("-_"*20)
# print(survey_data.info())

# print("-_"*20)
# print(survey_data.head().info())

print("-_"*20)
print("Summary")
print(survey_data.describe())

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

# print("-_"*20)
# print("Average GPA by Mood")
# print(round(survey_data.groupby("Mood at School")["GPA"].mean())) #bar

# # print("-_"*20)
# # print("Real Survey Data Set")
# # print(survey_data.iloc[0:6])

# print("-_"*20)
# print("GPA by Hours of Sleep")
# print(survey_data.groupby("Hours Slept")["GPA"]) #scatterplot

# print("-_"*20)
# print("GPA by Hours on Screens")
# print(survey_data.groupby("Hours on Screens")["GPA"]) #scatterplot

# print("-_"*20)
# print("Average GPA by Favorite Subject")
# print(round(survey_data.groupby("Favorite Subject")["GPA"].mean())) #bar

# print("-_"*20)
# print("Overall GPA") 
# print(survey_data["GPA"]) #box/hist

# graphs all down here

survey_data["GPA"].plot(kind='box')
plt.show()

survey_data.groupby("Mood at School")["GPA"].mean().plot(kind='bar', color='red')
plt.ylabel("GPA")
plt.show()

survey_data.groupby("Favorite Subject")["GPA"].mean().plot(kind='bar', color='green')
plt.ylabel("GPA")
plt.show()

plt.scatter(survey_data["Hours Slept"],survey_data["GPA"], color='orange')
plt.xlabel("Hours of Sleep")
plt.ylabel("GPA")
plt.show()

plt.scatter(survey_data["Hours on Screens"], survey_data["GPA"], color='purple')
plt.xlabel("Hours on Screens")
plt.ylabel("GPA")
plt.show()