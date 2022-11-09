
#minesweeper i-grid
import numpy as np

grid = np.array([
  ["-", "-", "-", "#", "#"],
  ["-", "#", "-", "-", "-"],
  ["-", "-", "#", "-", "-"],
  ["-", "#", "#", "-", "-"],
  ["-", "-", "-", "-", "-"]
])

(n, m) = grid.shape
mine = 0
mines = []
booms = []
for i in range(n):
  for j in range(m):
    if grid[i][j] == "#":
      mines.append([i, j])
      booms.extend([(i-1, j), (i, j-1), (i+1, j), (i, j+1), (i-1, j-1), (i+1, j+1), (i+1, j-1), (i-1, j+1)])

# print(booms)
# print(mines)
booms2 = []
print(len(booms))
for i in booms:
  print(i)
  if 0<=i[0]<n and 0<=i[1]<m:
    booms2.append(i)
print(booms2)
print(len(booms2))

for i in booms2:
  if grid[i[0]][i[1]] == "#":
    booms2.remove(i)
print(booms2)
print(len(booms2))
for i in booms2:
  if grid[i[0]][i[1]] == "#":
    booms2.remove(i)
booms_dict = {}

for i in booms2:
  cnt = 1
  if i not in booms_dict:
    booms_dict[i] = cnt
  else:
    booms_dict[i] = cnt+1

for i in range(n):
  for j in range(m):
    if (i, j) in booms_dict:
      grid[i][j] = booms_dict[(i, j)]
    if grid[i][j] == "-":
      grid[i][j] = "0"
print(grid)
