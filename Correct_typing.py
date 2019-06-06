import pandas as pd
import re

data = pd.read_csv(r"C:\Users\Sabri.GASMI\Desktop\ALDI\ALDI_ABLIS_STAFF_COMPOSANTS_BASES ASSUJETTIES 042019.csv",encoding="ansi", sep=";")

def correct_typing(dataframe):
    nb_columns = len(dataframe.columns)
    r = re.compile(r"^\d*[.,]\d*$")
    for y in range(nb_columns):
       for i in range(len(dataframe)):
           if pd.notna(dataframe.iat[i,y]):
               if len(str(dataframe.iat[i,y])) == 10 and str(dataframe.iat[i,y]).count('/') == 2: # Test if is a datetime
                   dataframe[dataframe.columns[y]] = dataframe[dataframe.columns[y]].astype('datetime64')
                   break

               if r.match(str(dataframe.iat[i,y])):

                   dataframe[dataframe.columns[y]] = dataframe[dataframe.columns[y]].apply(lambda x: str(x.replace(",",".")))
                   dataframe[dataframe.columns[y]] = dataframe[dataframe.columns[y]].astype('float64')
                   break

               break
    dataframe.to_excel(r'C:\Users\Sabri.GASMI\Desktop\toto.xlsx')

               #print("ok")


    print(dataframe.dtypes)


            #dataframe[dataframe.columns[y]] = dataframe[dataframe.columns[y]].astype('datetime64')




        #if len(str(dataframe.iat[1,i])) == 10:
            #print(dataframe[dataframe.columns[i]])
            #print("ok")
         #   print(dataframe[dataframe.columns[i]])
            #dataframe[dataframe.columns[i]] = dataframe[dataframe.columns[i]].astype('datetime64')


correct_typing(data)