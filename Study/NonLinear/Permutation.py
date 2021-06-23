# 2021.05.07 | gomip | created
import itertools
from typing import List


class Permutation:
    def solution(self, nums: List[int]) -> List[List[int]]:
        result = []
        prev_elements = []

        def dfs(elements):
            # 리프 노드에 도달하는 경우 result에 추가
            if len(elements) == 0:
                result.append(prev_elements[:])

            # 순열 재귀 호출
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)
                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        dfs(nums)
        return result

    def solutionLikePython(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))


if __name__ == '__main__':
    input = [1, 2, 3]
    temp = Permutation()
    ans1 = temp.solution(input)
    print('ans 1 : ', ans1)
    ans2 = temp.solutionLikePython(input)
    print('ans 2 : ', ans2)