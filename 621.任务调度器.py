#
# @lc app=leetcode.cn id=621 lang=python3
#
# [621] 任务调度器
#

# @lc code=start
from queue import PriorityQueue
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0

        if not n:
            return len(tasks)

        # 统计任务的个数
        task_dict = dict()
        for task in tasks:
            task_dict[task] = task_dict.get(task, 0) + 1

        task_sort = sorted(task_dict.items(), key=lambda x: x[1], reverse=True)

        max_task_cnt = task_sort[0][1]
        res = (max_task_cnt - 1) * (n + 1)

        for task in task_sort:
            if task[1] == max_task_cnt:
                res += 1

        return res if res >= len(tasks) else len(tasks)
        # 优先队列（每种任务的任务数为优先级）
        # queue = PriorityQueue()
        # for task, task_cnt in task_dict.items():
        #     if task_cnt != 0:
        #         queue.put((-task_cnt, task))

        # time = 0
        # while not queue.empty():
        #     i = 0
        #     tmp_task = []
        #     while i <= n:
        #         if not queue.empty():
        #             task = queue.get()
        #             if task[0] < -1:
        #                 tmp_task.append((task[0] + 1, task[1]))
        #         time += 1
        #         if queue.empty() and not tmp_task:
        #             break
        #         i += 1
        #     for task in tmp_task:
        #         queue.put(task)

        # return time


# @lc code=end
