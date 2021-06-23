from typing import List
import collections


#  | gomip | created

class ListNode:
    def __init__(self, val=0, next=None):
        self.head = val
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