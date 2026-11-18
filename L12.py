import sys
from decimal import Decimal, ROUND_HALF_UP

data = sys.stdin.read().split()
    
n = int(data[0])
idx = 1

for _ in range(n):
    x = Decimal(data[idx])
    idx += 1
    
    val = x.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    
    if val == 0:
        val = Decimal('0.00')
        
    print(f"{val:.2f}")