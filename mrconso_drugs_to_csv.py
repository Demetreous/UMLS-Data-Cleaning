# Author: Demetreous Stillman, Zergio Ruvalcaba

# Libraries
import pandas as pd
import csv

#Prompt user for path to MRCONSO File
file_path = input("Please enter the path to the MRCONSO file: ")

# Imports MRCONSO Table and adds column names
column_names = ['CUI', 'LAT', 'TS', 'LUI', 'STT', 'SUI', 'ISPREF', 'AUI', 'SAUI', 'SCUI', 'SDUI', 'SAB', 'TTY', 'CODE', 'STR', 'SRL', 'SUPPRESS', 'CVF']
rrf_data = pd.read_csv(file_path, header = None, sep = '|', low_memory = False, names = column_names, index_col = False)

# Filter rows where SAB indicates drug-related entries
drug_sources = ['RXNORM']

# Create df for drugs only
drug_df = rrf_data[rrf_data['SAB'].isin(drug_sources)]
drug_df.reset_index(drop=True, inplace=True)

# Drop all columns except for drug name
columns_to_keep = ['STR']
drug_df = drug_df[columns_to_keep]

# Keep only unique values in the 'STR' column
unique_values = drug_df['STR'].unique()

# Create a new dataframe with the unique values
unique_df = pd.DataFrame({'DRUGS': unique_values})

#turn df into dict
drug_dict = unique_df['DRUGS'].to_dict()

#Prompt user to choose program function 
print("\nChoose an option. Option 1 will extract all drug names and store them in a CSV file. \nOption 2 returns a random drug name. \nOption 3 asks for an index input and returns drug with corresponding index.")
print("\t1. Output Unique Drug Names to CSV")
print("\t2. Return Random Drug Name")
print("\t3. Return Drug with Specified Index")
action = int(input("Choice: "))

if (action == 1):
    file_name = "MRCONSO_Drugs.csv"
    csv_header = "Drugs"
    unique_df.to_csv(file_name, index=False, header = csv_header)
    print(f"Drugs have been exported to {file_name}")
elif (action == 2):
    random_drug = unique_df['DRUGS'].sample(n=1).iloc[0]
    print(random_drug)
        
elif (action == 3):
    indx = int(input("Enter a number in the range 0-303046: "))
    print(drug_dict[indx])
    
else:
    print("Not a valid option. Goodbye!")