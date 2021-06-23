from typing import List
import collections

# 2021.06.02 | gomip | created

class SingleNum:
    def solution(self, n: List[int]) -> int:
        result = 0
        for i in n:
            result ^= i
            print("result", result)
        return result

if __name__ == '__main__':
    n = [2,2,1]

    temp = SingleNum()
    ans = temp.solution(n)
    print("ans", ans)