from typing import List
import collections

# 21. 6. 21. | gomip | created
# 내가 요청한 문서가 몇번째로 출력하는지 확인하는 문서
# 내가 요청한 문서 = location

class Printer:
    def solution(self, priorities: List[int], location: int):
        answer = 0
        queue = collections.deque(priorities)
        temp = queue.popleft()

        print("temp", temp, "priorities", queue)

        for item in queue:
            if item > temp:
                queue.append(temp)
            else:
                print("small", item)
            t = queue.popleft()
            # temp = t
        return answer


if __name__ == "__main__":
    priorities = [2, 1, 3, 2]
    location = 2

    temp = Printer()
    ans = temp.solution(priorities, location)
    print(ans)