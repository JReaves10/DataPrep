import pandas as pd

# Read in customer_train.csv
ds_jobs = pd.read_csv("customer_train.csv")
ds_jobs_clean = ds_jobs.copy()


# Change data types
ordered_cat = {
    'relevant_experience': ['No relevant experience', 'Has relevant experience'],
    'enrolled_university': ['no_enrollment', 'Part time course', 'Full time course'],
    'education_level': ['Primary School', 'High School', 'Graduate', 'Masters', 'Phd'],
    'experience': ['<1'] + list(map(str, range(1, 21))) + ['>20'],
    'company_size': ['<10', '10-49', '50-99', '100-499', '500-999', '1000-4999', '5000-9999', '10000+'],
    'last_new_job': ['never', '1', '2', '3', '4', '>4']
}

# Filter and change the data types
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

# Filter for students with 10 or more experience and companies with at least 1000 employees.
ds_jobs_clean = ds_jobs_clean[(ds_jobs_clean['experience'] >= '10') & (ds_jobs_clean['company_size'] >= '1000-4999')]

ds_jobs.info()
ds_jobs_clean.info()