from typing import List
import collections

# 2021.06.02 | gomip | created

class HammingDistance:
    def solution(self, x: int, y: int) -> int:
        return bin(x^y).count('1')

if __name__ == '__main__':
    x = 1
    y = 4

    temp = HammingDistance()
    ans = temp.solution(x,y)
    print("ans", ans)