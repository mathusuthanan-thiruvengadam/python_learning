import pandas as pd
import matplotlib.pyplot as plt

data = {
    "name":["mathu", "ramya", "aashi", "maghathi"],
    "age":[42,38,12,6],
    "address":["BLR","BLR","BLR","BLR"]
}

df = pd.DataFrame(data)
df = df.sort_values(by="age",ascending=True)
print(df)

plt.figure(figsize=(8, 6))
plt.bar(df['name'], df['age'], color='skyblue')
plt.xlabel('name')
plt.ylabel('age')
plt.title('Age Distribution')
plt.xticks(rotation=45)
plt.show()

