from typing import List
import collections

# 21. 7. 2. | gomip | created

class RemoveSmallest:
    def solution(self, arr: List[int]) -> List[int]:
        # arr.sort()
        # answer = collections.deque(arr)
        # if len(arr) == 1:
        #     answer[0] = -1
        # else:
        #     answer.popleft()
        # answer.reverse()

        if len(arr) == 1:
            # 배열의 크기가 1보다 작으면 -1을 넣어준다
            arr.append(-1)
        else:
            # arr에서 가장 작은 값을 조회해서 해당 값을 제거
            temp = min(arr)
            arr.remove(temp)
        return arr


if __name__ == "__main__":
    arr = [4, 3, 2, 1]
    # arr = [10]
    ans = RemoveSmallest().solution(arr)
    print("ans", ans)