import sys

from decimal import Decimal
from math import ceil
X, Y = map(Decimal, input().split())

percentage = int(Y/X * 100) + 1
mission_percentage = (percentage * X - 100 * Y)/(100-percentage)

if X == Y or int((Y/X)*100) == 99:
    print(-1)
else:
    
    print(ceil(round(mission_percentage, 10)))
sys.exit(0)

# 파라메트릭 서치로 다시 공부해서 풀어보도록 하자...
