from typing import List
import collections

# 21. 7. 3. | gomip | created

class SumOfMatrix:
    def solution(self, arr1: List[List[int]], arr2: List[List[int]]) -> List[List[int]]:
        answer = []
        for idx, item in enumerate(arr1):
            temp = []
            for j in range(len(item)):
                temp.append(item[j] + arr2[idx][j])
            answer.append(temp)
        return answer

    def solution_by_other(self, arr1: List[List[int]], arr2: List[List[int]]) -> List[List[int]]:
        answer = [[c + d for c, d in zip(a,b)] for a, b in zip(arr1, arr2)]
        return answer


if __name__ == "__main__":
    arr1 = [[1,2], [2,3]]
    arr2 = [[3,4], [5,6]]
    ans = SumOfMatrix().solution(arr1, arr2)
    print("ans", ans)