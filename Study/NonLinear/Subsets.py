from typing import List
import collections

# 2021.05.08 | gomip | created

class Subsets:
    def solution(self, nums : List[int]) -> List[List[int]]:
        results = []

        def dfs(index, path):
            results.append(path)

            for i in range(index, len(nums)):
                dfs(i+1, path + [nums[i]])

        dfs(0, [])
        return results


if __name__ == '__main__':
    input = [1, 2, 3]
    temp = Subsets()
    ans = temp.solution(input)
    print(ans)