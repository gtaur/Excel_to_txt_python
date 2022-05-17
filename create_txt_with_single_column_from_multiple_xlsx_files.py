# -*- coding: utf-8 -*-
"""
Created on Tue May 17 09:54:23 2022

@author: gtaur
"""


# importing pandas module
import os
import pandas as pd



#make directory variable
userfolder = "" #your userfolder
deskt = "C:/Users/"+ userfolder +"/OneDrive - /Desktop/" #your desktop folder 

#create files vars
file1 = deskt+"xxx.xlsx" #filename1

file2 = deskt+"xxx.xlsx" #filename2

file3 = deskt+"xxx.xlsx" #filename3

file4 = deskt+"xxx.xlsx" #filename4

 
# import from excl


df1 = pd.read_excel(file1,index_col=None)

df2 = pd.read_excel(file2,index_col=None)

df3 = pd.read_excel(file3,index_col=None)

df4 = pd.read_excel(file4,index_col=None)


#unisci i df

df = df1.append(df2,ignore_index = True)

df = df.append(df3,ignore_index = True)

df = df.append(df4,ignore_index = True)

#select I DONE

select = df[df['Stato'] == 'Done'] #change cases

select2 = select.copy()


# dropping ALL duplicate values
select2.drop_duplicates(subset ="Descrizione", keep = False, inplace = True)
 

#pass the column to a list var
row_task = select2['Descrizione'].tolist()

#add prefix you want

stringa = '- '
row_task2 = [stringa + x   for x in row_task]

#print in console to check

for row in row_task2:
    print(row)
    
    
#print to non existing txt

with open(deskt + "report202204.txt","w+") as f:
        for row in row_task2:
            f.write("%s\n" % row)
    



'''
some recap

w  write mode
r  read mode
a  append mode

w+  create file if it doesn't exist and open it in write mode
r+  open for reading and writing. Does not create file.
a+  create file if it doesn't exist and open it in append mode
'''


