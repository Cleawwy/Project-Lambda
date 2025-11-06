nMobiles = int(input())
seriesOfCapacity = list(map(int, input().split()))
chargeCapacity = int(input())
chargedMobiles = 0

while chargeCapacity > 0:
    for i in range(nMobiles):
        if seriesOfCapacity[i] > 0:
            if chargeCapacity > 0:
                seriesOfCapacity[i] -= 1
                chargeCapacity -= 1
            else:
                break
    else:
        if all(cap == 0 for cap in seriesOfCapacity):
            break

for phone in seriesOfCapacity:
    if phone == 0:
        chargedMobiles += 1

print(chargedMobiles)
