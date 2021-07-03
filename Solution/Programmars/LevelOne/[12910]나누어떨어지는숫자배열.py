from typing import List
import collections

# 21. 7. 3. | gomip | created

class DivideArray:
    def solution(self, arr: List[int], divisor: int) -> List[int]:
        answer = []
        for item in arr:
            if item % divisor == 0:
                answer.append(item)
        if len(answer) == 0:
            answer.append(-1)
        answer.sort()
        return answer


if __name__ == "__main__":
    input = [5, 9, 7, 10]
    divisor = 5
    ans = DivideArray().solution(input, divisor)
    print("ans", ans)