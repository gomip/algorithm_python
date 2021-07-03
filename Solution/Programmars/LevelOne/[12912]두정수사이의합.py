from typing import List
import collections

# 21. 7. 3. | gomip | created

class SumOfDist:
    def solution(self, a:int, b: int) -> int:
        answer = 0
        if a > b:
            for i in range(b, a+1):
                answer += i
        else:
            for i in range(a, b+1):
                answer += i
        return answer


if __name__ == "__main__":
    a = 3
    b = 5
    ans = SumOfDist().solution(a, b)
    print("ans", ans)