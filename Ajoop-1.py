import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
df = pd.read_csv('D:/Ajoop/Ajoop-1.py')

# 1. Bar chart: Average GDP per region
plt.figure(figsize=(10, 6))
sns.barplot(x='Region', y='GDP_per_Capita', data=df, estimator='mean', palette='viridis')
plt.title('Average GDP per Capita by Region')
plt.ylabel('Average GDP per Capita')
plt.xlabel('Region')
plt.tight_layout()
plt.show()

# 2. Histogram: Population distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['Population_2020'], bins=20, kde=True, color='coral')
plt.title('Distribution of Population Across Countries (2020)')
plt.xlabel('Population')
plt.ylabel('Number of Countries')
plt.tight_layout()
plt.show()

# 3. Scatter plot: Population vs. GDP per Capita
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Population_2020', y='GDP_per_Capita', hue='Region', palette='Set2')
plt.title('Population vs. GDP per Capita by Region')
plt.xlabel('Population (2020)')
plt.ylabel('GDP per Capita')
plt.legend(title='Region')
plt.tight_layout()
plt.show()


