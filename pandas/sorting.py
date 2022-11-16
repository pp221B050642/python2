import pandas as pd

data = pd.read_csv("ted_talks.csv")

sorted_data_by_title = data.sort_values(by = "title")
pd.set_option('display.max_column', None)
print(sorted_data_by_title.head(5))
