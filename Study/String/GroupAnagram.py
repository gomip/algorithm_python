# 문자열 배열을 받아 애너그램 단위로 그룹평하라

import collections
from typing import List

input = ["eat", "tea", "tan", "ate", "nat", "bat"]
# output = [["ate", "eat", "tea"], ["nat", "tan"], ["bat"]]


def group_anagram(input: List[str]) -> List[List[str]]:
    anagram = collections.defaultdict(list)

    for word in input:
        anagram[''.join(sorted(word))].append(word)

    return list(anagram.values())


if __name__ == "__main__":
    print(group_anagram(input))