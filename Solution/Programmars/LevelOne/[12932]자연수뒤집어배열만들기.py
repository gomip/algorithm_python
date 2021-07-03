from typing import List
import collections

# 21. 7. 3. | gomip | created
# str()[::-1] 은 숫자를 뒤집어 준다.

class ReverseNumber:
    def solution(self, n: int) -> List[int]:
        answer = []
        temp = str(n)[::-1]
        for item in temp:
            answer.append(int(item))
        return answer


if __name__ == "__main__":
    n = 12345
    ans = ReverseNumber().solution(n)
    print("ans", ans)