#%% md
# #  Python project - Student Sleep Patterns
#%% md
# ### Hypothesis
#%% md
# My assumption - the quality of sleep of students depends on students' hours of study, sleep duration, physical activity and screen time
#%% md
# dataset is taken from - https://www.kaggle.com/datasets/arsalanjamal002/student-sleep-patterns/data
#%% md
# ### Importing libraries
#%%
import pandas as pd #helps to analyse and change the dataset
import matplotlib.pyplot as plt #makes a visualization
import seaborn as sns #makes a visualization
#%%
df = pd.read_csv('data/student_sleep_patterns.csv') #data account
#%% md
# ### Describing the main details of dataset
#%%
df.info() #overall information
#%%
df.head #investigating the first five rows of our dataset
#%% md
# ### Checking for rows with NaN and transformation of data set
#%%
df.isna().sum() #checking for rows with NaN
#%% md
# deleting unnecessary columns for our hypothesis(it doesn't need any info about students' age, gender etc.)
#%%
del df['Weekday_Sleep_Start']
del df['Weekday_Sleep_End']
del df['Weekend_Sleep_Start']
del df['Weekend_Sleep_End']
del df['Age']
del df['Gender']
del df['University_Year']
#%%
df.head() #investigating the first five rows of our dataset
#%% md
# transformation data from hours to minutes (all elements of columns, besides the physical activity one, are in amount of hours), creating the new column - free time and assuming that it can influence on quality of students' sleep
#%%
df['Sleep_Duration'] = df['Sleep_Duration'] * 60
df['Study_Hours'] = df['Study_Hours'] * 60
df = df.rename(columns={'Study_Hours': 'Study_Time'})
df['Screen_Time'] = df['Screen_Time'] * 60
df['Free_Time'] = (24 * 60) - (df['Physical_Activity'] + df['Screen_Time'] + df['Sleep_Duration'] + df['Study_Time'])
df.head()
#%% md
# finding incorrect data for our following analysis (where sum of hours of study, duration of sleep, time of physical activity and screen time more than 24 hours or 1440 minutes, so free time is less than 0)
#%%
df.describe().round(2) # brief description with rounding
#%% md
# finding the amount of such "incorrect" rows and observing that they are only 5, so deleting of them won't harm the quality of our analysis
#%%
print(df[df['Free_Time'] < 0])
#%% md
# deleting such columns
#%%
df = df[df['Free_Time'] >= 0]
df.head()
#%% md
# ### Creation of plots
#%% md
# investigation how many minutes students spend on each activity students spend
#%%
plt.figure(figsize=(20,5)) #defining the size of plot
sns.boxplot(df[["Sleep_Duration", "Study_Time", "Screen_Time", 'Free_Time']]) #making the plot, which shows us the range of values etc.
#%% md
# comparison of sleep duration and quality of sleep (there is no such big and obvious dependence, so it's not important parameter)
#%%
plt.figure(figsize=(15,8)) #defining the size of plot

sns.violinplot(df, x="Sleep_Duration", hue="Sleep_Quality",palette="pastel")#creating the plot, which helps to observe the distribution of numeric data
#%% md
# comparison of amount of study time and quality of sleep (there is no such big and obvious dependence)
#%%
plt.figure(figsize=(10, 6)) #defining the size of plot
plt.bar(df['Sleep_Quality'], df['Study_Time'], color='skyblue') #x, y - columns for creating the plot
plt.title('Comparison between amount of study time and quality of sleep', fontsize=14) # heading of the plot
plt.xlabel('Quality of sleep', fontsize=12) #creating the name and size of it for x
plt.ylabel('Study time', fontsize=12) #creating the name and size of it for y
plt.show() #showing the plot
#%% raw
# comparision of amount of free time and quality of sleep (there is no such big and obvious dependance)
#%%
plt.figure(figsize=(15,8))#defining the size of plot

sns.violinplot(df, x="Free_Time", hue="Sleep_Quality",palette="pastel") #creating the plot to find any dependence
#%% md
# comparison between caffeine intake and quality of sleep (there is no such big and obvious dependence)
#%%
plt.figure(figsize=(10, 6))
sns.boxplot(x='Caffeine_Intake', y='Sleep_Quality', data=df)
plt.title('Comparison between caffeine intake and quality of sleep')
plt.xlabel('Caffeine intake')
plt.ylabel('Sleep quality')
plt.grid(True)#creating of net
plt.show()
#%% md
# comparison between physical activity and quality of sleep (there is no such big and obvious dependence)
#%%
plt.figure(figsize=(10, 6))
sns.lineplot(x='Physical_Activity', y='Sleep_Quality', data=df, marker='o', color='blue', errorbar=None) #last - delete the range of other points
plt.title('Comparison between physical activity and quality of sleep')
plt.xlabel('Physical activity')
plt.ylabel('Sleep quality')
plt.grid(True)
plt.show()
#%% md
# comparison between screen time and quality of sleep (there is no such big and obvious dependence)
#%%
plt.figure(figsize=(10, 6))
sns.lineplot(x='Screen_Time', y='Sleep_Quality', data=df, marker="o", color='blue')
plt.title('Comparison between screen time and quality of sleep')
plt.xlabel('Time of screen')
plt.ylabel('Sleep quality')
plt.grid(True)
plt.show()
#%% md
# comparison between study time and screen time, which can influence on quality of sleep (there is no such big and obvious dependence)
#%%
sns.pairplot(df[['Study_Time','Sleep_Quality', 'Screen_Time']],hue="Sleep_Quality",palette="pastel")
#%% md
# visualisation of how quality of sleep depends on different time spending, there is no such a big correlation to prove our hypothesis
#%%
plt.figure(figsize=(10, 8))
df[['Sleep_Quality', 'Sleep_Duration', 'Study_Time', 'Screen_Time', 'Free_Time']].groupby('Sleep_Quality').mean().plot(kind='barh', stacked=True, alpha=0.9, colormap='Set3', figsize=(12, 8))
plt.title('Influence of different parameters with Sleep Quality', fontsize=16)
plt.xlabel('Mean Values of parameters', fontsize=12)
plt.ylabel('Sleep Quality', fontsize=12)
plt.legend(title='Parameters', bbox_to_anchor=(1.05, 1), loc='upper left') #creating the colours and lists of parameters for comparison
plt.grid(axis='x', linestyle='-', alpha=0.6) #creating the line for each 200
plt.tight_layout()
plt.show()
#%% md
# correlation heatmap, which shows that correlation is too small to say that different factors affects to quality of sleep
#%%
corr = df[['Sleep_Duration', 'Study_Time', 'Screen_Time', 'Caffeine_Intake', 'Physical_Activity', 'Sleep_Quality', 'Free_Time']].corr()
plt.figure(figsize=(10, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()
#%% md
# ### Conclusion
#%% md
# Our hypothesis is disproved, as there is not such a big correlation between factors and their relation to quality of sleep to make any decisions.
