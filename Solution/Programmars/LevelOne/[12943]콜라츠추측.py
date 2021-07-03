from typing import List
import collections

# 21. 7. 3. | gomip | created

class Collatz:
    def solution(self, num: int) -> int:
        answer = 0
        if num == 1:
            return 0

        while True:
            if num % 2 == 0:
                num = num / 2
            else:
                num = num * 3 + 1
            answer += 1
            if num == 1:
                return answer
            elif answer == 500:
                return - 1

        return answer


if __name__ == "__main__":
    input = 626331
    ans = Collatz().solution(input)
    print("ans", ans)