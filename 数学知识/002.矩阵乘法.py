def mul(a,b):
    '''
    矩阵a乘矩阵b
    :param a:
    :param b:
    :return:
    '''
    n,x=len(a),len(a[0])
    x,m=len(b),len(b[0])
    c=[[0]*m for i in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(x):
                c[i][j]+=a[i][k]*b[k][j]
    return c
a=[[1,2],[3,4]]
b=[[5,6],[7,8]]

print(mul(a,b))
# [[19, 22], [43, 50]]
