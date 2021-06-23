from typing import List
import collections

# 2021.05.06 | gomip | created
# 보석의 갯수 counting (J: 보석 S: 돌)
# input : J = "aA" S = "aAAbbbb"
# output : 3


class JewelAndStone:
    # 해시테이블 이용
    def countingUsingHash(self, j: str, s: str) -> int:
        freqs = {}
        count = 0

        # Stone counting
        for char in s:
            if char not in freqs:
                freqs[char] = 1
            else:
                freqs[char] +=1
        print(freqs)

        # Jewel counting
        for char in j:
            if char in freqs:
                count += freqs[char]
        return count

    # defaultdict 이용
    def countingUsingDefaultDict(self, j: str, s: str) -> int:
        freqs = collections.defaultdict(int)
        count = 0

        # Stone counting
        for char in s:
            freqs[char] += 1

        # Jewel counting
        for char in j:
            count += freqs[char]

        return count

    # 카운터 이용
    def countingUsingCounter(self, j: str, s: str) -> int:
        # freqs를 처음부터 s에 있는 char별로 counting 수행해서 저장
        freqs = collections.Counter(s)
        count = 0

        for char in j:
            count += freqs[char]
        return count

    # 파이썬다운 코딩
    def countingLikePython(self, j: str, s: str) -> int:
        # s를 구성하는 ch가 j에 있으면 True 리턴해주고 그걸 count
        return sum(ch in j for ch in s)


if __name__ == '__main__':
    jewel = "aA"
    stone = "aAAbbbb"

    temp = JewelAndStone()
    cnt = temp.countingUsingHash(jewel, stone)
    print('count', cnt)

    cnt2 = temp.countingUsingDefaultDict(jewel, stone)
    print('count 2', cnt2)

    cnt3 = temp.countingUsingCounter(jewel, stone)
    print('count 3', cnt3)

    cnt4 = temp.countingLikePython(jewel, stone)
    print('count 4', cnt4)