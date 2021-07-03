from typing import List
import collections

# 21.07.04 | gomip | created

class GcdLcm:
    def solution(self, n: int, m: int) -> List[int]:
        answer = []
        g = self.gcd(n, m)
        l = self.lcm(n, m, g)

        answer.append(g)
        answer.append(int(l))
        return answer

    def gcd(self, a: int, b: int) -> int:
        while b > 0:
            a, b = b, a % b
        return a

    def lcm(self, a: int, b: int, gcd: int) -> float:
        return a * b / gcd


if __name__ == '__main__':
    n = 3
    m = 12
    ans = GcdLcm().solution(n, m)
    print("ans", ans)