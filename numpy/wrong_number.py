import numpy as np
import math

lst1 = np.array([
  [1, 2, 3, 6 ],
  [4, 5, 6, 15],
  [7, 8, 9, 24],
  [12,15,18,46]

])
error1 = {}


for i in range(4):
  s = math.fsum(lst1[i, 0:3])
  if s != lst1[i][3]:
    for j in range(4):
        error1[lst1[i][j]] = [i, j]

# print(error1)

error2 = {}

for i in range(4):
  s = math.fsum(lst1[0:3, i])
  if s!= lst1[3][i]:
    for j in range(4):
      error2[lst1[j][i]] = [j, i]

# print(error2)

for i in error1.keys():
  for j in error2.keys():
    if error1[i] == error2[j]:
      print(i)
    





