from typing import List
import collections

# 2021.05.06 | gomip | created
# 해시 기능 구현
# 1. put(key,value) : 키 값을 해시맵에 삽입한다. 만약 이미 존재하는 키라면 업데이트
# 2. get(key)       : 키에 해당하는 값을 조회한다. 만약 키가 존재하지 않는다면 -1 리턴
# 3. remove(key)    : 키에 하당하는 키, 값을 해시맵에서 삭제

# 개별 체이닝


class ListNode:
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.next = None


class BaseHaspMap:
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        # 나눗셈 연산을 통해 해시값 지정
        index = key % self.size

        # 해시 테이블 인덱스에 값이 없다면 key , value 값 삽입
        # => self.table[index].value is None으로 비교한 이유는 defaultdict(ListNode)를 사용하기 때문이다.
        # ==> defaultdict는 존재하지 않는 인덱스로 조회하게 되면 에러를 발생하지 않고 새로운 객체를 생성한다.
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return

        # 해당 인덱스에 값이 존재할 경우
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = key % self.size
        # 해당 인덱스에 값이 없으면 오류 리턴
        if self.table[index].value is None:
            return -1

        # 값이 있을 경우, 키에 매칭되는 값을 리턴해준다.
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        # 해당 인덱스에 값이 없으면 아무것도 리턴해주지 않는다.
        if self.table[index].value is None:
            return

        # 값이 있을 경우
        # 1. 첫번째 노드인 경우 삭제 처리
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return
        # 2. 연결리스트 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next


if __name__ == '__main__':
    temp = BaseHaspMap()
    temp.put(1, 1)
    temp.put(2, 2)
    print('get 1 :', temp.get(2))
    temp.put(2, 3)
    temp.put(2, 4)
    print('get 2 :', temp.get(2))
    temp.remove(2)
    print('get 3 :', temp.get(2))