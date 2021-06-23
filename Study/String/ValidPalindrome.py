# 주어진 문자열이 펠린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.
# input example
# a man, a plan, a canal: Panama => true
# race a car => false

import timeit
import collections
from typing import Deque
import re

# solution 1
def solution_one(s: str):
    strs = []
    for char in s:
        # isalnum => 영문자 숫자 판별하고 해당하는 문자만 추가.
        if char.isalnum():
            strs.append(char.lower())
    # strs = ['a', 'm', 'a', 'n' .... ]

    # palindrome 여부 확인
    while len(strs) > 1:
        # 첫번째 요소와 마지막 요소를 pop하면서 비교를 하는데 다르면 false 같으면 true로 루프를 돌린다.
        if strs.pop(0) != strs.pop():
            return False
    return True

# solution 2
def solution_two(s: str):
    # 데크로 선언
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char)

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True


# solution 3
def solution_three(s: str):
    s = s.lower()
    # 정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]', '', s)
    return s == s[::-1] # 슬라이싱 -> 리스트 뒤집기


if __name__ == "__main__":
    s_one = "a man, a plan, a canal: Panama"
    s_two = "race a car"
    
    sol_one_start = timeit.default_timer()
    print('s_one', solution_one(s_one))
    sol_one_end = timeit.default_timer()
    print(sol_one_end - sol_one_start)

    sol_two_start = timeit.default_timer()
    print('s_one', solution_two(s_one))
    sol_two_end = timeit.default_timer()
    print(sol_two_end - sol_two_start)

    sol_three_start = timeit.default_timer()
    print(solution_three(s_one))
    sol_three_end = timeit.default_timer()
    print(sol_three_end-sol_three_start)
