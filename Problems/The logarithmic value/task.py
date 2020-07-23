import math
raised = int(input())
base = int(input())
result = 0
if base > 1:
    result = math.log(raised, base)
else:
    result = math.log(raised)
print(round(result, 2))