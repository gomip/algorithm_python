from typing import List
import collections

# 2021.06.05 | gomip | created

class TaskScheduler:
    def solution(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        result = 0

        while True:
            sub = 0

            # 개수 순 추출
            for task, _ in counter.most_common(n + 1):
                sub += 1
                result += 1

                counter.subtract(task)
                # 0 이하인 아이템을 목록에서 제거
                counter += collections.Counter()

            if not counter:
                break

            result += n - sub + 1
        return result


if __name__ == '__main__':
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2

    temp = TaskScheduler()
    ans = temp.solution(tasks, n)
    print("ans", ans)