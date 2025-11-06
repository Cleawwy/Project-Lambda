ref_index = int(input())
density = int(input())
hardness = float(input())

grade = 10

Conditions = [ref_index > 50, density < 2500, hardness < 6.8]

if all(Conditions):
  grade = 1
elif Conditions[0] and Conditions[1]:
  grade = 2
elif Conditions[0] and Conditions[2]:
  grade = 3
elif Conditions[1] and Conditions[2]:
  grade = 4
elif any(Conditions):
  grade = 9


print(grade)
