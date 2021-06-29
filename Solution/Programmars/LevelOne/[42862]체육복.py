from typing import List
import collections

# 2021.06.27 | gomip | created

class LostCloth:
    def solution(self, n: int, lost: List[int], reserve: List[int]) -> int:
        answer = 0
        set_reserve = set(reserve) - set(lost)
        set_lost = set(lost) - set(reserve)

        for i in set_reserve:
            if i-1 in set_lost:
                set_lost.remove(i-1)
            elif i+1 in set_lost:
                set_lost.remove(i+1)

        return n-len(set_lost)

if __name__ == '__main__':
    n = 5
    lost = [2, 4]
    reserve = [1, 3, 5]
    temp = LostCloth()
    ans = temp.solution(n, lost, reserve)
    print(ans)