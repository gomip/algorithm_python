from typing import List
import collections

# 21. 7. 3. | gomip | created

class MakeStrangeWord:
    def solution(self, s: str) -> str:
        answer = ''
        temp = s.split(" ")
        for idx, item in enumerate(temp):
            for index, char in enumerate(item):
                if index % 2 == 0:
                    answer += char.upper()
                else:
                    answer += char.lower()
            if idx != len(temp) - 1:
                answer += ' '
        return answer


if __name__ == "__main__":
    input = "try hello world"
    ans = MakeStrangeWord().solution(input)
    print("ans", ans)