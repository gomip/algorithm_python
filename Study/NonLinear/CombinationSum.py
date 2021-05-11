from typing import List
import collections

# 2021.05.08 | gomip | created

class CombinationSum:
    def solution(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(csum, index, path):
            # 종료조건
            if csum < 0: return
            if csum == 0:
                result.append(path)
                return
            # 자신부터 하위 원소까지 나열 재귀 호출
            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])
        return result


if __name__ == '__main__':
    candid = [2, 3, 6, 7]
    sum = 7
    temp = CombinationSum()
    ans = temp.solution(candid, sum)
    print('answer : ', ans)