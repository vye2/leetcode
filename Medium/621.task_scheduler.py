# You are given a char array representing tasks CPU need to do. It contains capital letters A to Z where each letter represents a different task. Tasks could be done without the original order of the array. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.
#
# However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.
#
# You need to return the least number of units of times that the CPU will take to finish all the given tasks.
#
#
#
# Example 1:
#
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation:
# A -> B -> idle -> A -> B -> idle -> A -> B
# There is at least 2 units of time between any two same tasks.
# Example 2:
#
# Input: tasks = ["A","A","A","B","B","B"], n = 0
# Output: 6
# Explanation: On this case any permutation of size 6 would work since n = 0.
# ["A","A","A","B","B","B"]
# ["A","B","A","B","A","B"]
# ["B","B","B","A","A","A"]
# ...
# And so on.
# Example 3:
#
# Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
# Output: 16
# Explanation:
# One possible solution is
# A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
#
#
# Constraints:
#
# The number of tasks is in the range [1, 10000].
# The integer n is in the range [0, 100]


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #sort tasklist by most occurrences to least in hashmap/dictionary.
        #loop through array, and then do greedy algorithm.

        D = {}
        # Wait = {}

        for task in tasks:
            if task not in D:
                D[task] = 1
                # Wait[task] = 0
            else:
                D[task]+=1


        most_frequent_task = max(D.values())
        how_many_with_tasks = len([k for k,v in D.items() if v == most_frequent_task])


        #A, B, C, A, B, C; n=2; best case scenario.
        #A, A, A; n=2; worst case scenario.
        #worst case would have A, I, I, A, I, I, A.
        #A, A, A, B, B, would have A, B, I, A, B, I, A.
        #this shows that in any other case, we could just replace I with the other characters.
        #how_many_with_tasks for this case: A, B, A, B; n = 2; -> A, B, I, A, B
        #n+1 because we include 'A' as well.
        idles = (most_frequent_task-1) * (n+1) + how_many_with_tasks

        return max(idles, len(tasks))
            
