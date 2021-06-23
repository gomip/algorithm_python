from typing import List
import collections

# 2021.06.08 | gomip | created

class MaximumSubarray:
    def solution(self, nums: List[int])-> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1] if nums[i-1] > 0 else 0
        return max(nums)
    

if __name__ == '__main__':
    input = [-2, 1, -3, 4, -1, 2, 1, -5, 5]

    temp = MaximumSubarray()
    ans = temp.solution(input)
    print("ans", ans)