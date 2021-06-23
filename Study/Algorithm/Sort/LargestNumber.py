from typing import List
import collections

# 2021.05.30 | gomip | created

class LargestNumber:
    def to_swap(self, n1: int, n2: int) -> bool:
        a = str(n1) + str(n2)
        b = str(n2) + str(n1)
        return str(n1) + str(n2) < str(n2) + str(n1)

    def solution(self, input: List[int]) -> str:
        i = 1
        while i < len(input):
            j = i
            while j > 0 and self.to_swap(input[j-1], input[j]):
                input[j], input[j-1] = input[j-1], input[j]
                j -= 1
            i += 1

        return str(int(''.join(map(str, input))))


if __name__ == '__main__':
    input = [10,2]
    temp = LargestNumber()
    ans = temp.solution(input)
    print(ans)