from typing import List
import collections

# 2021.04.18 | gomip | created
# push | pop | top | empty


class StackUsingQueue:
    def __init__(self):
        self.q = collections.deque()

    def push(self,x):
        self.q.append(x)
        # 요소 삽입 후 맨 앞에 두는 상태로 재 정렬
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0


if __name__ == '__main__':
    temp = StackUsingQueue()
    temp.push(1)
    temp.push(2)
    print(temp.pop())
    print(temp.top())
    print(temp.empty())