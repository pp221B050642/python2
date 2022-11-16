import pandas as pd

data = pd.read_csv("ted_talks.csv")

def count_videos_by_year():
    years = pd.to_datetime(data['published_date']).dt.year.value_counts()
    return years.sort_values()

# print(count_videos_by_year())