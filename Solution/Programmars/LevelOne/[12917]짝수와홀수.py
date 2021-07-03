from typing import List
import collections

# 21. 7. 3. | gomip | created

class OddOrEven:
    def solution(self, num: int) -> str:
        answer = ''
        if num % 2 == 0 :
            answer = "Even"
        else:
            answer = "Odd"
        return answer


if __name__ == "__main__":
    input = 3
    ans = OddOrEven().solution(input)
    print("ans", ans)