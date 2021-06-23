from typing import List
import collections

# 2021.04.18 | gomip | created

class CircularQueue:
    def __init__(self, k: int):
        self.q = [None] * k
        self.maxlen = k
        self.p1 = 0                 # front
        self.p2 = 0                 # rear

    def enQueue(self, value: int) -> bool:
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            self.p2 = (self.p2 + 1) % self.maxlen           # rear 포인터가 전체 길이를 넘어가지 않도록 하기 위해
            return True
        else :
            return False

    def deQueue(self) -> bool:
        if self.q[self.p1] is None:
            return False
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1 + 1) % self.maxlen
            return True

    def Front(self) -> int:
        return -1 if self.q[self.p1] is None else self.q[self.p1]

    def Rear(self) -> int:
        return -1 if self.q[self.p2-1] is None else self.q[self.p2-1]

    def isEmpty(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is None

    def isFull(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is not None


if __name__ == '__main__':
    temp = CircularQueue(5)
    temp.enQueue(10)
    temp.enQueue(20)
    temp.enQueue(30)
    temp.deQueue()
    temp.enQueue(25)
    print('1', temp.Rear())
    print('2', temp.Front())
    temp.enQueue(50)
    temp.enQueue(100)
    print('3', temp.Rear())
    print('4', temp.Front())
