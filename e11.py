arrSize = int(input())
arrElements = list(map(int, input().split()))
odd = 0;

for i in arrElements:
  iterable = str(i)

  sum = 0
  for i in iterable:
    sum += int(i)

  if sum % 2 != 0:
    odd += 1

if arrSize - odd > 0:
  print("Normal Array")
else:
  print("Special Odd Array")


print(odd)
