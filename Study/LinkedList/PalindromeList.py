from typing import List, Deque
import collections


# 2021.03.10 | gomip | created
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def palindrome_list(head: ListNode) -> bool:
    # q: List = []
    #
    # if not head:
    #     return True
    #
    # node = head
    # while node is not None:
    #     print('val', node.val)
    #     q.append(node.val)
    #     print('next', node.next)
    #     node = node.next
    #
    # while len(q) > 1:
    #     if q.pop(0) != q.pop():
    #         return False
    # return True

    # q: Deque = collections.deque
    #
    # if not head:
    #     return True
    #
    # node = head
    # if node is not None:
    #     q.append(node.val)
    #     node= node.next
    #
    # while len(q) > 1 :
    #     if q.popleft() != q.pop():
    #         return False
    # return True

    rev = None
    slow = fast = head

    while fast and fast.next :
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast :
        slow = slow.next

    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    return not rev

if __name__ == '__main__':
    head = ListNode()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(2)
    node4 = ListNode(1)
    head2 = ListNode()

    head.val = node1
    head.next = node2


    res = palindrome_list(head)
    print('res', res)
