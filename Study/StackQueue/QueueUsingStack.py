from typing import List
import collections

# 2021.04.18 | gomip | created
# push | pop | peek | empty

class QueueUsingStack:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self,x):
        self.input.append(x)

    def pop(self):
        self.peek()
        return self.output.pop()

    def peek(self):
        # output이 없으면 모두 재입력
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self):
        return self.input == [] and self.output == []


if __name__ == '__main__':
    temp = QueueUsingStack()
    temp.push(1)
    temp.push(2)
    print(temp.peek())
    print(temp.pop())
    print(temp.empty())