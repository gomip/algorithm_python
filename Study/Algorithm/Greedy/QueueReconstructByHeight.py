import heapq
from typing import List

# 2021.06.05 | gomip | created

# h = 사람의 키
# k = 현재 사람 앞에 있는 사람들 중 자신보다 큰 사람의 수
class QueueReconstructByHeight:
    def solution(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        for person in people:
            print("------------------------")
            print("person[0]", -person[0])
            print("person[1]", person[1])
            heapq.heappush(heap, (-person[0], person[1]))
            print("heap", heap)

        result = []
        while heap:
            print("===============")
            person = heapq.heappop(heap)
            result.insert(person[1], [-person[0], person[1]])
            print("result", result)
        return result


if __name__ == '__main__':
    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]

    temp = QueueReconstructByHeight()
    ans = temp.solution(people)
    print("ans", ans)