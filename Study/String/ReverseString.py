# 문자열 뒤집기

from typing import List


def reverse_string(s: List[str]) -> List[str]:
    s.reverse()
    return s


if __name__ == '__main__' :
    s = ['h', 'e', 'l', 'l', 'o']
    res = reverse_string(s)
    print(res)