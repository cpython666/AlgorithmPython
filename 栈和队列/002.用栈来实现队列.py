from queue import LifoQueue
class TwoStacksQueue():
    def __init__(self):
        self.pushStack=LifoQueue()
        self.popStack=LifoQueue()

    def put(self,x):
        self.pushStack.put(x)

    def get(self):
        if self.pushStack.empty() and self.popStack.empty():
            raise Exception('队列为空！')
        if self.popStack.empty():
            while not self.pushStack.empty():
                self.popStack.put(self.pushStack.get())
            return self.popStack.get()
    def top(self):
        if self.pushStack.empty() and self.popStack.empty():
            raise Exception('队列为空！')
        if self.popStack.empty():
            while not self.pushStack.empty():
                self.popStack.put(self.pushStack.get())
            return self.popStack.queue[-1]