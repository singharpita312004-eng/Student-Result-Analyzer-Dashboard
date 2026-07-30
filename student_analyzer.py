import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 1. CSV ko read karna
df = pd.read_csv('data/Students.csv')

print(df.head()) # check karne ke liye
print(df.columns.tolist()) # saare column naam

# 2. Total aur Percentage nikalna - tere dataset me ye 4 subject hain
subject_columns = ['english.grade', 'math.grade', 'sciences.grade', 'language.grade']
df['Total'] = df[subject_columns].sum(axis=1)
df['Percentage'] = (df['Total'] / (len(subject_columns)*5)) * 100  # har subject 5 me se hai

# 3. GRAPH 1: Gender wise Avg Percentage
plt.figure(figsize=(8,5))
sns.barplot(x='gender', y='Percentage', data=df)
plt.title('Gender vs Average Percentage')
plt.savefig('output/graphs/gender_avg.png')
plt.show()

# 4. GRAPH 2: Top 10 Students by Percentage
top10 = df.sort_values('Percentage', ascending=False).head(10)
plt.figure(figsize=(10,6))
sns.barplot(x='name', y='Percentage', data=top10)
plt.xticks(rotation=45)
plt.title('Top 10 Students')
plt.tight_layout()
plt.savefig('output/graphs/top10_students.png')
plt.show()

print("Done! Graph 'output/graphs' folder me save ho gaye")