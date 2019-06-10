import pandas as pd

#staff = pd.read_csv(r"C:\Users\Sabri.GASMI\Desktop\ALDI\ALDI_ABLIS_STAFF_CLAIRE.csv",encoding="ansi", sep=";",decimal=',')
staff_rep = r"C:\Users\Sabri.GASMI\Desktop\ALDI\ALDI_ABLIS_STAFF_CLAIRE.csv"
path = r'C:\Users\Sabri.GASMI\Desktop\ALDI'
#print(path)
#all_files = glob.glob(path + "/*.csv")

#for val in all_files:
 #   print(val)

#dataframe_ref = list(staff["Matricule"].values)
#dataframe_ref = set(dataframe_ref)

def staff(staff_rep):
    print(staff_rep)
    staff_res = pd.read_csv(staff_rep, encoding="ansi", sep=";", decimal=',')
    print(staff_res.dtypes)
    staff_res = list(staff_res["Matricule"].values)
    staff_res = set(staff_res)
    return staff_res

staff(staff_rep)