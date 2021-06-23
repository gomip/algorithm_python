import bisect
from typing import List, Set
import collections

# 2021.05.31 | gomip | created

class IntersectionOfTwoArray:
    def solution_by_brute_force(self, nums1:List[int], nums2:List[int]) -> List[int]:
        result: Set = set()
        for i in nums1:
            for j in nums2:
                if i == j:
                    result.add(i)

        return result

    def solution_by_intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: Set = set()
        nums2.sort()
        for n1 in nums1:
            i2 = bisect.bisect_left(nums2, n1)
            print("i2", i2)
            print("n1", n1)
            print("num2", nums2)
            if len(nums2) > 0 and len(nums2) > i2 and n1 == nums2[i2]:
                result.add(n1)
                print("--------------------")
        return result

    def solution_by_two_pointer(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: Set = set()
        nums1.sort()
        nums2.sort()
        i = j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                result.add(nums1[i])
                i += 1
                j += 1
        return result


if __name__ == '__main__':
    nums1 = [1,2,4,1,3]
    nums2 = [2,3,5]

    temp = IntersectionOfTwoArray()
    ans = temp.solution_by_brute_force(nums1, nums2)
    print("ans", ans)

    ans2 = temp.solution_by_intersection(nums1, nums2)
    print("ans2", ans2)