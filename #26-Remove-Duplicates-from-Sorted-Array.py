

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # print(nums)
        left_pointer = 1
        for right_pointer in range (1, len(nums)):
            if nums[right_pointer] != nums[right_pointer - 1]:
                nums[left_pointer] = nums[right_pointer]
                left_pointer += 1
        print(left_pointer)


test_case = Solution()
test_case.removeDuplicates([1,1,2])
test_case.removeDuplicates([0,0,1,1,1,2,2,3,3,4])

