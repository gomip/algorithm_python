from typing import List
import collections

# 21.07.04 | gomip | created

class Country:
    def solution(self, n: int) -> str:
        answer = ''
        div = int(n / 3)
        rem = n % 3

        if div > 3:
            answer += self.solution(div)
        else:
            if n != 3 and div != 0:
                answer += str(div)

        # else:
            # if div == 3:
            #     answer += '4'
            # elif div != 0:
            #     print("div:", div)
            #     answer += str(rem)

        if rem == 0:
            answer += '4'
        elif rem == 1:
            answer += '1'
        else:
            answer += '2'

        return answer

    def solution_by_other(self, n: int) -> str:
        answer = ""
        while num:
            num, nam = divmod(num, 3)
        answer = "412"[nam] + answer
        if not nam:
            num -= 1
        return answer


if __name__ == '__main__':
    n = 5
    ans = Country().solution(n)
    print("ans", ans)