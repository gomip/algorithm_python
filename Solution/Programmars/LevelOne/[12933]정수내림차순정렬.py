from typing import List
import collections

# 21. 7. 3. | gomip | created

class SortInteger:
    def solution(self,n :int) -> int:
        answer = 0
        temp = str(n)
        arr = []
        for i in range(len(temp)):
            arr.append(temp[i])
        arr.sort(reverse=True)

        return int("".join(arr))


if __name__ == "__main__":
    n = 118372
    ans = SortInteger().solution(n)
    print("ans", ans)