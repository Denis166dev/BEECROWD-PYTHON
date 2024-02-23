import math
a,b,c = map(int, input().split())

p = (a+b+c)/2
area = math.sqrt(p*(p-a)*(p-b)*(p-c))

print(f'{area:.3f} m2')