teamSize = int(input())
teamIQ = list(map(int, input().split()))
total = sum(teamIQ)

for i in teamIQ:
  print(total-i, end=' ')
