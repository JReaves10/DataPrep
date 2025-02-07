# Data Preprocessing for Efficient Storage of Customer Data

This project aims to transform the **customer_train.csv** dataset for **Training Data Ltd**. in order to optimize memory usage while preserving data integrity and usability. The transformation adheres to specific data storage requirements outlined by the Head Data Scientist.

# Objectives

### 1. Data Type Optimization:
- Convert columns with only two factors to **bool**.
- Store integer-only columns as 32-bit integers (**int32**).
- Store float columns as 16-bit floats (**float16**).
- Convert nominal categorical columns to the **category** data type.
- Convert ordinal categorical columns to **ordered categories**.

### 2. Data Filtering:
- Retain only students with **10 or more** years of experience.
- Include only companies with **1000 or more** employees.

# Dataset Description
- **relevant_experience**: Indicates if the student has relevant work experience.
- **enrolled_university**: Type of university enrollment (no enrollment, part-time, or full-time).
- **education_level**: Highest education level attained.
- **experience**: Years of professional experience.
- **company_size**: Size of the current company.
- **last_new_job**: Time since the last job change.

# Installation
Clone this repository and install the necessary libraries if required.

!(
# Code Explanation
### 1. Reading the Data
Load the dataset using pandas.read_csv() and create a copy for transformation.

import pandas as pd
# Read in customer_train.csv
ds_jobs = pd.read_csv("customer_train.csv")
ds_jobs_clean = ds_jobs.copy()

### 2. Defining Ordered Categories
Specify the natural order for categorical columns that require ordering.

ordered_cat = {
    'relevant_experience': ['No relevant experience', 'Has relevant experience'],
    'enrolled_university': ['no_enrollment', 'Part time course', 'Full time course'],
    'education_level': ['Primary School', 'High School', 'Graduate', 'Masters', 'Phd'],
    'experience': ['<1'] + list(map(str, range(1, 21))) + ['>20'],
    'company_size': ['<10', '10-49', '50-99', '100-499', '500-999', '1000-4999', '5000-9999', '10000+'],
    'last_new_job': ['never', '1', '2', '3', '4', '>4']
}

### 3. Data Type Optimization
Loop through columns and adjust data types based on content and requirements.

for col in ds_jobs_clean:
    if ds_jobs_clean[col].dtype == 'int':
        ds_jobs_clean[col] = ds_jobs_clean[col].astype('int32')
    elif ds_jobs_clean[col].dtype == 'float':
        ds_jobs_clean[col] = ds_jobs_clean[col].astype('float16')
    elif col in ordered_cat.keys():
        category = pd.CategoricalDtype(ordered_cat[col], ordered=True)
        ds_jobs_clean[col] = ds_jobs_clean[col].astype(category)
    else:
        ds_jobs_clean[col] = ds_jobs_clean[col].astype('category')

### 4. Data Filtering
Apply conditions to retain relevant records.

# Filter for students with 10 or more experience and companies with at least 1000 employees.
ds_jobs_clean = ds_jobs_clean[(ds_jobs_clean['experience'] >= '10') & (ds_jobs_clean['company_size'] >= '1000-4999')]

### 5. Memory Usage Comparison
Compare memory usage before and after transformation using .info().

# Display memory usage comparison
ds_jobs.info()
ds_jobs_clean.info()

# Results
By implementing these transformations, we achieved a substantial decrease in memory usage, making the dataset more efficient for analysis and modeling.

Example Output

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 19158 entries, 0 to 19157
Data columns (total 14 columns):
  ...
memory usage: 2.0+ MB

<class 'pandas.core.frame.DataFrame'>
Int64Index: 2201 entries, 9 to 19143
Data columns (total 14 columns):
  ...
memory usage: 76.1 KB

# Conclusion
This project showcases how thoughtful data preprocessing and type optimization can significantly enhance performance and efficiency in data science workflows.
