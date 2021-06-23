from typing import List
import collections

# 2021.03.18 | gomip | created

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_list(self, li: List[int]):
        for i in range(len(li)):
            tmp = ListNode(li[i])

            if self.head is None:
                self.head = tmp
            else:
                cur = self.head
                while cur.next is not None:
                    cur = cur.next
                cur.next = tmp
            print("i :", li[i])
        self.reverse_list(self.head)

    def reverse_list(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            print("next", head.val)
            next, node.next = node.next, prev
            prev, node = node, next
        return prev


if __name__ == '__main__':
    res = [1,2,3,4,5]
    node = LinkedList()
    node.add_list(res)