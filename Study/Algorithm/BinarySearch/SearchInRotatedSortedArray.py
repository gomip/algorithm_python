from typing import List
import collections

# 2021.05.30 | gomip | created


class SearchInRotatedSortedArray:
    def solution(self, nums: List[int], target: int) -> int:
        # 예외 처리
        if not nums:
            return -1

        # 최솟값을 찾아 피벗 설정
        left, right = 0, len(nums) - 1
        i = 0
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > right:
                left = mid + 1
            else:
                right = mid
        pivot = left

        # 피벗 기준 이진검색
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            mid_pivot = (mid + pivot) % len(nums)

            if nums[mid_pivot] < target:
                left = mid+1
            elif nums[mid_pivot] > target:
                right = mid -1
            else:
                return mid_pivot
        return -1


if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    target =1

    temp = SearchInRotatedSortedArray()
    ans = temp.solution(nums, target)
    print(ans)