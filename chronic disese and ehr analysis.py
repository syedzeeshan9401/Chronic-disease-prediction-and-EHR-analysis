#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

df = pd.read_csv(r"C:\Users\essem\OneDrive\Desktop\Infotact data sets\Chronic disease and ehr analysis\patients.csv")

print(df.head())


# In[11]:


import pandas as pd

df = pd.read_csv(r"C:\Users\essem\OneDrive\Desktop\Infotact data sets\Chronic disease and ehr analysis\patients.csv")

print(df.columns.tolist())


# In[12]:


import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv(r"C:\Users\essem\OneDrive\Desktop\Infotact data sets\Chronic disease and ehr analysis\patients.csv")

# Count Male vs Female
gender_count = df['sex'].value_counts()

# Create graph
plt.figure(figsize=(6,5))
gender_count.plot(kind='bar')

# Labels and title
plt.title("Male vs Female Count")
plt.xlabel("Sex")
plt.ylabel("Count")

# Show values on bars
for i, value in enumerate(gender_count):
    plt.text(i, value + 1, str(value), ha='center')

# Show graph
plt.show()


# In[13]:


import pandas as pd
import matplotlib.pyplot as plt

# Read CSV
df = pd.read_csv(r"C:\Users\essem\OneDrive\Desktop\Infotact data sets\Chronic disease and ehr analysis\patients.csv")

# Scatter plot
plt.figure(figsize=(8,5))

plt.scatter(df['age'], df['bmi'])

plt.title("BMI by Age")
plt.xlabel("Age")
plt.ylabel("BMI")

plt.show()


# In[14]:


import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv(r"C:\Users\essem\OneDrive\Desktop\Infotact data sets\Chronic disease and ehr analysis\patients.csv")

# Create figure
plt.figure(figsize=(8,5))

# Plot Systolic BP vs Age
plt.scatter(df['age'], df['systolic_bp'], label='Systolic BP')

# Plot Diastolic BP vs Age
plt.scatter(df['age'], df['diastolic_bp'], label='Diastolic BP')

# Titles and labels
plt.title("Blood Pressure vs Age")
plt.xlabel("Age")
plt.ylabel("Blood Pressure")

# Show legend
plt.legend()

# Show graph
plt.show()


# In[15]:


import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv(r"C:\Users\essem\OneDrive\Desktop\Infotact data sets\Chronic disease and ehr analysis\patients.csv")

# Group data by age and calculate average BP
avg_bp = df.groupby('age')[['systolic_bp', 'diastolic_bp']].mean()

# Create line graph
plt.figure(figsize=(10,6))

plt.plot(avg_bp.index, avg_bp['systolic_bp'], marker='o', label='Systolic BP')
plt.plot(avg_bp.index, avg_bp['diastolic_bp'], marker='o', label='Diastolic BP')

# Titles and labels
plt.title("Average Blood Pressure by Age")
plt.xlabel("Age")
plt.ylabel("Blood Pressure")

# Show legend
plt.legend()

# Grid for better understanding
plt.grid(True)

# Show graph
plt.show()


# In[17]:


import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv(r"C:\Users\essem\OneDrive\Desktop\Infotact data sets\Chronic disease and ehr analysis\patients.csv")

# Create age groups
df['age_group'] = pd.cut(
    df['age'],
    bins=[0, 20, 30, 40, 50, 60, 70, 80, 100],
    labels=['0-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81+']
)

# Average heart rate by age group
heart_rate_avg = df.groupby('age_group', observed=False)['heart_rate'].mean()

# Plot graph
plt.figure(figsize=(10,6))

heart_rate_avg.plot(kind='bar')

plt.title("Average Heart Rate by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Average Heart Rate")

# Show values on bars
for i, value in enumerate(heart_rate_avg):
    plt.text(i, value + 0.5, round(value, 1), ha='center')

plt.show()


# In[19]:


import pandas as pd

# Read the medications CSV file
df = pd.read_csv(r"C:\Users\essem\OneDrive\Desktop\Infotact data sets\Chronic disease and ehr analysis\medications.csv")

# Show first 5 rows
print(df.head())

# Show column names
print(df.columns)

# Show dataset information
print(df.info())


# In[22]:


import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv(r"C:\Users\essem\OneDrive\Desktop\Infotact data sets\Chronic disease and ehr analysis\medications.csv")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Print columns to verify names
print(df.columns)

# Count patients taking each medication
med_counts = df['medication'].value_counts()

# Get counts for Aspirin and Ibuprofen
aspirin_count = med_counts.get('Aspirin', 0)
ibuprofen_count = med_counts.get('Ibuprofen', 0)

