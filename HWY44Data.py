from unittest import result
import pandas as pd
import numpy
import matplotlib

#importing data
df=pd.read_csv('venv\Analysis\Incident.txt')
df2=pd.read_csv('venv\Analysis\Registration data - Sheet1.csv')
df['year'] =pd.DatetimeIndex(df['CollisionDate']).year
#Looking at different parts of the data set.
    #print (df.head)
    #print (df.info())
    #print (df.describe)
    #print (df['AgencyName'].value_counts())

useful_columns = [39,22,23,24,]
df = df[df.columns[useful_columns]]
#print (df)
#print (new_df.head)
#print (new_df.info())
#print ( new_df.describe)
#print (new_df.shape)
#print (new_df['MotorVehiclesInvolved'].value_counts())
#print (new_df.sum())    
df = df.groupby(['year']).sum()
df = df.T
df2=df2.T
print (df2)
print (df)





#frames= [df, df2]
#result = pd.concat(frames)

#print(result)