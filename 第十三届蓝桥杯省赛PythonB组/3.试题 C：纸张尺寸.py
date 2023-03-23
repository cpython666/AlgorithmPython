s = input() 

t = int(s[-1]) # 最后一个数字也就是迭代的次数
w,h = 1189,841

for i in range(t):
    if w > h:
        w = w//2
    else:
        h = h//2
if w > h:
    print(w)
    print(h)
else:
    print(h)
    print(w)
