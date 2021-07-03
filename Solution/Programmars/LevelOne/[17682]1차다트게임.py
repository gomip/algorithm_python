from typing import List
import collections
import re
# 21. 7. 1. | gomip | created

class FirstDartGame:
    def solution(self, dartResult: str) -> int:
        answer = 0
        # queue = collections.deque(dartResult)

        num = [int(i) for i in re.findall('\d+', dartResult)]
        symbol = re.sub("\d+", "", dartResult)

        idx = 0
        print("num", num[idx])
        for item in symbol:
            if item == "S":
                num[idx] = num[idx] ** 1
                idx += 1
            elif item == "D":
                num[idx] = num[idx] ** 2
                idx += 1
            elif item == "T":
                num[idx] = num[idx] ** 3
                idx += 1
            elif item == "*":
                if idx == 1:
                    num[idx-1] = num[idx-1] * 2
                else:
                    num[idx-1] = num[idx-1] * 2
                    num[idx-2] = num[idx-2] * 2
            elif item == "#":
                num[idx-1] = num[idx-1] * -1
        for item in num:
            answer += item
        return answer


if __name__ == "__main__":
    dartResult = '1S*2T*3S'
    ans = FirstDartGame().solution(dartResult)

    print("ans", ans)