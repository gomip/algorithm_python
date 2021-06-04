from typing import List
import collections

# 21. 6. 4. | gomip | created

class KthNum:
    def solution(self, array: List[int], commands: List[List[int]]):
        answer = []
        for i in range(len(commands)):
            temp = array[commands[i][0]-1:commands[i][1]]
            temp.sort()
            answer.append(temp[commands[i][2]-1])

        return answer

    def soltuin_programmars(self, array: List[int], commands: List[List[int]]):
        return list(map(lambda x: sorted(array[x[0] - 1:x[1]])[x[2] - 1], commands))


if __name__ == "__main__":
    arr = [1,5,2,6,3,7,4]
    commands = [[2,5,3],[4,4,1],[1,7,3]]

    temp = KthNum()
    ans = temp.solution(arr, commands)
    print("ans", ans)

    ans2 = temp.soltuin_programmars(arr, commands)
    print("ans2", ans2)