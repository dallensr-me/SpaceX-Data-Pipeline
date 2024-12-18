import pandas as pd

data = {
    "rocket": [
        "Falcon 1",
        "Falcon 9",
        "Falcon Heavy",
        "Rocky McRocketson"
    ],
    "Launches": [5, 100, 3, 666]
}

df = pd.DataFrame(data)

df["success_rate"] = [0.5,0.6,1,0.666]

rocky_df = df[df["rocket"] == "Rocky McRocketson"]
print(rocky_df)