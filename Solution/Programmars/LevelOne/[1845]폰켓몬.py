from typing import List
import collections
import random
# 2021.06.23 | gomip | created

class Phonekemon:
    def solution(self, nums: List[int]) -> int:
        answer = 0
        unique = set(nums)
        u_list = list(unique)

        for item in u_list:
            if (answer < len(nums) // 2):
                answer += 1

        return answer


if __name__ == '__main__':
    input = [3,3,3,2,2,2]
    temp = Phonekemon()
    ans = temp.solution(input)
    print(ans)