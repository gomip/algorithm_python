from typing import List
import collections

# 21. 7. 3. | gomip | created

class StrToInt:
    def solution(self, s: str) -> int:
        return int(s)


if __name__ == "__main__":
    input = "1234"
    ans = StrToInt().solution(input)
    print("ans", ans)