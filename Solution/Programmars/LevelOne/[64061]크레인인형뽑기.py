from typing import List
import collections

# 21. 6. 23. | gomip | created


class Crane:
    def checkValue(self, item: int) -> int:
        
        return 0

    def solution(self, board: List[List[int]], moves: List[int]) -> int:
        answer = 0
        board.reverse()
        basket = []
        col = len(board[0])

        for item in moves:
            for row in range(col):
                temp = self.checkValue(board[row][item-1])


        return answer


if __name__ == "__main__":
    input = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    moves = [1,5,3,5,1,2,1,4]
    temp = Crane()
    ans = temp.solution(input, moves)
    print(ans)
