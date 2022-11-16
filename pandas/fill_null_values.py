import pandas as pd

data = pd.read_csv("ted_talks.csv")
# print(data.shape)
# print(data.info())
# d = data.describe()
# print(d)
# print(d["duration"]["max"])
# columns = data.columns
# bool_series = pd.isnull(data["event"])
# print(data[bool_series])
def fill_null_values():
    temp = data['speaker'].value_counts()
    temp2 = data["recorded_date"].value_counts()
    temp3 = data["event"].value_counts()
    data["speaker"].fillna(temp.index[0], inplace = True)
    data['recorded_date'].fillna(temp2.index[0], inplace=True)
    data["event"].fillna(temp3.index[0], inplace= True)
fill_null_values()






