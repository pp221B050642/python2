import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("ted_talks.csv")
years = pd.to_datetime(data['published_date']).dt.year.value_counts()

bar_chart = {}
for i, year in enumerate(years.index.tolist()):
    x = int(year)
    y = years.iloc[i]
    bar_chart[x] = y

graph = {}
for i in sorted(bar_chart):
    graph[i] = bar_chart[i]

year = list(graph.keys())
counts = list(graph.values())
# print(year)
fig = plt.figure(figsize = (10, 5))
plt.bar(year, counts, color = "maroon", width = 0.3)
plt.xlabel("years")
plt.ylabel("No. of published video")
plt.title("ted talks")
plt.show()


