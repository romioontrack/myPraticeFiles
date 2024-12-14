import pandas as pd
import seaborn as sns # type: ignore
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("C:/Users/Win11/Downloads/greendestination (1).csv")

# Calculate attrition rate
attrition_rate = df['Attrition'].value_counts(normalize=True).get('Yes', 0) * 100
print(f"Attrition Rate: {attrition_rate:.2f}%")

# EDA: Visualize attrition by age, years at company, and income
sns.histplot(data=df, x='Age', hue='Attrition', multiple='stack')
plt.title("Attrition Rate")
plt.xlabel('Age of Employees')
plt.ylabel('Number of Employees')
plt.show()

sns.histplot(data=df, x='YearsAtCompany', hue='Attrition', multiple='stack')
plt.title("Years at Company by Attrition")
plt.xlabel('Number of Year Employee worked for Company')
plt.ylabel('Number of Employee')
plt.show()

sns.histplot(data=df, x='Income', hue='Attrition', multiple='stack')
plt.title("Income Distribution by Attrition")
plt.show()
