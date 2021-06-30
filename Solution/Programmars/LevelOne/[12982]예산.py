from typing import List
import collections
import itertools

# 2021.06.27 | gomip | created

class Budget:
    def solution(self,d: List[int], budget: int) -> int:
        answer = 0
        d.sort()
        temp = 0

        for item in d:
            temp += item
            if temp <= budget:
                answer += 1
            else:
                break

        if answer < budget:
            answer = 0

        return answer
    

if __name__ == '__main__':
    d = [1, 3, 2, 5, 4]
    budget = 9
    ans = Budget().solution(d, budget)
    print(ans)