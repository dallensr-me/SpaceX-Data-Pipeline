#import pandas library for data manipulation
import pandas as pd

#url for pandas to access api
url = "https://api.spacexdata.com/v4/launches"

#create dataframe from api return values
df = pd.read_json(url)

#print dataframe
#print(df.head())

#print list of column names
#print(df.columns)

#print list of data types
print(df.dtypes)
