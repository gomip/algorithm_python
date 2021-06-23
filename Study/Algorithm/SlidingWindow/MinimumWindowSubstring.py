import collections
from typing import List

# 2021.06.05 | gomip | created

class MinimumWindowSubstring:
    # brute force로 t만큼의 길이만큼부터해서 s의 길이만큼 비교하는 형식
    def solution_bruteforce(self, s: str, t: str) -> str:
        def contains(sub_list: List[str], t_list: List[str]):
            for t_elem in t_list:
                if t_elem in sub_list:
                    sub_list.remove(t_elem)
                else:
                    return False
            return True

        # 매개변수 값이 없다면 빈값 return
        if not s or not t:
            return ''

        # 윈도우 최초 길이는 비교하는 문자열 t만큼의 길이로
        window = len(t)

        for size in range(window, len(s) + 1):
            for left in range(len(s) - size + 1):
                sub = s[left: left + size]
                if contains(list(sub), list(t)):
                    return sub
        return ""

    def solution_window(self, s: str, t: str) -> str:
        # 필요한 문자의 각가의 개수
        need = collections.Counter(t)
        # 필요한 문자의 전체개수
        missing = len(t)
        left = start = end = 0

        # 윈도우를 오른쪽으로 확대한다
        # enumerate(s, 1)은 1부터 시작
        for right, char in enumerate(s, 1):
            missing -= need[char] > 0
            need[char] -= 1

            if missing == 0:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                if not end or right - left <= end - start:
                    start, end = left, right
                    need[s[left]] += 1
                    missing += 1
                    left += 1
        return s[start:end]


if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"

    temp = MinimumWindowSubstring()
    ans = temp.solution_bruteforce(s, t)
    print("ans", ans)

    ans2 = temp.solution_window(s, t)
    print("ans2", ans2)