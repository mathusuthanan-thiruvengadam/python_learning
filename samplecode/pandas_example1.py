import pandas as pd

data = {
    "name":["mathu", "ramya", "aashi", "maghathi"],
    "age":[42,38,12,6],
    "address":["BLR","BLR","BLR","BLR"]
}

df = pd.DataFrame(data)
df = df.sort_values(by="age",ascending=True)
print(df)
df.to_csv("family_details.csv")
