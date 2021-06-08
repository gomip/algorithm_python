from typing import List
import collections

# 2021.06.08 | gomip | created

class Fibonacci:
    # 두변수 이용
    def solution(self, n: int) -> int:
        x, y = 0, 1
        for i in range(0, n):
            x, y = y, x+y
        return x

    # 메모제이션
    dp = collections.defaultdict(int)
    def solution_memorization(self, n: int) -> int:
        if n <= 1:
            return n
        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.solution(n - 1) + self.solution(n - 2)
        return self.dp[n]

    # 타뷸레이션
    dp2 = collections.defaultdict(int)
    def solution_tab(self, n: int) -> int:
        self.dp2[0] = 1
        self.dp2[1] = 1

        for i in range(2, n + 1):
            self.dp2[i] = self.dp2[i-1] + self.dp2[i-2]
        return self.dp[n]



if __name__ == '__main__':
    n = 5

    temp = Fibonacci()
    ans = temp.solution(n)
    print("ans", ans)

    ans2 = temp.solution_memorization(n)
    print("ans2", ans2)

    ans3 = temp.solution_tab(n)
    print("ans3", ans3)