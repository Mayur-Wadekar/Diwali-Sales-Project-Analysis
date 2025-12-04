import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==============================================================================
# REMINDER: Update 'YOUR_ACTUAL_FILENAME.csv' with your file name.
# ==============================================================================
file_name = "Diwali Sales Data.csv" # <-- CHANGE THIS
data_folder = r"C:\Users\Admin\AppData\Local\Programs\Python\Python313\pythonprj"
file_path = f"{data_folder}\\{file_name}"

# Load dataset
try:
    df = pd.read_csv(file_path, encoding='unicode_escape')
except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
    print("Please check the file name and path.")
    exit()
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    exit()

# --- Data Cleaning and Preparation ---
print("--- Data Info & Cleaning ---")
# Drop unrelated/blank columns
cols_to_drop = ['Status', 'unnamed1']
df.drop(cols_to_drop, axis=1, inplace=True, errors='ignore')

# Drop rows with null values
df.dropna(inplace=True)
df.reset_index(drop=True, inplace=True)

# Convert 'Amount' to integer
df['Amount'] = df['Amount'].astype('int')

# --- Exploratory Data Analysis (EDA) ---
plt.style.use('seaborn-v0_8-darkgrid')

# 1. Gender vs Orders Count
plt.figure(figsize=(6, 4))
# FIX: Added hue='Gender' and legend=False
sns.countplot(x='Gender', data=df, hue='Gender', palette='viridis', legend=False)
plt.title('Customer Count by Gender')
plt.show()

# 2. Gender vs Amount (Total Sales)
gender_sales = df.groupby('Gender', as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
plt.figure(figsize=(6, 4))
# FIX: Added hue='Gender' and legend=False
sns.barplot(x='Gender', y='Amount', data=gender_sales, hue='Gender', palette='magma', legend=False)
plt.title('Total Sales Amount by Gender')
plt.ylabel('Total Amount (in Crores/Millions)')
plt.show()

# 3. Age Group vs Orders Count
plt.figure(figsize=(8, 5))
# FIX: Added hue='Age Group' and legend=False
sns.countplot(x='Age Group', data=df, order=df['Age Group'].value_counts().index, hue='Age Group', palette='Spectral', legend=False)
plt.title('Customer Count by Age Group')
plt.show()

# 4. Age Group vs Amount (Total Sales)
age_sales = df.groupby('Age Group', as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
plt.figure(figsize=(8, 5))
# FIX: Added hue='Age Group' and legend=False
sns.barplot(x='Age Group', y='Amount', data=age_sales, hue='Age Group', palette='Spectral', legend=False)
plt.title('Total Sales Amount by Age Group')
plt.ylabel('Total Amount')
plt.show()

# 5. Top 10 States by Orders (No Seaborn warning as it uses pandas plot)
state_orders = df.groupby('State')['Orders'].sum().nlargest(10).sort_values(ascending=False)
plt.figure(figsize=(12, 6))
state_orders.plot(kind='bar', color='skyblue')
plt.title('Top 10 States by Number of Orders')
plt.ylabel('Total Orders')
plt.xlabel('State')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# 6. Top 10 States by Amount (No Seaborn warning as it uses pandas plot)
state_amount = df.groupby('State')['Amount'].sum().nlargest(10).sort_values(ascending=False)
plt.figure(figsize=(12, 6))
state_amount.plot(kind='bar', color='darkorange')
plt.title('Top 10 States by Total Sales Amount')
plt.ylabel('Total Amount')
plt.xlabel('State')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# 7. Marital Status vs Orders Count
plt.figure(figsize=(6, 4))
# FIX: Added hue='Marital_Status' and legend=False
sns.countplot(x='Marital_Status', data=df, hue='Marital_Status', palette='Pastel1', legend=False)
plt.title('Customer Count by Marital Status')
plt.show()

# 8. Marital Status vs Amount
marital_amount = df.groupby('Marital_Status', as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
plt.figure(figsize=(6, 4))
# FIX: Added hue='Marital_Status' and legend=False
sns.barplot(x='Marital_Status', y='Amount', data=marital_amount, hue='Marital_Status', palette='Pastel1', legend=False)
plt.title('Total Sales Amount by Marital Status')
plt.ylabel('Total Amount')
plt.show()

# 9. Occupation vs Orders Count
plt.figure(figsize=(12, 6))
# FIX: Added hue='Occupation' and legend=False
sns.countplot(x='Occupation', data=df, order=df['Occupation'].value_counts().index, hue='Occupation', palette='cubehelix', legend=False)
plt.title('Customer Count by Occupation')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# 10. Occupation vs Amount (Total Sales)
occupation_amount = df.groupby('Occupation', as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
plt.figure(figsize=(12, 6))
# FIX: Added hue='Occupation' and legend=False
sns.barplot(x='Occupation', y='Amount', data=occupation_amount, hue='Occupation', palette='cubehelix', legend=False)
plt.title('Total Sales Amount by Occupation')
plt.ylabel('Total Amount')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# 11. Top 10 Product Category vs Orders Count
top_10_products = df['Product_Category'].value_counts().nlargest(10).index
plt.figure(figsize=(12, 6))
# FIX: Added hue='Product_Category' and legend=False
sns.countplot(x='Product_Category', data=df, order=top_10_products, hue='Product_Category', palette='tab10', legend=False)
plt.title('Top 10 Product Categories by Orders')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# 12. Top 10 Product Category vs Amount (Total Sales) (No Seaborn warning as it uses pandas plot)
product_sales = df.groupby('Product_Category')['Amount'].sum().nlargest(10).sort_values(ascending=False)
plt.figure(figsize=(12, 6))
product_sales.plot(kind='bar', color='teal')
plt.title('Top 10 Product Categories by Sales Amount')
plt.ylabel('Total Amount')
plt.xlabel('Product Category')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

print("\nAll warnings have been addressed and the code is ready.")
