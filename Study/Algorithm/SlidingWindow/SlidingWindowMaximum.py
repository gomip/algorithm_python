from typing import List
import collections
# 2021.06.05 | gomip | created

class SlidingWindowMaximum:
    def solution(self, nums: List[int], k: int) -> List[int]:
        # 배열이 없을경우 return
        if not nums:
            return nums

        r = []
        for i in range(len(nums) - k + 1):
            # print("i", i)
            # print("check", nums[i:i + k])
            r.append(max(nums[i:i + k]))
        return r

    # 슬라이딩은 최적화가 어려우니 max값 구하는것을 최적화하자
    def solution_Queue(self, nums: List[int], k:int) -> List[int]:
        result = []
        window = collections.deque()
        current = float('-inf')
        for i,v in enumerate(nums):
            window.append(v)
            print("i", i, "v", v)
            if i < k-1:
                print("check", i, v)
                continue

            # 새로추가된 값이 기존 최대값보다 큰 경우 교체, 처음에는 그냥 무한값으로 한다.
            if current == float('-inf'):
                current = max(window)
                print("im here", current)
            elif v > current:
                current = v
                print("no im here", current)

            result.append(current)

            # 최대값이 윈도우에서 빠지면 초기화
            if current == window.popleft():
                current = float('-inf')
        return result


if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    temp = SlidingWindowMaximum()
    ans = temp.solution(nums, k)
    print("ans", ans)

    ans2 = temp.solution_Queue(nums,k)
    print("ans2", ans)