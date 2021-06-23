from typing import List
import collections

# 2021.05.06 | gomip | created
# 중복 문자가 없는 가장 긴 부분 문자열의 길이 구하기
# input : abcabcbb
# output: 3


class LongestSubstringWithoutDuplicates:
    def countingUsingSlicing(self, value: str) -> int:
        used = {}
        max_length = start = 0

        for index, char in enumerate(value):
            print(char, index)
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_length = max(max_length, index - start + 1)
            used[char] = index
        return max_length


if __name__ == '__main__':
    input = "abcabcbb"
    temp = LongestSubstringWithoutDuplicates()
    cnt = temp.countingUsingSlicing(input)
    print('count 1', cnt)
