from typing import List


def two_sum(strl: List[int], target: int) -> List[int]:
    # for i, n in enumerate(strl):
    #     complement = target-n
    #
    #     if complement in strl[i + 1:]:
    #         return [strl.index(n), strl[i+1:].index(complement) + (i+1)]\
    nums_map = {}
    for i,num in enumerate(strl):
        if target - num in nums_map:
            return [nums_map[target-num], i]
        nums_map[num] = i


if __name__ == '__main__' :
    list = [2,3,7,11,15]
    target = 9
    res = two_sum(list, 9)
    print(res)