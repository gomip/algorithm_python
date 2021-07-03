from typing import List
import collections

# 21. 7. 3. | gomip | created

class SumOfNum:
    def solution(self, n: int) -> int :
        answer = 0
        for item in str(n):
            answer += int(item)
        return answer


if __name__ == "__main__":
    input = 123
    ans = SumOfNum().solution(input)
    print("ans", ans)