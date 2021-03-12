from typing import List, Deque
import collections


# 2021.03.10 | gomip | created
class ListNode:
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = None


def palindrome_list(head: ListNode) -> bool:
    q: List = []

    if not head:
        return True

    node = head
    while node is not None:
        # print('val', node.val)
        q.append(node.val)
        # print('next', node.next)
        node = node.next

    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False
    return True

    # q: Deque = collections.deque
    #
    # if not head:
    #     return True
    #
    # node = head
    # if node is not None:
    #     q.append(node.val)
    #     node = node.next
    #
    # while len(q) > 1 :
    #     if q.popleft() != q.pop():
    #         return False
    # return True

    # rev = None
    # slow = fast = head
    #
    # while fast and fast.next:
    #     fast = fast.next.next
    #     rev, rev.next, slow = slow, rev, slow.next
    # if fast:
    #     slow = slow.next
    #
    # while rev and rev.val == slow.val:
    #     slow, rev = slow.next, rev.next
    # return not rev


class LinkedList:
    def __init__(self):
        self.head = None

    def add_list(self, value: List[int]):
        for i in range(len(value)):
            tmp = ListNode(value[i])
            if self.head is None:
                self.head = tmp
            else:
                cur = self.head
                while cur.next is not None:
                    cur = cur.next
                cur.next = tmp
        res = palindrome_list(self.head)
        print(res)


if __name__ == '__main__':
    node = LinkedList()
    node.add_list([1, 2, 2])
    # arr = [1, 2, 1]

    # res = palindrome_list(head)
    # print('res', res)
