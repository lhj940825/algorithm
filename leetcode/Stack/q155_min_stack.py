'''
 * User: Hojun Lim
 * Date: 2021-02-16
'''
import sys

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = sys.maxsize

    def push(self, x: int) -> None:

        self.stack.append(x)
        if x < self.min:
            self.min = x

        return None

    def pop(self) -> None:
        pop_item = self.stack.pop()
        if pop_item == self.min:
            if self.stack:
                self.min = min(self.stack)
            else:
                self.min = sys.maxsize

        return pop_item

    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.min
