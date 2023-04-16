# 是否存在n个不同正整数和为k，
# 有的话输出其中一种，没有的话返回-1

# 用的贪心，1~n-1采用最小的数，第n个数采用差值

n,k=map(int,input().split())
ans=0
for i in range(1,n):
    ans+=i
# 1~n-1都用过了
if k-ans<n:
    print(-1)
else:
    l=[str(i) for i in range(1,n)]+[str(k-ans)]
    print(' '.join(l))