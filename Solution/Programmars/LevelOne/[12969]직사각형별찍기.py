from typing import List
import collections

# 21. 7. 3. | gomip | created

class SquareStar:
    def solution(self, input: str) -> str:
        answer = ''
        a, b = map(int, input.strip().split(' '))

        for i in range(b):
            for j in range(a):
                print("*", end = '')
            print("")
        return answer


if __name__ == "__main__":
    input = "5 3"
    ans = SquareStar().solution(input)
    print("ans", ans)