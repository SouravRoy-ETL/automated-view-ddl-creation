import pandas as pd
import numpy as np
import string
import sys
import os
import shutil
import time
from pathlib import Path
####################################################################################################################################################
###Function for Creation of the Views
####################################################################################################################################################
def create_views(input_view):
    l=input_view['TARGET_Table_Name'].nunique()
    listofuniquetargets = pd.unique(input_view['TARGET_Table_Name']).tolist()
    for i in range(l):
        scan = input_view.loc[input_view['TARGET_Table_Name'] == listofuniquetargets[i]]
        Target_Table_Name=scan['TARGET_Table_Name'].iloc[0]
        Source_Dataset_Name=scan['Source_Dataset_Name'].iloc[0]
        #str(Source_Dataset_Name).strip(" ")
        Target_Columns=scan['TARGET_Columns'].tolist()
        Target_View_Name=scan['Target_View_Name'].iloc[0]
        Target_Project_Name=scan['Target_Project_Name'].iloc[0]
        Target_Dataset_Name=scan['Target_Dataset_Name'].iloc[0]
        pop=[]
        view = open(r'Output_DDL/View_Report001.sql', 'a')
        view.write('CREATE VIEW `'+str.lower(Target_Project_Name)+'.'+str.lower(Target_Dataset_Name)+'.'+Target_View_Name+'`'+' ')
        view.write('AS SELECT'+'\n')
        for n in range(0, len(Target_Columns)):
            data= '   '+Target_Columns[n]+','
            view.write(data)
            view.write('\n')
        #Source_Dataset_Name.translate({ord(c): None for c in string.whitespace})
        input_view['Source_Dataset_Name'] = input_view['Source_Dataset_Name'].replace(' ','')
        view.write('FROM `'+Source_Dataset_Name+'.'+Target_Table_Name+'`;'+'\n')
        view.close() # Close writing the SQL View File
####################################################################################################################################################
###Function for Removing the Last Comma
####################################################################################################################################################
def remove_last_comma():
    with open(r'C:\Users\Sourav Roy\Desktop\Workspace\VIEW_CREATION\Output_DDL\View_Report001.sql', 'r') as file :
        filedata = file.read()
    filedata = filedata.replace(",\nFROM","\nFROM")
    with open(r'C:\Users\Sourav Roy\Desktop\Workspace\VIEW_CREATION\Output_DDL\View_Report001.sql', 'w') as file:
         file.write(filedata)
####################################################################################################################################################
###Main Function
####################################################################################################################################################
if(__name__=='__main__'):
    input_view = pd.read_csv(r"Input/View_Report001.csv",encoding='utf8', sep=',', header=None, skiprows=0, na_values=' ', error_bad_lines=False)
    input_view.columns = input_view.iloc[0]
    input_view = input_view[1:]
    input_view.replace('', np.nan, inplace=True)
    input_view['Source_Dataset_Name'] = input_view['Source_Dataset_Name'].replace(" ","")
    create_views(input_view)
    remove_last_comma()
