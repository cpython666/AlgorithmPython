# 初始值1，目标值k
# 操作1：乘2
# 操作2：乘2加1

# 输入一个数k
# 输出操作的方法，不存在输出-1

# 如：输入5，输出1 2

x=int(input())
x=bin(x)[3:]
ans=[]
for i in x:
    if i=='1':
        ans.append('2')
    else:
        ans.append('1')
print(' '.join(ans))

# 本质是二进制运算，操作一末尾补0，操作二末尾补1