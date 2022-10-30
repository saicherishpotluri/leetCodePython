from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # #silly solution
        # print(nums+nums)

        #proper solution
        ans = nums
        nums = nums[::-1] #reversing the array

        for i in range(len(nums)):
            ans.append(nums.pop())
        print(ans)

testcase = Solution()
testcase.getConcatenation([1,2,1])
testcase.getConcatenation([1,3,2,1])