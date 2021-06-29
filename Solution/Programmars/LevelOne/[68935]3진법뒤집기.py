from typing import List
import collections

# 2021.06.27 | gomip | created

class Three:
    def solution(self, n: int) -> int:
        answer = 0
        temp = self.convert(n, 3)
        temp = str(temp)[::-1]
        return int(temp, 3)

    def convert(self, num: int, base: int) -> int:
        q, r = divmod(num, base)
        T = "0123456789ABCDEF"
        if q == 0:
            return T[r]
        else:
            return self.convert(q, base) + T[r]


if __name__ == '__main__':
    n = 45
    temp = Three()
    ans = temp.solution(n)
    print(ans)