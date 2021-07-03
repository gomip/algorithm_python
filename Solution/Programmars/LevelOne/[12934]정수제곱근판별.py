from typing import List
import collections
import math
# 21. 7. 3. | gomip | created

class isSquare:
    def solution(self,n : int) -> int:
        answer = 0
        temp_sqrt = math.sqrt(n)
        check = temp_sqrt % 1

        if check <= 0.0:
            answer = math.pow(temp_sqrt + 1, 2)
        else:
            answer = -1
        return int(answer)


if __name__ == "__main__":
    n = 121

    ans = isSquare().solution(n)
    print("ans", ans)