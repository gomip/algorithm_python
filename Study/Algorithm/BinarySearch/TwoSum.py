from typing import List
import collections
import bisect

# 2021.06.02 | gomip | created


class TwoSum:
    def solution_by_tp(self, n: List[int], t: int) -> List[int]:
        left, right = 0, len(n) - 1
        while not left == right:
            if n[left] + n[right] < t:
                left += 1
            elif n[left] + n[right] > t:
                right -= 1
            else:
                return left + 1, right + 1

    def solution_by_bisect(self, n: List[int], t: int) -> List[int]:
        for k, v in enumerate(n):
            left, right = k+1, len(n) -1
            expected = t - v

            while left <= right:
                mid = left + (right-left)//2
                print("n[mid[", n[mid])
                if n[mid] < expected:
                    left = mid + 1
                elif n[mid] > expected:
                    right = mid - 1
                else:
                    return k+1,mid+1

    def solution_by_bisect_slice(self, n: List[int], t: int) -> List[int]:
        for k,v in enumerate(n):
            expected = t - v
            i = bisect.bisect_left(n, expected, k+1)
            if i < len(n) and n[i] == expected:
                return k + 1, i +1


if __name__ == '__main__':
    n = [2,7,11,15]
    t = 9
    
    temp = TwoSum()
    ans = temp.solution_by_tp(n, t)
    print("ans", ans)

    ans2 = temp.solution_by_bisect(n,t)
    print("ans2", ans2)