# https://www.acwing.com/problem/content/91/

# 求 a 的 b 次方对 p 取模的值。

# 快速幂

def ksm(a,b,p):
    res=1%p
    while b:
        if b&1:res=res*a%p
        a=a*a%p
        b>>=1
    return res

a,b,p=map(int,input().split())
print(ksm(a,b,p))