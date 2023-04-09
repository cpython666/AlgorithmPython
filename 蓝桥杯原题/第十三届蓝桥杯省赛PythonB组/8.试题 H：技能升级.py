import heapq

n,m = map(int,input().split())
a,b = [],[]

heap = []
for i in range(n):
    x,y = map(int,input().split())
    a.append(x)
    b.append(y)
    heapq.heappush(heap,(-x,i,0))

cnt = 0
import math
for i in range(m):
    x,y,z = heapq.heappop(heap)
    if x == 0:
        break
    x=-x
    cnt += x
    # x,y = nlargest(1,heap)
    if z > math.ceil(a[y]/b[y]):  
        x = 0
        continue
    else:
        x = x - b[y]
    heapq.heappush(heap,(-x,y,z+1))
    
print(cnt)