from typing import List
import collections

# 21. 6. 23. | gomip | created


class Crane:
    def checkValue(self, item: int) -> int:
        
        return 0

    def solution(self, board: List[List[int]], moves: List[int]) -> int:
        answer = 0
        stack = [0]

        for item in moves:
            for b in board:
                if b[item-1] != 0:
                    if stack[-1] == b[item-1]:
                        stack.pop()
                        answer += 2
                    else:
                        stack.append(b[item-1])
                    b[item-1] = 0
                    break

        return answer


if __name__ == "__main__":
    input = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    moves = [1,5,3,5,1,2,1,4]
    temp = Crane()
    ans = temp.solution(input, moves)
    print(ans)
