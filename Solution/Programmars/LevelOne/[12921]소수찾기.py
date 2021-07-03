from typing import List
import collections

# 21. 7. 3. | gomip | created

class FindPrime:
    def solution(self, n: int) -> int:
        answer = 0
        temp = [False, False] + [True] * (n-1)
        for i in range(2, n+1):
            if temp[i]:
                for j in range(2*i, n+1, i):
                    temp[j] = False

        for item in temp:
            if item == True:
                answer += 1
        return answer


if __name__ == "__main__":
    input = 10
    ans = FindPrime().solution(input)
    print("ans", ans)