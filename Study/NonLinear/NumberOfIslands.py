# 2021.05.07 | gomip | created
# 섬의 개수
# 1을 육지로 0을 물로 가정한 2D 그리드 맵이 주어졌을때 섬의 개수를 계산하시오 (연결되어있는 1끼리는 한덩어리로 취급)
# input = [
#   11110
#   11010
#   11000
#   00000
# ]
# output = 1

from typing import List


class NumberOfIslands:
    def solution(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            # 더 이상 땅이 아닌 경우 예외처리
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
                return
            grid[i][j] = 0

            # 동서남북탐색
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)

        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count


if __name__ == '__main__':
    grid = [
        ['1', '1', '1', '1', '0'],
        ['1', '1', '0', '1', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '0', '0', '0']
    ]

    temp = NumberOfIslands()
    ans = temp.solution(grid)
    print('answer', ans)