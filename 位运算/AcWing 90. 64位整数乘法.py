# https://www.acwing.com/problem/content/92/

# 求 a 乘 b 对 p 取模的值。

# 思路：快速幂是计算a的b次方，是a*a*...*a
# 此题是计算a*b，a+a+...+a，可以使用同样的思路

def ksj(a,b,p):
    res=0
    while b:
        if b&1:res=(res+a)%p
        b>>=1
        a=(a+a)%p
    return res

a,b,p=map(int,[input(),input(),input()])

print(ksj(a,b,p))