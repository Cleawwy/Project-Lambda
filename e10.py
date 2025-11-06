# index will be based on character order
# no libraries needed

segments = [
  "ABCEFG", "CG", "BCDEF", "BCDGF", "ADCG", "BADGF",
  "BADEFG", "BCD", "ABCDEFG", "ABCDG"
]

chosen = "X"
while True:
  number = int(input())
  temp = segments[number]

  if chosen == "X":
    chosen = temp
    print(len(chosen))
  else:
    count = 0
    for a in chosen:
      for b in temp:
        if a == b:
            count+=1

    print((len(chosen) - count) + (len(temp) - count)) # [1, 0] <-> [0, 1] foolproof
    chosen = temp

