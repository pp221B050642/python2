import pandas as pd
import math

data = pd.read_csv("ted_talks.csv")

data["duration"] = data['duration']/60

pd.set_option('display.max_column', None)
print(data)

