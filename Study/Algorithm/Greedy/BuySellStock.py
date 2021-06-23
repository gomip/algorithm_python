from typing import List

# 2021.06.05 | gomip | created

class BuySellStock:
    def solution(self, nums: List[int]) -> int:
        result = 0

        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]:
                result += nums[i + 1] - nums[i]

        return result

if __name__ == '__main__':
    nums = [7, 1, 5, 3, 6, 4]

    temp = BuySellStock()
    ans = temp.solution(nums)
    print("ans", ans)