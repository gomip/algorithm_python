from typing import List
import collections

# 21.07.04 | gomip | created

class SortString:
    def solution(self, strings: List[str], n: int) -> List[str]:
        # strings.sort(key=lambda x: x[n])
        answer = []
        for item in strings:
            item = item[n] + item
            answer.append(item)
        answer.sort()
        return [i[1:] for i in answer]


if __name__ == '__main__':
    strings = ["abce", "abcd", "cdx"]
    n = 2
    ans = SortString().solution(strings, n)
    print("ans", ans)