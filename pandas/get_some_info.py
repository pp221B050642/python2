import pandas as pd

data = pd.read_csv("ted_talks.csv")

def get_the_longest_video():
    temp = data["duration"].max()
    longest_video = data[data["duration"]==temp]
    print(longest_video)
get_the_longest_video()

def get_the_most_viewed_video():
    temp = data["views"].max()
    most_viewed = data[data["views"]==temp]
    print(most_viewed)
get_the_most_viewed_video()

def get_the_most_liked_video():
    temp = data["likes"].max()
    liked = data[data["likes"]==temp]
    print(liked)
get_the_most_liked_video()