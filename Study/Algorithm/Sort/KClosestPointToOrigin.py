from typing import List
import collections
import heapq

# 2021.05.30 | gomip | created

class KClosestPointsToOrigin:
    def solution(self, input: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for (x,y) in input:
            dist = x ** 2 + y ** 2
            print(dist)
            heapq.heappush(heap, (dist, x, y))

        result = []
        for _ in range(k):
            (dist, x, y) = heapq.heappop(heap)
            result.append((x,y))
        return result


if __name__ == '__main__':
    input = [[1,3], [-2,2]]
    k = 1

    temp = KClosestPointsToOrigin()
    ans = temp.solution(input,k)
    print("ans", ans)