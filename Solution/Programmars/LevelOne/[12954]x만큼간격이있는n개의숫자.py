from typing import List
import collections

# 21. 7. 3. | gomip | created

class DistOfNumb:
    def solution(self, x:int, n: int) -> List[int]:
        answer = []
        for i in range(n):
            answer.append(x+x*i)
        return answer


if __name__ == "__main__":
    x = 2
    n = 5
    ans = DistOfNumb().solution(x, n)
    print("ans", ans)