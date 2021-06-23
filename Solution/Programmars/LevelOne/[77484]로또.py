from typing import List
import collections

# 2021.06.23 | gomip | created

class Lotto:
    def check_rank(self, num: int) -> int:
        if num == 6:
            return 1
        elif num == 5:
            return 2
        elif num == 4:
            return 3
        elif num == 3 :
            return 4
        elif num == 2:
            return 5
        else:
            return 6

    def solution(self, lottos: List[int], win_nums: List[int]) -> List[int]:
        answer = []
        max_count = 0
        min_count = 0
        for item in lottos:
            if item != 0 and item in win_nums:
                print("item", item)
                max_count += 1
                min_count += 1
            if item == 0:
                max_count += 1

        max = self.check_rank(max_count)
        answer.append(max)
        min = self.check_rank(min_count)
        answer.append(min)
        return answer

    def solution_two(self, lottos: List[int], win_nums: List[int]) -> List[int]:
        answer = []
        zero = lottos.count(0)
        rank = [6, 6, 5, 4, 3, 2, 1]
        cnt = 0
        for item in lottos:
            if item in win_nums:
                cnt += 1
        answer.append(rank[cnt+zero])
        answer.append(rank[cnt])
        return answer


if __name__ == '__main__':
    input = [44, 1, 0, 0, 31, 25]
    win_nums = [31, 10, 45, 1, 6, 19]

    temp = Lotto()
    ans = temp.solution(input, win_nums)
    print(ans)

    ans2 = temp.solution_two(input, win_nums)
    print(ans2)