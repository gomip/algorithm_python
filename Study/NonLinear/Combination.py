import itertools
from typing import List
import collections

# 2021.05.08 | gomip | created

class Combination:
    def solution(self,n: int, k: int) -> List[List[int]]:
        results = []

        def dfs(elements, start: int, k: int):
            if k == 0:
                results.append(elements[:])
                return
            for i in range(start, n+1):
                elements.append(i)
                dfs(elements, i+1, k-1)
                elements.pop()
        dfs([], 1, k)
        return results

    def solutionLikePython(self, n: int, k: int):
        return list(itertools.combinations(range(1, n + 1), k))


if __name__ == '__main__':
    n = 4
    k = 2
    temp = Combination()
    ans = temp.solution(n, k)
    print(ans)

    ans2 = temp.solutionLikePython(n,k)
    print(ans2)