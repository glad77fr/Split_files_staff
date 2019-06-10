import pandas as pd
import re
import glob
import xlsxwriter
import os
from Correct_typing import correct_typing



def staff(staff_file):
    staff = pd.read_csv(staff_file, encoding="ansi", sep=";", decimal=',')
    staff = list(staff["Matricule"].values)
    staff = set(staff)
    return staff

def split(file, dataframe_ref):

    file_name = ""
    file_rep = file
    file_ind = file[:-4]
    target_folder = ""

    for val in file_ind[::-1]:
        if val != "\\":
            file_name = file_name + val
        else:
            break
    file_name = file_name[::-1]

    file = pd.read_csv(file, encoding="ansi", sep= ";")
    correct_typing(file)

    file_staff = file[file['Matricule'].isin(dataframe_ref)]

    file_non_staff = file[~file['Matricule'].isin(dataframe_ref)]

    target_folder = file_rep[:-(len(file_name)+4)] + "\\Split\\"


    if os.path.isdir(target_folder):
        pass
    else:
        os.mkdir(target_folder)

    writer = pd.ExcelWriter(target_folder + file_name + "_STAFF.xlsx" , engine='xlsxwriter',date_format='DD-MM-YYYY')
    file_staff.to_excel(writer, sheet_name='Feuil1',index=False)
    writer.save()

    writer = pd.ExcelWriter(target_folder + file_name + "_NON_STAFF.xlsx", engine='xlsxwriter',date_format='DD-MM-YYYY')
    file_non_staff.to_excel(writer, sheet_name='Feuil1',index=False)
    writer.save()


#split(r"C:\Users\Sabri.GASMI\Desktop\ALDI\ALDI_ABLIS_STAFF_BASES ASSUJETTIES 042019.csv",dataframe_ref)


#all_files = glob.glob(path + "/*.csv")
#for val in all_files:
 #   split(val,dataframe_ref)

#all_files = glob.glob(path + "/*.csv")
