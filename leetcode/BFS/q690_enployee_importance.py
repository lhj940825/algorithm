'''
 * User: Hojun Lim
 * Date: 2021-01-07
'''

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        id2importance = {} # build hashmap
        for i in range(len(employees)):
            id2importance[employees[i].id] = (employees[i].importance, employees[i].subordinates)

        importance, subordinates = id2importance[id]

        from collections import deque
        subordinates = deque(subordinates)
        while subordinates: # bfs
            subordinate = subordinates.popleft()
            importance += id2importance[subordinate][0]
            subordinates.extend(id2importance[subordinate][1])


        return importance




