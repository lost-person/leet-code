# coding = utf-8

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = MaxHeap(10000)
        self.min_heap = MinHeap(10000)

    def addNum(self, num: int) -> None:
        self.max_heap.insert(num)
        self.min_heap.insert(self.max_heap.extract_max())
        if self.max_heap.size() < self.min_heap.size():
            self.max_heap.insert(self.min_heap.extract_min())

    def findMedian(self) -> float:
        if self.max_heap.size() == self.min_heap.size():
            return (self.max_heap.data[1] + self.min_heap.data[1]) / 2
        else:
            return self.max_heap.data[1]


class MaxHeap:
    def __init__(self, capacity):
        super().__init__()
        self.data = [0] * (capacity + 1)
        self.cnt = 0
        self.capacity = capacity
    
    def size(self) -> int:
        return self.cnt

    def is_full(self) -> bool:
        return self.cnt == self.capacity

    def is_empty(self) -> bool:
        return self.cnt == 0
    
    def insert(self, num):
        """插入
        """
        if self.is_full():
            raise Exception('MaxHeap Capacity Exceed!')
        self.cnt += 1
        self.data[self.cnt] = num
        self.__swim(self.cnt)
    
    def extract_max(self) -> int:
        if self.is_empty():
            raise Exception('MaxHeap is Empty')
        num = self.data[1]
        self.data[1], self.data[self.cnt] = self.data[self.cnt], self.data[1]
        self.cnt -= 1
        # self.data.pop()
        self.__sink(1)
        return num
    
    def __swim(self, index):
        """上浮
        """
        tmp = self.data[index]
        while index > 1 and self.data[index >> 1] < tmp:
            self.data[index] = self.data[index >> 1]
            index >>= 1
        self.data[index] = tmp
    
    def __sink(self, index):
        """下沉
        """
        tmp = self.data[index]
        while index << 1 <= self.cnt:
            j = index << 1
            # 右孩子存在，且右孩子比左孩子大
            if j + 1 <= self.cnt and self.data[j + 1] > self.data[j]:
                j += 1
            if tmp >= self.data[j]:
                break
            self.data[index] = self.data[j]
            index = j
        self.data[index] = tmp


class MinHeap:
    def __init__(self, capacity):
        super().__init__()
        self.data = [0] * (capacity + 1)
        self.cnt = 0
        self.capacity = capacity
    
    def size(self) -> int:
        return self.cnt

    def is_full(self) -> bool:
        return self.cnt == self.capacity

    def is_empty(self) -> bool:
        return self.cnt == 0
    
    def insert(self, num):
        """插入
        """
        if self.cnt + 1 > self.capacity:
            raise Exception('MinHeap Capacity Exceed!')
        self.cnt += 1
        self.data[self.cnt] = num
        self.__swim(self.cnt)
    
    def extract_min(self) -> int:
        if self.is_empty():
            raise Exception('MinHeap is Empty')
        num = self.data[1]
        self.data[1], self.data[self.cnt] = self.data[self.cnt], self.data[1]
        self.cnt -= 1
        # self.data.pop()
        self.__sink(1)
        return num
    
    def __swim(self, index):
        """上浮
        """
        tmp = self.data[index]
        while index > 1 and self.data[index >> 1] > tmp:
            self.data[index] = self.data[index >> 1]
            index >>= 1
        self.data[index] = tmp
    
    def __sink(self, index):
        """下沉
        """
        tmp = self.data[index]
        while index << 1 <= self.cnt:
            j = index << 1
            # 右孩子存在，且右孩子比左孩子大
            if j + 1 <= self.cnt and self.data[j + 1] < self.data[j]:
                j += 1
            if tmp <= self.data[j]:
                break
            self.data[index] = self.data[j]
            index = j
        self.data[index] = tmp

# if __name__ == "__main__":
#     median_finder = MedianFinder()
#     median_finder.addNum(1)
#     median_finder.addNum(2)
#     median_finder.addNum(3)
#     median_finder.addNum(4)
#     median_finder.addNum(5)
#     median_finder.addNum(6)
#     median_finder.addNum(7)
#     print(median_finder.findMedian())

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

