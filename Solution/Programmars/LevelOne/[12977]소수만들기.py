from typing import List
import collections
import itertools
import math

# 2021.06.27 | gomip | created

class MakePrime:
    def solution(self, nums: List[int]) -> int:
        # 모든 조합 생성
        result = list(itertools.combinations(nums, 3))

        # 합 구하기
        answer = 0
        sum_value = []
        for item in result:
            sum_value.append(sum(item))
            # temp = 0
            #
            # for i in range(len(item)):
            #     temp += item[i]
            #
            # sum_value.append(temp)

        # 소수 확인

        for item in sum_value:
            temp = self.isPrime(item)
            if temp:
                answer += 1

        return answer

    def isPrime(self, item: int) -> bool:
        for i in range(2, int(math.sqrt(item)) + 1):
            if item % i == 0:
                return False
        return True



if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    temp = MakePrime()
    ans = temp.solution(nums)
    print(ans)