#the shortest path
import numpy as np

arr = np.asarray([
  ("00000"),
  ("01006"),
  ("02000"),
  ("30050"),
  ("00004")
])
points = {}

for i in range(arr.shape[0]):
  for j in range(len(arr[i])):
    if arr[i][j] != 0:
      points[arr[i][j]]=[i, j]

points.pop("0")
sorted_points = sorted(points.items())

cnt = 0

for i in range(len(sorted_points)-1): 
  cnt += abs(int(sorted_points[i][1][0]-int(sorted_points[i+1][1][0])))
  cnt += abs(int(sorted_points[i][1][1]-int(sorted_points[i+1][1][1])))

print(cnt)