# Count all other medications together
others_count = med_counts.sum() - aspirin_count - ibuprofen_count

# Create labels and values
labels = ['Aspirin', 'Ibuprofen', 'Others']
values = [aspirin_count, ibuprofen_count, others_count]

# Create pie chart
plt.figure(figsize=(7,7))

plt.pie(values, labels=labels, autopct='%1.1f%%')

# Title
plt.title("Patients Taking Aspirin and Ibuprofen vs Others")

# Show graph
plt.show()


# In[24]:


import pandas as pd

# Read the lab results CSV file
df = pd.read_csv(r"C:\Users\essem\OneDrive\Desktop\Infotact data sets\Chronic disease and ehr analysis\lab_results.csv")

# Show first 5 rows
print(df.head())

# Show column names
print(df.columns.tolist())

# Show dataset information
print(df.info())


# In[27]:


import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv(r"C:\Users\essem\OneDrive\Desktop\Infotact data sets\Chronic disease and ehr analysis\lab_results.csv")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Print columns to verify names
print(df.columns)

# Filter rows where flag is High
high_flag = df[df['flag'] == 'high']

# Count high results for each test
test_counts = high_flag['test_name'].value_counts()

# Plot graph
plt.figure(figsize=(10,6))

test_counts.plot(kind='bar')

# Labels and title
plt.title("Test Names with high Flag")
plt.xlabel("Test Name")
plt.ylabel("Count of high Results")

# Show values on bars
for i, value in enumerate(test_counts):
    plt.text(i, value + 0.5, str(value), ha='center')

# Show graph
plt.xticks(rotation=45)
plt.show()


# In[28]:


import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# READ DATASETS
# -----------------------------
patients = pd.read_csv(r"C:\Users\essem\OneDrive\Desktop\Infotact data sets\Chronic disease and ehr analysis\patients.csv")

medications = pd.read_csv(r"C:\Users\essem\OneDrive\Desktop\Infotact data sets\Chronic disease and ehr analysis\medications.csv")

lab_results = pd.read_csv(r"C:\Users\essem\OneDrive\Desktop\Infotact data sets\Chronic disease and ehr analysis\lab_results.csv")

# Remove extra spaces from column names
patients.columns = patients.columns.str.strip()
medications.columns = medications.columns.str.strip()
lab_results.columns = lab_results.columns.str.strip()

# -----------------------------
# BASIC INFORMATION
# -----------------------------
print("\n PATIENTS DATASET")
print(patients.head())
print(patients.info())

print("\n MEDICATIONS DATASET")
print(medications.head())
print(medications.info())

print("\n LAB RESULTS DATASET")
print(lab_results.head())
print(lab_results.info())

# -----------------------------
# MISSING VALUES
# -----------------------------
print("\n Missing Values in Patients")
print(patients.isnull().sum())

print("\n Missing Values in Medications")
print(medications.isnull().sum())

print("\n Missing Values in Lab Results")
print(lab_results.isnull().sum())

# -----------------------------
# SEX DISTRIBUTION
# -----------------------------
plt.figure(figsize=(6,5))

patients['sex'].value_counts().plot(kind='bar')

plt.title("Male vs Female Patients")
plt.xlabel("Sex")
plt.ylabel("Count")

plt.show()

# -----------------------------
# AGE DISTRIBUTION
# -----------------------------
plt.figure(figsize=(8,5))

patients['age'].hist(bins=10)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Patients")

plt.show()

# -----------------------------
# BMI DISTRIBUTION
# -----------------------------
plt.figure(figsize=(8,5))

patients['bmi'].hist(bins=10)

plt.title("BMI Distribution")
plt.xlabel("BMI")
plt.ylabel("Count")

plt.show()

# -----------------------------
# BLOOD PRESSURE VS AGE
# -----------------------------
avg_bp = patients.groupby('age')[['systolic_bp', 'diastolic_bp']].mean()

plt.figure(figsize=(10,6))

plt.plot(avg_bp.index, avg_bp['systolic_bp'], marker='o', label='Systolic BP')
plt.plot(avg_bp.index, avg_bp['diastolic_bp'], marker='o', label='Diastolic BP')

plt.title("Average Blood Pressure by Age")
plt.xlabel("Age")
plt.ylabel("Blood Pressure")

plt.legend()
plt.grid(True)

plt.show()

# -----------------------------
# HEART RATE BY AGE GROUP
# -----------------------------
patients['age_group'] = pd.cut(
    patients['age'],
    bins=[0,20,30,40,50,60,70,80,100],
    labels=['0-20','21-30','31-40','41-50','51-60','61-70','71-80','81+']
)

