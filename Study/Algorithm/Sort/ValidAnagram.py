from typing import List
import collections

# 2021.05.30 | gomip | created

class ValidAnagram:
    def solution(self, s: str, t: str) -> bool:
        a = sorted(s)
        return sorted(s) == sorted(t)

if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    temp = ValidAnagram()
    ans = temp.solution(s,t)
    print(ans)