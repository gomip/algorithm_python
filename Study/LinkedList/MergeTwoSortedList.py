# 정렬되어있는 두 연결리스트 합치기

# input : 1->2->4 | 1->3->4
# output : 1->1->2->3->4->4

from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_list(self, value: List[int], value2: List[int]):
        tmp: ListNode() = None
        for i in range(len(value)):
            tmp = ListNode(value[i])
            if self.head is None:
                self.head = tmp
            else:
                cur = self.head
                while cur.next is not None:
                    cur = cur.next
                cur.next = tmp

        tmp2: ListNode() = None
        for i in range(len(value2)):
            tmp2 = ListNode(value2[i])
            if self.head is None:
                self.head = tmp2
            else:
                cur = self.head
                while cur.next is not None:
                    cur = cur.next
                cur.next = tmp2

        res = merge_list(tmp, tmp2)
        print(res)


def merge_list(l1: ListNode, l2: ListNode) -> ListNode:
    if (not l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1
    if l1:
        l1.next = merge_list(l1.next, l2)
    return l1


if __name__ == '__main__':
    input_one = [1, 2, 4]
    input_two = [1, 3, 4]

    node = LinkedList()
    node.add_list(input_one, input_two)

