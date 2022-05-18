# -*- coding: utf-8 -*-
"""
Created on Wed May 18 10:53:06 2022

@author: gtaur
"""


# import necessary libraries
import pandas as pd
import os
import glob


#make dir
userfolder = "HF469NN"
folder_files = "C:/Users/"+ userfolder +"/OneDrive - EY/Documents/Py_file_folder/"

# use glob to get all the csv files
# in the folder
path = folder_files
xl_files = glob.glob(os.path.join(path, "*.xlsx"))

lista_df = []

# loop over the list of xl files
for f in xl_files:

	# read the csv file
	df_temp = pd.read_excel(f)
    
	lista_df.append(df_temp)	
	# print the content
	print('Content:')
	print(df_temp)  
	
    
df_tot = pd.concat(lista_df) #concat df

df = df_tot

#select column
	
select = df[df['Stato'] == 'Done']

select2 = select.copy()




# dropping ALL duplicate values
select2.drop_duplicates(subset ="Descrizione", keep = False, inplace = True)
 

#pass col to list
row_task = select2['Descrizione'].tolist()

#add prefix

stringa = '- '
row_task2 = [stringa + x   for x in row_task]

#print in console

for row in row_task2:
    print(row)
    
    
#print to new txt

with open(path + "report202204.txt","w+") as f:
        for row in row_task2:
            f.write("%s\n" % row)
    





'''
some reminders

w  write mode
r  read mode
a  append mode

w+  create file if it doesn't exist and open it in write mode
r+  open for reading and writing. Does not create file.
a+  create file if it doesn't exist and open it in append mode




'''
