
import pandas as pd

# Load the data
df = pd.read_csv('customer_support_data.csv')

# Basic stats
avg_resolution = df['Resolution Time (hrs)'].mean()
avg_satisfaction = df['Satisfaction Score'].mean()
issue_counts = df['Issue Type'].value_counts()
satisfaction_distribution = df['Satisfaction Score'].value_counts().sort_index()

# Output the analysis
print("Customer Support Analytics Report")
print("----------------------------------")
print(f"Average Resolution Time: {avg_resolution:.2f} hours")
print(f"Average Satisfaction Score: {avg_satisfaction:.2f} / 5")
print("
Issue Type Breakdown:")
print(issue_counts.to_string())
print("
Satisfaction Score Distribution:")
print(satisfaction_distribution.to_string())
