#import pandas library
import pandas as pd

#build dataset
data = {
    "rocket": [
        "Falcon 1",
        "Falcon 9",
        "Falcon Heavy",
        "Rocky McRocketson"
    ],
    "Launches": [5, 100, 3, 666]
}

#convert dataset into dataframe
df = pd.DataFrame(data)

#print dataframe
print(df)

#print just the rocket values from the dataframe
print(df["rocket"])

#add new column success_rate to dataframe
df["success_rate"] = [0.5,0.6,1,0.666]

#create dataframe filtered to rocket = 'Rocky McRocketson'
rocky_df = df[df["rocket"] == "Rocky McRocketson"]

#print filtered dataframe
print(rocky_df)