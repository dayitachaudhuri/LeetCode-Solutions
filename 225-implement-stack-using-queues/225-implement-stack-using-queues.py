class MyStack:

    def __init__(self):
        self.data=[]
        self.temp=[]
        self.rear=-1

    def push(self, x: int) -> None:
        self.data.append(x)
        self.rear+=1

    def pop(self) -> int:
        for i in range(0,self.rear):
            self.temp.append(self.data.pop(0))
        val=self.data.pop()
        self.data=self.temp
        self.temp=[]
        self.rear-=1
        return val

    def top(self) -> int:
        return self.data[self.rear]

    def empty(self) -> bool:
        if self.rear==-1:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()