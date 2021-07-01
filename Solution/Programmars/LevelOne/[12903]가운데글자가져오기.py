from typing import List
import collections
import math

# 21. 7. 1. | gomip | created

class ReturnCenterCharacter:
    def solution(self, s: str) -> str:
        answer = ''
        mid = int(len(s) / 2)

        if len(s) % 2 == 0:
            answer += s[mid-1]
            answer += s[mid]
        else:
            answer += s[mid]

        return answer



if __name__ == "__main__":
    s = "abce"
    ans = ReturnCenterCharacter().solution(s)
    print("ans", ans)