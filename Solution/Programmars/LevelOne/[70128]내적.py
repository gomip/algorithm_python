from typing import List
import collections

# 2021.06.27 | gomip | created

class DotProduct:
    def solution(self, a: List[int], b:List[int]) -> int:
        answer = 0
        multiply = [i*j for i,j in zip(a,b)]
        for item in multiply:
            answer += item
        return answer
    

if __name__ == '__main__':
    a = [1, 2, 3, 4]
    b = [-3, -1, 0, 2]
    temp = DotProduct()
    ans = temp.solution(a, b)
    print(ans)