heart_rate_avg = patients.groupby('age_group', observed=False)['heart_rate'].mean()

plt.figure(figsize=(10,6))

heart_rate_avg.plot(kind='bar')

plt.title("Average Heart Rate by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Heart Rate")

plt.show()

# -----------------------------
# TOP MEDICATIONS
# -----------------------------
print("\n Medication Columns:")
print(medications.columns)

# Replace 'medication' if your column name is different
med_col = medications.columns[1]

top_meds = medications[med_col].value_counts().head(10)

plt.figure(figsize=(10,6))

top_meds.plot(kind='bar')

plt.title("Top 10 Medications")
plt.xlabel("Medication")
plt.ylabel("Count")

plt.xticks(rotation=45)

plt.show()

# -----------------------------
# HIGH FLAG TESTS
# -----------------------------
print("\n Lab Result Columns:")
print(lab_results.columns)

# Convert flags to lowercase
lab_results['flag'] = lab_results['flag'].astype(str).str.lower()

high_flag = lab_results[lab_results['flag'] == 'high']

high_tests = high_flag['test_name'].value_counts()

plt.figure(figsize=(10,6))

high_tests.plot(kind='bar')

plt.title("Lab Tests with High Flag")
plt.xlabel("Test Name")
plt.ylabel("Count")

plt.xticks(rotation=45)

plt.show()

# -----------------------------
# INTERPRETATIONS
# -----------------------------
print("\n -------- EDA INTERPRETATIONS --------")

print("1. Sex distribution shows the number of male and female patients.")
print("2. Age distribution helps identify dominant age groups.")
print("3. BMI distribution indicates obesity or underweight trends.")
print("4. Blood pressure generally changes with age.")
print("5. Heart rate differs among age groups.")
print("6. Top medications indicate commonly prescribed drugs.")
print("7. High flag lab tests help identify abnormal test trends.")


# In[32]:


import pandas as pd
import matplotlib.pyplot as plt

