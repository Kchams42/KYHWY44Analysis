import webbrowser
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#importing data
df=pd.read_csv('Incident.txt')
df2=pd.read_csv('Registration data .csv')
print (df2)
# Changing the date format to only show the year
df['year'] =pd.DatetimeIndex(df['CollisionDate']).year

#Looking at different parts of the data set.
    #print (df.head)
    #print (df.info())
    #print (df.describe)
    #print (df['AgencyName'].value_counts())

# Pulling the needed columns from the data. 
useful_columns = [39,22,23,24,]
df = df[df.columns[useful_columns]]

#grouping each data set by year  
df = df.groupby(['year']).sum()
df2 = df2.groupby(['year']).sum()



#transforming the data sets 
df = df.T
df2=df2.T

#Combine the two data sets
result=pd.concat([df, df2])

# remove the last column containint incomplete data
result = result.iloc[: , :-1]

#double checking that I do have a dataframe
if isinstance(result, pd.DataFrame):
    print ('YES!')
result.set_index('year', inplace=True)
#printing the data frame to a web browser
with open('str.html', 'w') as f:
    result.to_html(f)
filename = 'str.html'
webbrowser.open_new_tab(filename)