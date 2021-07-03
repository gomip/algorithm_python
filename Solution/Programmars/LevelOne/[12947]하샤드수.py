from typing import List
import collections

# 21. 7. 3. | gomip | created

class Hashard:
    def solution(self, x: int) -> bool:
        answer = True
        temp = 0
        for item in str(x):
            temp += int(item)
        if x % temp == 0:
            answer = True
        else:
            answer = False
        return answer

if __name__ == "__main__":
    input = 10
    ans = Hashard().solution(input)
    print("ans", ans)