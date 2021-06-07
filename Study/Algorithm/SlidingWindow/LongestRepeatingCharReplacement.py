import collections
from typing import List

# 2021.06.05 | gomip | created

class LongestRepeatingCharReplacement:
    def solution(self, s: str, k: int) -> int:
        left = right = 0
        counts = collections.Counter()
        # 우측 포인터는 계속해서 오른쪽으로 이동
        for right in range(1, len(s) + 1):
            # 카운터를 통해 가장 흔히 등장하는 문자의 값을 구한다
            counts[s[right - 1]] += 1
            print("========= right", right, "=========")
            print("right-1", right-1)
            print("s[right-1]", s[right-1])
            print("counts", counts)

            # 가장 흔하게 등장하는 문자 탐색
            # (1) counts에 있는 첫번째 요소. [('A',3)]
            # [0] ('A', 3)
            # [1] 3
            max_char = counts.most_common(1)[0][1]

            # k 초과시 왼쪽 이동
            if right - left - max_char > k:
                print("s[left]", s[left])
                print("before", counts)
                counts[s[left]] -= 1
                print("after", counts)
                left += 1
                print("left", left)
        return right - left


if __name__ == '__main__':
    s = "AAABBC"
    k = 2

    temp = LongestRepeatingCharReplacement()
    ans = temp.solution(s, k)
    print("ans", ans)