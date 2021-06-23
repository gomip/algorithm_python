from typing import List
import collections

# 2021.05.30 | gomip | created
# 겹치는 구간 병합


class MergeIntervals:
    def solution(self, input: List[List[int]]) -> List[List[int]]:
        ans = []
        for i in sorted(input, key=lambda x: x[0]):
            print("i", i)
            if ans and i[0] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], i[1])
            else:
                ans += i,   # 중첩 연산
        return ans


if __name__ == '__main__':
    input = [[1,3], [2,6], [8,10], [15,18]]

    temp = MergeIntervals()
    ans = temp.solution(input)
    print("input: ", ans)