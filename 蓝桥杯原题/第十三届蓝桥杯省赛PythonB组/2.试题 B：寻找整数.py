#1.枚举数据找规律
i=1
while True:
    flag=True
    if i%49!=46:
        flag=False
    if i%48!=41:
        flag=False
    if i%47!=5:
        flag=False
    if i%46!=15:
        flag=False
    if i%45!=29:
        flag=False
    if flag:
        print(i)
    i+=1
'''
4772009
42909689
81047369
119185049
157322729
195460409
233598089
271735769
···
'''


# #2.找出规律求公式
# a=[4772009, 42909689, 81047369, 119185049,157322729]
# #发现存在等差数列
# print(a[1]-a[0])#38137680
# print(a[2]-a[1])#38137680
# print(a[3]-a[2])#38137680
# k=38137680
# b=4772009
# #求出公式
# y=k


# #遍历公式
# x=0
# k=38137680
# b=4772009
# while True:
#     flag=True
#     y=k*x+b
#     for i,j in mod:
#         if y%i !=j:
#             flag=False
#             break
#     if flag==True:
#         print(y)#2022040920220409
#         break
#     x+=1
