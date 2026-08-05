import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Folder banane ke liye
os.makedirs('output/graphs', exist_ok=True)

# 1. CSV ko read karna
df = pd.read_csv('data/Students.csv')

print("Data loaded. Shape:", df.shape)

# 2. Total aur Percentage nikalna - G1,G2,G3 ke liye
subject_columns = ['G1', 'G2', 'G3']
df['Total'] = df[subject_columns].sum(axis=1)
df['Percentage'] = (df['Total'] / (len(subject_columns)*20)) * 100  # har subject 20 me se hai
df['Pass_Fail'] = df['G3'].apply(lambda x: 'Pass' if x >= 10 else 'Fail')

# Graph ka style set
sns.set_style("whitegrid")

# ===== GRAPH 1: Gender vs Avg Percentage =====
plt.figure(figsize=(8,5))
sns.barplot(x='sex', y='Percentage', data=df, estimator='mean', palette='Set2')
plt.title('1. Gender vs Average Percentage')
plt.xlabel('Gender - F:Female, M:Male')
plt.ylabel('Average %')
plt.savefig('output/graphs/1_gender_avg.png')
plt.close()

# ===== GRAPH 2: Top 15 Students =====
top15 = df.sort_values('Percentage', ascending=False).head(15)
top15['Student'] = 'S_' + top15.index.astype(str)
plt.figure(figsize=(12,6))
sns.barplot(x='Student', y='Percentage', data=top15, palette='viridis')
plt.title('2. Top 15 Students by Percentage')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('output/graphs/2_top15_students.png')
plt.close()

# ===== GRAPH 3: Study Time vs Final Grade G3 =====
plt.figure(figsize=(8,5))
sns.boxplot(x='studytime', y='G3', data=df, palette='Blues')
plt.title('3. Study Time vs Final Grade G3')
plt.xlabel('Study Time 1:Low to 4:High')
plt.ylabel('Final Grade G3')
plt.savefig('output/graphs/3_studytime_vs_G3.png')
plt.close()

# ===== GRAPH 4: Parents Education vs Avg G3 =====
plt.figure(figsize=(10,5))
df_medu = df.groupby('Medu')['G3'].mean().reset_index()
sns.barplot(x='Medu', y='G3', data=df_medu, palette='Greens')
plt.title('4. Mother Education Level vs Avg Final Grade')
plt.xlabel('Mother Education 0:None to 4:High')
plt.ylabel('Average G3')
plt.savefig('output/graphs/4_medu_vs_G3.png')
plt.close()

# ===== GRAPH 5: Internet Access vs Pass/Fail =====
plt.figure(figsize=(8,5))
sns.countplot(x='internet', hue='Pass_Fail', data=df, palette='coolwarm')
plt.title('5. Internet Access vs Pass/Fail')
plt.xlabel('Internet - yes/no')
plt.ylabel('Count of Students')
plt.savefig('output/graphs/5_internet_passfail.png')
plt.close()

# ===== GRAPH 6: Alcohol Consumption vs G3 =====
plt.figure(figsize=(10,5))
sns.boxplot(x='Dalc', y='G3', data=df, palette='Reds')
plt.title('6. Workday Alcohol vs Final Grade')
plt.xlabel('Workday Alcohol 1:Very Low to 5:Very High')
plt.ylabel('Final Grade G3')
plt.savefig('output/graphs/6_alcohol_vs_G3.png')
plt.close()

# ===== GRAPH 7: School Support vs Avg Percentage =====
plt.figure(figsize=(8,5))
sns.barplot(x='schoolsup', y='Percentage', data=df, estimator='mean', palette='Pastel1')
plt.title('7. School Support vs Average Percentage')
plt.xlabel('School Support - yes/no')
plt.ylabel('Average %')
plt.savefig('output/graphs/7_schoolsup_avg.png')
plt.close()

# ===== GRAPH 8: Absences vs G3 Scatter =====
plt.figure(figsize=(8,5))
sns.scatterplot(x='absences', y='G3', data=df, hue='sex', alpha=0.6)
plt.title('8. Absences vs Final Grade')
plt.xlabel('Number of Absences')
plt.ylabel('Final Grade G3')
plt.savefig('output/graphs/8_absences_vs_G3.png')
plt.close()

# ===== GRAPH 9: Reason for School vs Avg G3 =====
plt.figure(figsize=(10,5))
df_reason = df.groupby('reason')['G3'].mean().reset_index()
sns.barplot(x='reason', y='G3', data=df_reason, palette='mako')
plt.title('9. Reason for Choosing School vs Avg Final Grade')
plt.xlabel('Reason')
plt.ylabel('Average G3')
plt.savefig('output/graphs/9_reason_vs_G3.png')
plt.close()

# ===== GRAPH 10: Correlation Heatmap =====
plt.figure(figsize=(12,8))
corr_cols = ['age', 'studytime', 'failures', 'absences', 'G1', 'G2', 'G3', 'Percentage']
sns.heatmap(df[corr_cols].corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('10. Correlation Heatmap - Marks, Study, Absences')
plt.tight_layout()
plt.savefig('output/graphs/10_correlation_heatmap.png')
plt.close()

print("Done! 10 Graph 'output/graphs' folder me save ho gaye")