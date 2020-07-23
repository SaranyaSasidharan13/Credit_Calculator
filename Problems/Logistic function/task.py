import math
x = int(input())
sigma = math.exp(x) / (math.exp(x) + 1)
print(round(sigma, 2))