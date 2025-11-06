sticks = int(input())
lengths = list(map(int, input().split()))
lengths.sort()

Rectangles = 0;
Index = 0;

while True:
  Index += 1;
  for i in range(len(lengths)):
    LRSide = False;
    UDSide = False;
    if i+1 < len(lengths):
      if lengths[i] == lengths[i+1]:
        del lengths[i+1];
        del lengths[i];

        LRSide = True;
        if LRSide == False:
          break;

        for v in range(len(lengths)):
          if v+1 < len(lengths):
            if lengths[v] == lengths[v+1]:
              del lengths[v+1];
              del lengths[v];

              UDSide = True;
              break;
      
      if UDSide:
        Rectangles += 1;
        break;

  if Index == len(lengths):
    break;

print(Rectangles)
