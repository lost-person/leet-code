class CQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.size = 0

    def appendTail(self, value: int) -> None:
        while self.stack1:
            self.stack2.append(self.stack1.pop())

        self.stack1.append(value)
        while self.stack2:
            self.stack1.append(self.stack2.pop())

        self.size += 1

    def deleteHead(self) -> int:
        if self.size <= 0:
            return -1

        self.size -= 1
        return self.stack1.pop()


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()