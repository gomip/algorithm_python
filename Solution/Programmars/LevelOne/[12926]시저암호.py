from typing import List
import collections

# 21. 7. 3. | gomip | created
# chr = 아스키코드 값을 입력받아 문자 리턴
# ord = 문자의 아스키 리턴

class Secret:
    def solution(self, s: str, n: int) -> str:
        temp = list(s)
        for i in range(len(temp)):
            if temp[i].isupper():
                temp[i] = chr((ord(temp[i]) - ord('A')+n) % 26 + ord('A'))
            elif temp[i].islower():
                temp[i] = chr((ord(temp[i]) - ord('a')+n) % 26 + ord('a'))
        return "".join(temp)


if __name__ == "__main__":
    input = "AB"
    n = 1
    ans = Secret().solution(input, n)
    print("ans", ans)