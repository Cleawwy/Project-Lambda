matrixSize = int(input())
matrix = [
 [1, 3, 1, 5],
 [2, 2, 4, 1],
 [5, 0, 2, 3],
 [0, 6, 1, 2]
]



zigZag = []

for i in range(matrixSize):
  fours = list(map(int, input().split()))
  matrix.append(fours)

print(matrix)

for row in range(len(matrix)):

  iterator = 0
  for i in range(row+1):
    zigZag.append(matrix[row][iterator])
    iterator+=1

  if row == matrixSize+1:
    break

print(zigZag)
