import sys
import heapq

input_data = sys.stdin.read().split()
    
t = int(input_data[0])

max_heap = []
min_heap = []

for i in range(1, t + 1):
    x = int(input_data[i])
    if not max_heap or x <= -max_heap[0]:
        heapq.heappush(max_heap, -x)
    else:
        heapq.heappush(min_heap, x)
    if len(max_heap) > len(min_heap) + 1:
        heapq.heappush(min_heap, -heapq.heappop(max_heap))
    elif len(min_heap) > len(max_heap):
        heapq.heappush(max_heap, -heapq.heappop(min_heap))
        
    if len(max_heap) == len(min_heap):
        median = (-max_heap[0] + min_heap[0]) // 2
    else:
        median = -max_heap[0]
        
    print(median)