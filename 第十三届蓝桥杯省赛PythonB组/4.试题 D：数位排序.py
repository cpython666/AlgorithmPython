n = int(input())
m = int(input())
l = [i for i in range(1,n+1)]
# 设置一个排序规则，计算数位之和
def fun(x):
    ans = 0
    while x:
        ans += x%10
        x = x//10
    return ans 

l.sort(key = fun)
print(l[m-1])