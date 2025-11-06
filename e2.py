rows = int(input())
columns = int(input())

matrix = []

"""
Example Input:
3 rows
3 columns

[
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

"""


for i in range(rows):
  matrix.append(list(map(int, input().split())))

maxRow = 0;
maxColumn = 0;

# maxRow finder
bigRow = 0;
for i in range(rows):
  sum = 0;
  for val in matrix[i]:
    sum += val;

  if sum > bigRow:
    bigRow = sum;
    maxRow = i;

# maxColumn finder
bigColumn = 0;
for i in range(columns):
  sum = 0;
  for v in range(rows):
    sum += matrix[v][i];

  if sum > bigColumn:
      bigColumn = sum
      maxColumn = i;

print(matrix[maxRow][maxColumn])
