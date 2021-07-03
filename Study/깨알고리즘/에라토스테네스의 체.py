from typing import List
import collections
import math
# 21. 7. 3. | gomip | created

class isPrime:
    def solution(self, n: int) -> List[int]:
        answer = [True for i in range(n+1)]
        for i in range(2, int(math.sqrt(n)) + 1):
            if answer[i] == True:
                j = 2
                while i * j <= n:
                    answer[i * j] = False
                    j += 1

        return [i for i in range(2, n+1) if answer[i]]


if __name__ == "__main__":
    input = 100
    ans = isPrime().solution(input)
    print("ans", ans)