from typing import List
import collections

# 21. 7. 1. | gomip | created

class FirstDartGame:
    def solution(self, dartResult: str) -> int:
        answer = 0
        queue = collections.deque(dartResult)
        temp = queue.popleft()
        num = []

        for i in range(len(queue)):
            if temp in ["S", "D", "T"]:
                print("h1", temp)
            elif temp in ["*", "#"]:
                print("h2", temp)
            else:
                num.append(int(temp))
            temp = queue.popleft()
        print("num", num)
        return answer


if __name__ == "__main__":
    dartResult = '1S2D*3T'
    ans = FirstDartGame().solution(dartResult)

    print("ans", ans)