from typing import List
import collections


# 2021.03.10 | gomip | created
# 문제 : 배열을 입력받아 output [i[가 자신을 제외한 나머지 모든 요소의 곱셈 결과를 가지도록 출력

def product_of_array_except_self(nums: List[int]) -> List[int]:
    output = []
    # 왼쪽 계산
    p = 1
    for i in range(0, len(nums)):
        output.append(p)
        p = p * nums[i]

    # 오른쪽  계산
    p = 1
    for i in range(len(nums) - 1,-1, -1):
        print(i)
        output[i] = output[i] * p
        p = p * nums[i]
    return output


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    res = product_of_array_except_self(nums)
    print('res', res)
