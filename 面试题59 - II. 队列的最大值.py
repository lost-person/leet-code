# coding = utf-8


class MaxQueue(object):
    def __init__(self):
        from collections import deque
        self.que = deque()
        self.sort_que = deque()

    def max_value(self):
        """
        :rtype: int
        """
        return self.sort_que[0] if self.sort_que else -1

    def push_back(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.que.append(value)
        while self.sort_que and self.sort_que[-1] < value:
            self.sort_que.pop()
        self.sort_que.append(value)

    def pop_front(self):
        """
        :rtype: int
        """
        if not self.que: return -1
        res = self.que.popleft()
        if res == self.sort_que[0]:
            self.sort_que.popleft()
        return res
