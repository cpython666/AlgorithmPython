def gcd(m,n):
    '''
    最大公因数
    '''
    return n if m%n==0 else gcd(n,m%n)
def lcm(m,n):
    '''
    最小公倍数
    '''
    return int(m*n/gcd(m,n))
print(gcd(12,16))
print(lcm(12,16))