from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        print(k)

testcase = Solution()
testcase.removeElement([3,2,2,3],3)
testcase.removeElement([0,1,2,2,3,0,4,2],2)
testcase.removeElement([7,6,6,7],7)