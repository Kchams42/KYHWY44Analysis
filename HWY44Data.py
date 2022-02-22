import pandas as pd
import numpy
import matplotlib

#importing data
df=pd.read_csv('venv\Analysis\Incident.txt')

#Looking at different parts of the data set.
    #print (df.head)
    #print (df.info())
    #print (df.describe)
    #print (df['AgencyName'].value_counts())
useful_columns = [19,20,22,23,24,]
new_df = df[df.columns[useful_columns]]
#print (new_df.head)
#print (new_df.info())
#print ( new_df.describe)
#print (new_df.shape)
print (new_df['NumberInjured'].value_counts())
#import registration data
