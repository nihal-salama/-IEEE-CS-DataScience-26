import math
x1 , y1 = map(int,input(f"Enter the point 1: ").split())
x2 , y2 = map(int,input(f"Enter the point 2: ").split())
d = math.sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
print(f"The distance is: {d:.2f}")