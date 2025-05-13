import pandas as pd

df = pd.read_csv("सरकारी रिजल्ट (SKResult.Com)  42.csv",header=None,names=["Phone"])

df["Name"] = ["Member" + str(i + 1) for i in range(len(df))]

df = df[["Name","Phone"]]

df.to_csv("सरकारी रिजल्ट (SKResult.Com)  42 with header.csv", index=None)