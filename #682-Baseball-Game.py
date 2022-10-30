
from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for ops in operations:
            if ops == "+":
                stack.append(stack[-1] + stack[-2])
            elif ops == "D":
                stack.append(2 * stack[-1])
            elif ops == "C":
                stack.pop()
            else:
                stack.append(int(ops))
        print(sum(stack))

testcase = Solution()
print("Output:")
testcase.calPoints(["5","2","C","D","+"])
testcase.calPoints(["5","-2","4","C","D","9","+","+"])
testcase.calPoints(["1","C"])