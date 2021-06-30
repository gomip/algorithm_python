from typing import List
import collections
from datetime import date

# 2021.07.01 | gomip | created

class Sixteen:
    def solution(self, a:int, b: int) -> str:
        answer = ''
        day = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

        return day[date(2016, a, b).weekday()]

if __name__ == '__main__':
    a = 5
    b = 24

    ans = Sixteen().solution(a, b)
    print("ans", ans)