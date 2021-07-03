from typing import List
import collections

# 21. 7. 3. | gomip | created

class ReverseString:
    def solution(self, s: str) -> str:
        lower = []
        upper = []

        for c in s:
            if c.islower():
                lower.append(c)
            else:
                upper.append(c)
        lower.sort(reverse=True)
        upper.sort(reverse=True)
        return "".join(lower) + "".join(upper)


if __name__ == "__main__":
    input = "Zbcdefg"
    ans = ReverseString().solution(input)
    print("ans", ans)