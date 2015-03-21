__author__ = 'workhorse'

import pandas as pd
from scipy import stats


data = '''Region,Alcohol,Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''


#split the data into lines
data = data.splitlines()
#turn the data into a list object that can be iterated through
data = [i.split(",") for i in data]
#set column header names equal to the first row
column_names = data[0]
#store non-column data in a seperate variable
data_rows = data[1:]
#print data_rows
rows = [i[0] for i in data_rows]
#print rows
#create a frame - use the data rows as the source, column_names for the headers
#attempted to uses rows as a header, df = pd.DataFrame(data_rows, columns=column_names, index = rows)
#but it lead to duplication of the regions column
df = pd.DataFrame(data_rows, columns=column_names)
#print df

#create float values
df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

#create two dictionaries to hold computed descriptive stats.  Im sure it could
#be done other ways
alcohol = {}
tobacco = {}

alcohol["mean"]= df['Alcohol'].mean()
alcohol["median"] = df['Alcohol'].median()
alcohol["mode"] = stats.mode(df['Alcohol'])[0][0]
alcohol["range"] = max(df['Alcohol'])- min(df['Alcohol'])
alcohol["standard deviation"] = df['Alcohol'].std()
alcohol["variance"] = df['Alcohol'].var()


print "Descriptive Statistics for Alcohol Spending"

for k,v in alcohol.iteritems():
    print "The {} of weekly household spending on alcohol is {} pounds".format(k, round(v, 4))

tobacco["mean"]= df['Tobacco'].mean()
tobacco["median"] = df['Tobacco'].median()
tobacco["mode"] = stats.mode(df['Tobacco'])[0][0]
tobacco["range"] = max(df['Tobacco'])- min(df['Tobacco'])
tobacco["standard deviation"] = df['Tobacco'].std()
tobacco["variance"] = df['Tobacco'].var()

print "Descriptive Statistics for Tobacco Spending"

for k,v in tobacco.iteritems():
    print "The {} of weekly household spending on tobacco is {} pounds".format(k, round(v, 4))
