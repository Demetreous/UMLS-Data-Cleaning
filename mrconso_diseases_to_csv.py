# Authors: Demetreous Stillman, Zergio Ruvalcaba
# This program takes in an RRF MRCONSO table file from the Unified Medical Language System,
#  processes the file, isolates the names of unique diseases and drugs in the file, and then gives the user
#  the option to store this into a CSV file or to extract a single disease/drug name. 
# This script has been produced in attempts to simplify and automate efforts to collect data to 
#   generate queries on medical information. 

# Libraries
import pandas as pd

#Prompt user for path to MRCONSO File
file_path = input("Please enter the path to the MRCONSO file: ")
print("Now attempting to process the file. This may take some time...")

# Imports MRCONSO Table and adds column names to create a Pandas dataframe
column_names = ['CUI', 'LAT', 'TS', 'LUI', 'STT', 'SUI', 'ISPREF', 'AUI', 'SAUI', 'SCUI', 'SDUI', 'SAB', 'TTY', 'CODE', 'STR', 'SRL', 'SUPPRESS', 'CVF']
rrf_data = pd.read_csv(file_path, header = None, sep = '|', low_memory = False, names = column_names, index_col = False)

# Filter rows where SAB indicates disease-related entries
disease_sources = ['ICD10CM', 'ICD9CM', 'MDR', 'CMT', 'HPO']
#disease_sources = ['SNOMEDCT_US', 'ICD10CM', 'ICD9CM', 'MEDCIN', 'NCI', 'MDR', 'OMIM', 'RCD', 'CMT', 'HPO'] ## more extensive list, but contained elements that weren't diseases

# Filter rows where SAB indicates drug-related entries
drug_sources = ['RXNORM']

#Create DF for diseases only
disease_df = rrf_data[rrf_data['SAB'].isin(disease_sources)]
disease_df.reset_index(drop=True, inplace=True)

# Create DF for drugs only
drug_df = rrf_data[rrf_data['SAB'].isin(drug_sources)]
drug_df.reset_index(drop=True, inplace=True)

#Drop all columns except for disease name and drug name in respective dataframes
columns_to_keep = ['STR']
disease_df = disease_df[columns_to_keep]
drug_df = drug_df[columns_to_keep]

# Keep only unique values in the 'STR' column
unique_values_diseases = disease_df['STR'].unique()
unique_values_drugs = drug_df['STR'].unique()

# Create a new dataframe with the unique values
unique_disease_df = pd.DataFrame({'DISEASES': unique_values_diseases})
unique_drug_df = pd.DataFrame({'DRUGS': unique_values_drugs})

#Prompt user to choose program function 
action = 0
#Loop to keep presenting user with menu
while (action != 7):
    print("\nChoose an option. For each section, the first option will extract all disease/drugs names and store them in a CSV file. \nThe second option returns a random disease/drug name. \nOption 3 asks for an index input and returns disease/drug with corresponding index.")
    
    #Options for diseases
    print("\n DISEASES: ")
    print("\t1. Output Unique Disease Names to CSV")
    print("\t2. Return Random Disease Name")
    print("\t3. Return Disease with Specified Index")
    
    #Options for drugs
    print("\nDRUGS: ")
    print("\t4. Output Unique Drug Names to CSV")
    print("\t5. Return Random Drug Name")
    print("\t6. Return Drug with Specified Index")
    
    print("\n\t7. Quit")
    action = int(input("Choice: "))

    #Export DF to a csv file
    if (action == 1):
        file_name = "MRCONSO_Diseases.csv"
        csv_header = "Diseases"
        unique_disease_df.to_csv(file_name, index=False, header = csv_header)
        print(f"Diseases have been exported to {file_name} in the current directory")
        
    #Extract random disease name
    elif (action == 2):
        random_disease = unique_disease_df['DISEASES'].sample(n=1).iloc[0]
        print(random_disease)
            
    #Extract disease name with specified index
    elif (action == 3):
        #turn df into dict
        disease_dict = unique_disease_df['DISEASES'].to_dict()
        indx = int(input("Enter a number in the range 0-305349: "))
        print(disease_dict[indx])
        
    #Export DF to a csv file
    elif (action == 4):
        file_name = "MRCONSO_Drugs.csv"
        csv_header = "Drugs"
        unique_drug_df.to_csv(file_name, index=False, header = csv_header)
        print(f"Drugs have been exported to {file_name} in the current directory")
        
    #Extract random drug name
    elif (action == 5):
        random_drug = unique_drug_df['DRUGS'].sample(n=1).iloc[0]
        print(random_drug)
        
    #Extract drug name with specified index
    elif (action == 6):
        #turn df into dict
        drug_dict = unique_drug_df['DRUGS'].to_dict()
        indx = int(input("Enter a number in the range 0-303046: "))
        print(drug_dict[indx])
    
    #Break from loop and end program
    elif (action == 7):
        print("Goodbye!!")
        break
    
    #Return to menu
    else:
        print("Not a valid option. Try again!")
        action = 0