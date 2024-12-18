#import requests library for API requests
import requests
#import pandas library for data manipulation
import pandas as pd

response = requests.get("https://api.spacexdata.com/v4/launches")
data = response.json()

#convert dataset into dataframe
df = pd.DataFrame(data)

#print dataframe
print(df[:5])