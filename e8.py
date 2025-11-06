t_mins = int(input())
t_sec = t_mins * 60

reloadTime = int(input())
fireTime   = int(input())

totalBullets = 0

while True:
  if t_sec < reloadTime+fireTime:
    break

  t_sec -= reloadTime
  t_sec -= fireTime
  totalBullets += 1

print(totalBullets)
