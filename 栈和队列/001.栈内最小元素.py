# 构造一个可以获取站内最小元素的栈

# 可以使用现有的栈

from queue import LifoQueue

class GetMinStack1():
    """
    a self-defined stack with get min function
    """
    def __init__(self):
        self.stack=LifoQueue()
        self.minStack=LifoQueue()

    def put(self,x):
        self.stack.put(x)
        if self.minStack.empty():
            self.minStack.put(x)
        else:
            if x<=self.getMin():
                self.minStack.put(x)

    def get(self):
        if self.stack.empty():
            raise Exception('栈为空！')
        tmp=self.stack.get()
        if tmp==self.getMin():
            self.minStack.get()
        return tmp

    def getMin(self):
        if self.minStack.empty():
            raise Exception("栈为空！")
        top=self.minStack.get()
        self.put(top)
        return top

getMinStack=GetMinStack1()
getMinStack.put(3)
getMinStack.put(4)
getMinStack.put(5)
getMinStack.put(1)
getMinStack.put(2)
getMinStack.put(1)
while not getMinStack.minStack.empty():
    print(getMinStack.minStack.get())
print('-'*20)
class GetMinStack2():
    def __init__(self):
        self.stack=LifoQueue()
        self.minStack=LifoQueue()
    def get(self):
        if self.stack.empty():
            raise Exception('栈为空！')
        tmp=self.stack.get()
        self.minStack.get()
        return tmp
    def put(self,x):
        self.stack.put(x)
        if self.minStack.empty():
            self.minStack.put(x)
        else:
            self.minStack.put(min(self.getMin(),x))
    def getMin(self):
        if self.minStack.empty():
            raise Exception('栈为空！')
        top=self.minStack.get()
        self.minStack.put(top)
        return top

getMinStack=GetMinStack2()
getMinStack.put(3)
getMinStack.put(4)
getMinStack.put(5)
getMinStack.put(1)
getMinStack.put(2)
getMinStack.put(1)
while not getMinStack.minStack.empty():
    print(getMinStack.minStack.get())
