inputStr = list(input())
iter = False

while True:
  for i in range(len(inputStr)-1, -1, -1):
    if i < (len(inputStr)-1) and inputStr[i] == inputStr[i+1]:
      del inputStr[i+1]
      del inputStr[i]
      iter = True
      break
    else:
      iter = False

  if len(inputStr) == 0:
    break

  if iter == False:
    break

print("".join(inputStr))
