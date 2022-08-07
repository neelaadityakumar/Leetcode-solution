class Solution(object):
    def taskSchedulerII(self, tasks, space):
        """
        :type tasks: List[int]
        :type space: int
        :rtype: int
        """
        #tasks = [5,8,8,5], space = 2
        day_count = 0
        task_counter = {}
        
        for i in tasks:
            task_counter[i] = -1
        
        for task in tasks:
            if task_counter[task] == -1 or day_count - task_counter[task]  > space:
                task_counter[task] = day_count
            else:
                day_count += (space - (day_count - task_counter[task] - 1))
                task_counter[task] = day_count
            day_count += 1
        return day_count
                
            