from typing import List
import collections

# 21. 7. 3. | gomip | created

class SumOfDivisor:
    def solution(self, n: int) -> int:
        answer = 0
        temp = []
        for i in range(1,n+1):
            if n % i == 0:
                answer += i

        return answer


if __name__ == "__main__":
    input = 12
    ans = SumOfDivisor().solution(input)
    print("ans", ans)