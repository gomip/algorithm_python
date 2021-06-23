from typing import List
from itertools import chain, combinations
import collections

# 21. 6. 19. | gomip | created

class Spy:
    def solution(self, clothes: List[List[str]]) -> int:
        answer = 1
        temp_map = {}

        for kind, cloth in clothes:
            print(kind, cloth)
            if cloth not in temp_map:
                temp_map[cloth] = 1
            else:
                temp_map[cloth] += 1

        for item in temp_map.values():
            answer *= (item + 1)
        return answer-1

    def solution_two(self, clothes: List[List[str]]) -> int:
        answer = 1
        cnt = collections.Counter(kind for name, kind in clothes)

        for item in cnt.values():
            print(item)
            answer *= (item+1)
        return answer -1


if __name__ == "__main__":
    input = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
    temp = Spy()
    ans = temp.solution(input)
    print(ans)

    ans2 = temp.solution_two(input)
    print(ans2)