import math
edge = int(input())
area = 2 * math.sqrt(3) * pow(edge, 2)
volume = 1 / 3 * math.sqrt(2) * pow(edge, 3)
print(round(area, 2), " ", round(volume, 2))