# coding = utf-8

class MinStack(object):
    def __init__(self):
        super().__init__()
        self._data = []
        self._min_data = []

    def push(self, num):
        # 空直接添加
        if self.size() == 0:
            self._data.append(num)
            self._min_data.append(num)
        else:
            cur_min_num = self._min_data[-1]
            min_num = min(num, cur_min_num)
            self._data.append(num)
            self._min_data.append(min_num)
        return

    def pop(self):
        if self.size() == 0:
            raise Exception("Empty MinStack")
        self._data.pop()
        min_num = self._min_data.pop()
        return min_num

    def size(self):
        return len(self._data)
