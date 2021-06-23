from typing import List
import collections

# 2021.03.18 | gomip | created

class Node:
    # item : 노드의 값
    # next : 다음 노드를 가리키는 포인터
    def __init__(self, item, next):
        self.item = item
        self.next = next

class Stack:
    def __init__(self):
        self.last = None

    def push(self, item):
        self.last = Node(item, self.last)

    def pop(self):
        item = self.last.item
        self.last = self.last.next
        return item


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    for _ in range(3):
        print(stack.pop())
