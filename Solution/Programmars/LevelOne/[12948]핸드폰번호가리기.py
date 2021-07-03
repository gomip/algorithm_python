from typing import List
import collections
import re

# 21. 7. 3. | gomip | created

class HideNumber:
    def solution(self, phone_number: str) -> str:
        prefix = re.sub('\d', '*', phone_number[0: -4])
        suffix = phone_number[-4:]
        return prefix + suffix

if __name__ == "__main__":
    input = "01033334444"
    ans = HideNumber().solution(input)
    print("ans", ans)