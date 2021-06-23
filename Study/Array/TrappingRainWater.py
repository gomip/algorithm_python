from typing import List
import collections

# 2021.03.08 | gomip | created

def TrappingRainWater(input: List[int]) -> List[int]:
    if not input:
        return 0

    vol = 0
    l, r = 0, len(input) - 1
    lmax, rmax = input[l], input[r]

    while l < r:
        lmax, rmax = max(input[l],lmax), max(input[r], rmax)

        if lmax <= rmax:
            vol += lmax - input[l]
            l +=1
        else :
            vol += rmax - input[r]
            r -=1
    return vol


if __name__ == '__main__':
    input = [0,1,0,2,1,0,1,3,2,1,2,1]
    res = TrappingRainWater(input)
    print('res' , res)