class CustomStack:

    def __init__(self, maxSize: int):
        self.size=maxSize
        self.stack=[]

    def push(self, x: int) -> None:
        n=len(self.stack)
        if n<self.size:
            self.stack.append(x)

    def pop(self) -> int:
        n=len(self.stack)
        if n>0:
            x = self.stack[-1];
            self.stack.pop()
            return x
        return -1

    def increment(self, k: int, val: int) -> None:
        n=min(k,len(self.stack))
        for i in range(n):
            self.stack[i]+=val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)