from typing import List
import collections

# 21. 7. 3. | gomip | created

class RepeatChar:
    def solution(self, n: int) -> str:
        answer = ''
        for i in range(n):
            print("i", i)
            if i % 2 == 0:
                answer += '수'
            else:
                answer += '박'
        return answer


if __name__ == "__main__":
    input = 3
    ans = RepeatChar().solution(input)
    print("ans", ans)