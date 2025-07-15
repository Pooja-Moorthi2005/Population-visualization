import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset
file_path = 'C:/Users/Sys/Downloads/population_2020_sample.csv'  # Make sure this matches your file name
data = pd.read_csv(file_path)

# Step 2: Sort and get top 10 countries by population
top10 = data.sort_values(by='Population_2020', ascending=False).head(10)

# Step 3: Create a Bar Chart
plt.figure(figsize=(12, 6))
plt.bar(top10['Country'], top10['Population_2020'], color='skyblue')
plt.title('Top 10 Most Populous Countries in 2020')
plt.xlabel('Country')
plt.ylabel('Population')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

