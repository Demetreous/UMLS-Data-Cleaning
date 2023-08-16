# Author: Demetreous Stillman, Zergio Ruvalcaba
#This program takes in an RRF file 
# Libraries
import pandas as pd
import csv

#Prompt user for path to MRCONSO File
file_path = input("Please enter the path to the MRREL file: ")
print("Now attempting to process the file. This may take some time...")

# Imports MRCONSO Table and adds column names
column_names = ['CUI', 'LAT', 'TS', 'LUI', 'STT', 'SUI', 'ISPREF', 'AUI', 'SAUI', 'SCUI', 'SDUI', 'SAB', 'TTY', 'CODE', 'STR', 'SRL', 'SUPPRESS', 'CVF']
rrf_data = pd.read_csv(file_path, header = None, sep = '|', low_memory = False, names = column_names, index_col = False)

# Filter rows where SAB indicates disease-related entries
disease_sources = ['ICD10CM', 'ICD9CM', 'MDR', 'CMT', 'HPO']
#disease_sources = ['SNOMEDCT_US', 'ICD10CM', 'ICD9CM', 'MEDCIN', 'NCI', 'MDR', 'OMIM', 'RCD', 'CMT', 'HPO'] more extensive list, but contained elements that weren't diseases

#Create DF for diseases only
disease_df = rrf_data[rrf_data['SAB'].isin(disease_sources)]
disease_df.reset_index(drop=True, inplace=True)

#Drop all columns except for disease name
columns_to_keep = ['STR']
disease_df = disease_df[columns_to_keep]

# Keep only unique values in the 'STR' column
unique_values = disease_df['STR'].unique()

# Create a new dataframe with the unique values
unique_df = pd.DataFrame({'DISEASES': unique_values})

#Prompt user to choose program function 
action = 0
while (action != 4):
    print("\nChoose an option. Option 1 will extract all disease names and store them in a CSV file. \nOption 2 returns a random disease name. \nOption 3 asks for an index input and returns disease with corresponding index.")
    print("\t1. Output Unique Disease Names to CSV")
    print("\t2. Return Random Disease Name")
    print("\t3. Return Disease with Specified Index")
    print("\t4. Quit")
    action = int(input("Choice: "))

    if (action == 1):
        file_name = "MRCONSO_Diseases.csv"
        unique_df.to_csv(file_name, index=False, header = None)
        print(f"Diseases have been exported to {file_name}")
    elif (action == 2):
        random_disease = unique_df['DISEASES'].sample(n=1).iloc[0]
        print(random_disease)
            
    elif (action == 3):
        #turn df into dict
        disease_dict = unique_df['DISEASES'].to_dict()
        indx = int(input("Enter a number in the range 0-305349: "))
        print(disease_dict[indx])
    
    elif (action == 4):
        print("Goodbye!!")
        break
        
    else:
        print("Not a valid option. Try again!")
        action = 0