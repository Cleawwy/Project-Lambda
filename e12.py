bags = int(input())
chocolates = list(map(int, input().split()))

avg = sum(chocolates)//bags

time = 0;
for i in chocolates:
    time += abs(avg-i)

print(time)
