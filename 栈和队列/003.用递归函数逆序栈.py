from queue import LifoQueue

stack=LifoQueue()
for i in range(10):
    stack.put(i)
print(stack.queue)
def getAndRemoveLast(stack):
    tmp_lst=stack.get()
    if stack.empty():
        return tmp_lst
    last=getAndRemoveLast(stack)
    stack.put(tmp_lst)
    return last

def reverceStack(stack):
    if stack.empty():
        return '栈为空'
    last=getAndRemoveLast(stack)
    reverceStack(stack)
    stack.put(last)

reverceStack(stack)

print(stack.queue)