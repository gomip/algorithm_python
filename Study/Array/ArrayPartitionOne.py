from typing import List
import collections


# 2021.03.10 | gomip | created

def ArrayPartitionOne(input: List[int]) -> int:
    # 기본
    # - 정렬하고 앞에서부터 페어를 만들어주는데 이러면 뒤에 녀석이 선택됨으로 짝수번째 녀석만 더한다.
    #
    #     sum = 0
    #     input.sort()
    #
    #     for i, n in enumerate(input):
    #         if i % 2 == 0:
    #             sum += n
    #     return sum

    # 파이썬다운 방식
    return sum(sorted(input)[::2])


if __name__ == '__main__':
    input = [1, 4, 3, 2]
    res = ArrayPartitionOne(input)
    print('res', res)
