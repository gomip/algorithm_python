from typing import List
import collections

# 21. 7. 3. | gomip | created

class CheckString:
    def solution(self, s: str) -> bool:
        answer = True
        if len(s) in [4, 6]:
            for c in s:
                if not c.isdigit():
                    answer = False
                    break
        else:
            answer = False
        return answer


if __name__ == "__main__":
    input = "a234"
    ans = CheckString().solution(input)
    print("ans" , ans)