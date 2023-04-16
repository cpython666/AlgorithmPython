class Stack():
    def __init__(self):
        self.stk=[]
    def put(self,x):
        self.stk.append(x)
    def get(self):
        return self.stk.pop()
    def empty(self):
        return False if self.stk else True
class Stack1():
    def __init__(self,N=10**5):
        self.N=N
        self.stk=[0]*N
        self.cur=0
    def put(self,x):
        self.stk[self.cur]=x
        self.cur+=1
    def get(self):
        self.cur-=1
        return self.stk[self.cur]
    def empty(self):
        return False if self.cur else True

stack=Stack()
for i in range(5):
    stack.put(i)
while not stack.empty():
    print(stack.get(),end=' ')

stack1=Stack1()
for i in range(5):
    stack1.put(i)
while not stack1.empty():
    print(stack1.get(),end=' ')