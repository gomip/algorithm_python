from typing import List
import collections

# 21. 7. 3. | gomip | created

class NumOfPandY:
    def solution(self, s: str) -> bool:
        answer = True
        cnt_p = 0
        cnt_y = 0
        for c in s:
            if c == 'p' or c == 'P':
                cnt_p += 1
            elif c == 'y' or c == 'Y':
                cnt_y += 1

        if cnt_p == cnt_y:
            answer = True
        else:
            answer = False

        return answer


if __name__ == "__main__":
    input = "pPoooyY"
    ans = NumOfPandY().solution(input)
    print("ans", ans)