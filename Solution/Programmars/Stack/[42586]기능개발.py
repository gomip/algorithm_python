from typing import List
import math
import collections

# 21. 6. 19. | gomip | created

class DevProgress:
    # copy로 pop했던 값들 유
    def solution(self, progresses: List[int], speeds: List[int]) -> List[int]:
        answer = []
        remain = []
        # 각 기능별 남은 시간 계산
        for i in range(len(progresses)):
            remain.append(math.ceil((100 - progresses[i]) / speeds[i]))
        print(remain)
        # 그룹핑
        while len(remain) > 0:
            count = 1
            temp = remain.pop(0)
            print("temp", temp, "remain", remain)
            item = remain.copy()
            for i in range(len(remain)):
                if temp >= remain[i]:
                    count += 1
                    item.pop(0)
                else:
                    break
            answer.append(count)
            remain = item.copy()

        return answer

    def solution_two(self, progresses: List[int] , speeds: List[int]) -> List[int]:
        answer = []
        remain = []
        # 각 기능별 남은 시간 계산
        for i in range(len(progresses)):
            remain.append(math.ceil((100 - progresses[i]) / speeds[i]))
        print(remain)

        count = 0
        item = remain[0]
        for i in remain:
            if item < i:
                answer.append(count)
                item = i
                count = 0
            count += 1
        answer.append(count)
        return answer

if __name__ == "__main__":
    progresses = [93, 30, 55]
    # progresses = [95, 90, 99, 99, 80, 99]
    speeds = [1, 30, 5]
    # speeds = [1, 1, 1, 1, 1, 1]
    temp = DevProgress()
    ans = temp.solution(progresses, speeds)
    print(ans)

    ans2 = temp.solution_two(progresses, speeds)
    print(ans2)