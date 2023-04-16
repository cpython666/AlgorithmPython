from queue import LifoQueue
# Last In First Out 后进先出
stack=LifoQueue()
for i in range(5):
    stack.put(i)
while not stack.empty():
    print(stack.get(),end=' ')