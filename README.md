# Diwali Sales Data Analysis

This project performs Exploratory Data Analysis (EDA) on the Diwali Sales dataset using Python. The goal is to understand customer behaviour, sales patterns, and top-performing product categories.

---

## Project Overview

The analysis covers:

* Data cleaning and preprocessing
* Gender-wise, age-wise and occupation-wise analysis
* State-wise sales and order insights
* Product category performance
* Visualizations using Matplotlib and Seaborn

---

## Dataset

File: **Diwali Sales Data.csv**
Default file path used in the script:

```
C:\Users\Admin\AppData\Local\Programs\Python\Python313\pythonprj\Diwali Sales Data.csv
```

Update the path if needed.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn

---

## How to Run

1. Install required libraries:

   ```
   pip install pandas numpy matplotlib seaborn
   ```
2. Ensure the CSV file is placed in the correct folder.
3. Run the script:

   ```
   python diwali_sales_analysis.py
   ```

---

## Data Cleaning

* Removed unwanted columns
* Dropped rows with missing values
* Converted Amount column to integer
* Reset dataset index

---

## Visualizations Generated

* Gender-based customer count and sales
* Age group distribution and spending
* State-wise top 10 orders and sales
* Marital status and occupation insights
* Top product categories by orders and sales

---

## Project Structure

```
/Diwali-Sales-Analysis
│── diwali_sales_analysis.py
│── Diwali Sales Data.csv
│── README.md

