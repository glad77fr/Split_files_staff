import pandas as pd
import re
import glob
import xlsxwriter
import os


staff = pd.read_csv(r"C:\Users\Sabri.GASMI\Desktop\ALDI\ALDI_ABLIS_STAFF_CLAIRE.csv",encoding="ansi", sep=";",decimal=',')


#path = r'C:\Users\Sabri.GASMI\Desktop\ALDI'
#print(path)
#all_files = glob.glob(path + "/*.csv")

#for val in all_files:
 #   print(val)

dataframe_ref = list(staff["Matricule"].values)
dataframe_ref = set(dataframe_ref)



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
    print(file.dtypes)

    file_staff = file[file['Matricule'].isin(dataframe_ref)]

    file_non_staff = file[~file['Matricule'].isin(dataframe_ref)]

    target_folder = file_rep[:-(len(file_name)+4)] + "\\Split\\"

    print(target_folder)

    if os.path.isdir(target_folder):
        pass
    else:
        os.mkdir(target_folder)

    writer = pd.ExcelWriter(target_folder + file_name + "_STAFF.xlsx" , engine='xlsxwriter')
    file_staff.to_excel(writer, sheet_name='Feuil1',index=False)
    writer.save()

    file_staff.to_excel(target_folder + file_name + "_STAFF2.xlsx")
    writer = pd.ExcelWriter(target_folder + file_name + "_NON_STAFF.xlsx", engine='xlsxwriter')
    file_non_staff.to_excel(writer, sheet_name='Feuil1',index=False)
    writer.save()
    print(file_staff)

split(r"C:\Users\Sabri.GASMI\Desktop\ALDI\ALDI_ABLIS_STAFF_BASES ASSUJETTIES 042019.csv",dataframe_ref)

#all_files = glob.glob(path + "/*.csv")
