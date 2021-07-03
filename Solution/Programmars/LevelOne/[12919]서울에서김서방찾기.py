from typing import List
import collections

# 21. 7. 3. | gomip | created

class FindKim:
    def solution(self, seoul: List[str]) -> str:
        answer = ''
        temp = seoul.index("Kim")
        return "김서방은 " + str(temp) + "에 있다"


if __name__ == "__main__":
    input = ["Jane", "Kim"]
    ans = FindKim().solution(input)
    print("ans", ans)