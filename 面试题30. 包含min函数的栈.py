class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.help_data = []

    def push(self, x: int) -> None:
        self.data.append(x)
        if not self.help_data or self.help_data[-1] > x:
            self.help_data.append(x)
        else:
            self.help_data.append(self.help_data[-1])

    def pop(self) -> None:
        if not self.data:
            raise Exception("no data")
        
        self.help_data.pop()
        return self.data.pop()


    def top(self) -> int:
        if not self.data:
            raise Exception("no data")
        
        return self.data[-1]


    def min(self) -> int:
        if not self.data:
            raise Exception("no data")

        return self.help_data[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()