# Read CSV
df = pd.read_csv(r"C:\Users\essem\OneDrive\Desktop\Infotact data sets\Chronic disease and ehr analysis\lab_results.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Print columns
print(df.columns.tolist())

# Convert to lowercase
df['test_name'] = df['test_name'].astype(str).str.lower()
df['flag'] = df['flag'].astype(str).str.lower()

# Filter high flags safely
high_results = df[df['flag'] == 'high'].copy()

# Disease prediction function
def predict_disease(test_name):

    if 'glucose' in test_name:
        return 'Possible Diabetes Risk'

    elif 'cholesterol' in test_name:
        return 'Possible Heart Disease Risk'

    elif 'creatinine' in test_name:
        return 'Possible Kidney Disease Risk'

    elif 'hba1c' in test_name:
        return 'Possible Diabetes Risk'

    elif 'triglyceride' in test_name:
        return 'Possible Cardiovascular Risk'

    elif 'ldl' in test_name:
        return 'Possible Heart Disease Risk'

    elif 'hdl' in test_name:
        return 'Possible Cholesterol Imbalance'

    else:
        return 'General Health Risk'

# Create prediction column
high_results['predicted_disease'] = high_results['test_name'].apply(predict_disease)

# Display predictions
print(high_results[['patient_id', 'test_name', 'predicted_disease']].head(20))

# Count disease predictions
disease_counts = high_results['predicted_disease'].value_counts()

# Plot graph
plt.figure(figsize=(10,6))

disease_counts.plot(kind='bar')

plt.title("Predicted Disease Risks from High Lab Results")
plt.xlabel("Disease Risk")
plt.ylabel("Number of Patients")

# Show values
for i, value in enumerate(disease_counts):
    plt.text(i, value + 0.5, str(value), ha='center')

plt.xticks(rotation=20)

plt.show()


# In[39]:


import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# READ FILES
# -----------------------------
lab_results = pd.read_csv(
    r"C:\Users\essem\OneDrive\Desktop\Infotact data sets\Chronic disease and ehr analysis\lab_results.csv"
)

medications = pd.read_csv(
    r"C:\Users\essem\OneDrive\Desktop\Infotact data sets\Chronic disease and ehr analysis\medications.csv"
)

# -----------------------------
# CLEAN COLUMN NAMES
# -----------------------------
lab_results.columns = lab_results.columns.str.strip()
medications.columns = medications.columns.str.strip()

# -----------------------------
# PRINT COLUMN NAMES
# -----------------------------
print("Lab Results Columns:")
print(lab_results.columns.tolist())

print("\nMedications Columns:")
print(medications.columns.tolist())

# -----------------------------
# CONVERT TO LOWERCASE
# -----------------------------
lab_results['test_name'] = lab_results['test_name'].astype(str).str.lower()
lab_results['flag'] = lab_results['flag'].astype(str).str.lower()

# -----------------------------
# FILTER HIGH RESULTS
# -----------------------------
high_results = lab_results[
    lab_results['flag'] == 'high'
].copy()

# -----------------------------
# DISEASE PREDICTION FUNCTION
# -----------------------------
def predict_disease(test_name):

    if 'glucose' in test_name:
        return 'Diabetes Risk'

    elif 'cholesterol' in test_name:
        return 'Heart Disease Risk'

    elif 'creatinine' in test_name:
        return 'Kidney Disease Risk'

    elif 'hba1c' in test_name:
        return 'Diabetes Risk'

    elif 'triglyceride' in test_name:
        return 'Cardiovascular Risk'

    elif 'ldl' in test_name:
        return 'Heart Disease Risk'

    elif 'hdl' in test_name:
        return 'Cholesterol Imbalance'

    else:
        return 'General Health Risk'

# -----------------------------
# PREDICT DISEASES
# -----------------------------
high_results['predicted_disease'] = high_results[
    'test_name'
].apply(predict_disease)

# -----------------------------
# TREATMENT RECOMMENDATIONS
# -----------------------------
def treatment_recommendation(disease):

    if disease == 'Diabetes Risk':
        return 'Metformin / Insulin Therapy'

    elif disease == 'Heart Disease Risk':
        return 'Statins / Aspirin / BP Control'

    elif disease == 'Kidney Disease Risk':
        return 'Creatinine Monitoring / Hydration Therapy'

    elif disease == 'Cardiovascular Risk':
        return 'Lifestyle Modification / Cardiac Monitoring'

    elif disease == 'Cholesterol Imbalance':
        return 'Cholesterol Lowering Drugs'

    else:
        return 'General Medical Consultation'

# -----------------------------
# DIET RECOMMENDATIONS
# -----------------------------
def diet_recommendation(disease):

    if disease == 'Diabetes Risk':
        return 'Low Sugar Diet'

    elif disease == 'Heart Disease Risk':
        return 'Low Fat Diet'

    elif disease == 'Kidney Disease Risk':
        return 'Low Sodium Diet'

    elif disease == 'Cardiovascular Risk':
        return 'Healthy Heart Diet'

    elif disease == 'Cholesterol Imbalance':
        return 'Healthy Cholesterol Diet'

    else:
        return 'Balanced Diet'

# -----------------------------
# APPLY RECOMMENDATIONS
# -----------------------------
high_results['treatment'] = high_results[
    'predicted_disease'
].apply(treatment_recommendation)

high_results['diet'] = high_results[
    'predicted_disease'
].apply(diet_recommendation)

# -----------------------------
# SHOW RESULTS
# -----------------------------
print("\nPREDICTED DISEASES WITH TREATMENT & DIET\n")

print(
    high_results[
        [
            'patient_id',
            'test_name',
            'predicted_disease',
            'treatment',
            'diet'
        ]
    ].head(20)
)

# -----------------------------
# GRAPH 1 - DISEASE COUNTS
# -----------------------------
disease_counts = high_results[
    'predicted_disease'
].value_counts()

plt.figure(figsize=(10,6))

disease_counts.plot(kind='bar')

plt.title("Predicted Diseases from Lab Results")
plt.xlabel("Disease")
plt.ylabel("Number of Patients")

for i, value in enumerate(disease_counts):
    plt.text(i, value + 0.5, str(value), ha='center')

plt.xticks(rotation=20)

plt.show()

# -----------------------------
# GRAPH 2 - TREATMENT COUNTS
# -----------------------------
treatment_counts = high_results[
    'treatment'
].value_counts()

plt.figure(figsize=(10,6))

treatment_counts.plot(kind='bar')

plt.title("Recommended Treatments")
plt.xlabel("Treatment")
plt.ylabel("Number of Patients")

for i, value in enumerate(treatment_counts):
    plt.text(i, value + 0.5, str(value), ha='center')

plt.xticks(rotation=20)

plt.show()

# -----------------------------
# GRAPH 3 - DIET COUNTS
# -----------------------------
diet_counts = high_results[
    'diet'
].value_counts()

plt.figure(figsize=(10,6))

diet_counts.plot(kind='bar')

plt.title("Recommended Diet Plans")
plt.xlabel("Diet")
plt.ylabel("Number of Patients")

for i, value in enumerate(diet_counts):
    plt.text(i, value + 0.5, str(value), ha='center')

plt.xticks(rotation=20)

plt.show()


# In[ ]:




