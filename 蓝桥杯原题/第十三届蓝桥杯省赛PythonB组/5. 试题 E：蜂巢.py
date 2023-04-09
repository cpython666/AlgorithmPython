d1,p1,q1,d2,p2,q2=map(int,input().split())

# 全部转化为0 方向 和 1方向的向量
def change(d,p,q):
    if d==0:return (p-q,q)
    if d==1:return (-q,p)
    if d==2:return (-p,p-q)
    if d==3:return (q-p,-q)
    if d==4:return (q,-p)
    if d==5:return (p,q-p)
s1=change(d1,p1,q1)
s2=change(d2,p2,q2)

# 向量的剑法
s=[s1[0]-s2[0],s1[1]-s2[1]]
a,b=s[0],s[1]
if a*b > 0: 
    # ab同号
    print(abs(a+b))
else: 
    # ab异号
  	print(max(abs(a),abs(b)))