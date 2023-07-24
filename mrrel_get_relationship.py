# Authors: Demetreous Stillman & Zergio Ruvalcaba
#This program allows you to extract relationships from UMLS MRREL file and store them in a csv file.
#You can extract a single relationship by name, or all of the relationships in the file. 
#This is an extension of 'mrrel_cleaning.ipynb' program

# Libraries
import pandas as pd
import csv

#Prompt user for path to MRREL File
file_path = input("Please enter the path to the MRREL file: ")

# Imports MRREL Table and adds column names
column_names = ['CUI1', 'AUI1', 'STYPE1', 'REL', 'CUI2', 'AUI2', 'STYPE2', 'RELA', 'RUI', 'SRUI', 'SAB', 'SL', 'RG', 'DIR', 'SUPPRESS', 'CVF', 'UNNAMED']
rrf_data = pd.read_csv(file_path, header = None, sep = '|', low_memory = False, names = column_names)

#Prompt user to choose program function 
print("\nChoose an option. Option 1 will prompt for the name of a single relationship, and store all the rows for that relationship in a CSV file. \nOption 2 goes through each of the relationships in MRREL, and stores all corresponding rows in individual CSV files.")
print("\t1. Extract single relationship")
print("\t2. Extract ALL relationships")
action = int(input("Choice: "))

if (action == 1):
    rel_name = input("Enter the name of the relationship (must match the name in the MRREL file): ")
    rel_rows = rrf_data[rrf_data['RELA'] == rel_name]
    output_file = f"MRREL_{rel_name}_data.csv"
    rel_rows.to_csv(output_file, index=False, mode = 'w')
elif (action == 2):
    unique_rela = rrf_data['RELA'].unique()

    for rela in unique_rela:
        # Filter the DataFrame for the current unique name
        filtered_data = rrf_data[rrf_data['RELA'] == rela]
        
        # Save the filtered data to a new CSV file
        file_name = f"{rela}_data.csv"
        filtered_data.to_csv(file_name, index=False, mode = 'w')
        
        print(f"CSV file '{file_name}' has been saved.")
else:
    print("Not a valid option. Goodbye!")

