import bisect
from typing import List
import collections

# 2021.05.30 | gomip | created
# 정렬된 input을 받아 target에 해당하는 index 리턴


class BinarySearch:
    def solution_recursive(self, input: List[int], target: int) -> int:
        def binary_search(left, right):
            if left <= right:
                mid = (left+right)//2

                if input[mid] < target:
                    return binary_search(mid+1, right)
                elif input[mid] < target:
                    return binary_search(left, mid - 1)
                else:
                    return mid
            else:
                return -1

        return binary_search(0, len(input) - 1)

    def solution_loop(self, input: List[int], target:int) -> int:
        left, right = 0, len(input) -1
        while left <= right:
            mid = (left+right)//2

            if input[mid] < target:
                left = mid + 1
            elif input[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1

    def solution_bisect(self, input: List[int], target:int) -> int:
        index = bisect.bisect_left(input, target)
        print(index)
        if index < len(input) and input[index] == target:
            return index
        else:
            return -1

    def solution_index(self, input: List[int], target: int) -> int:
        try:
            return input.index(target)
        except ValueError:
            return -1


if __name__ == '__main__':
    input = [-1, 0, 3, 5, 9, 12]
    target = 9

    temp = BinarySearch()
    ans = temp.solution_recursive(input, target)
    print("ans1", ans)

    ans2 = temp.solution_bisect(input, target)
    print("ans2", ans2)