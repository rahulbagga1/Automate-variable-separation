import pandas as pd
import numpy as np

#path of the data file
path = input('Enter path of data: ')

#df is the dataframe
df = pd.read_csv(path)

threshold = input('Enter threshold for selecting ordinal features: ')

#cat and con lists store column names of categorical and continuoud variables
cat_ord, cat_int, con_flt, con_int, cat, con = [], [], [], [], [], []

#compare each feature datatype and filtering continuous features
for i,j in zip(df.dtypes.index.tolist(), df.dtypes):
    if np.issubdtype(j, np.float64) or np.issubdtype(j, np.float32):
        con_flt.append(i)
    if np.issubdtype(j, np.object_) or np.issubdtype(j, np.string_):
        cat_ord.append(i)
    if np.issubdtype(j, np.int64) or np.issubdtype(j, np.int32):
        con_int.append(i)

con = con_flt + con_int  

#filtering categorical features
for i in con_int:
    if len(df[i].value_counts().index) < int(threshold):
        cat_int.append(i)
        con.remove(i)
        
for i in cat_ord:
    if len(df[i].value_counts().index) < int(threshold):
        cat.append(i)
        
cat = cat + cat_int

print("Continuos variables: " + str(con))
print("Categorical variables: " + str(cat))

