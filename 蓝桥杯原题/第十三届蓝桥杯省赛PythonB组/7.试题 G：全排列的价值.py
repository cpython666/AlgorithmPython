MOD = 998244353
n = int(input().strip())
dp = 0
f = 1
for i in range(2,n+1):
    dp = (dp*i+f*i*(i-1)//2)%MOD
    f = f*i%MOD
print(dp)