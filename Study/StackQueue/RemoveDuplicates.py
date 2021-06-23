# 중복된 문자를 제외하고 사전식 순서로 나열하라
# input = bcabc | cbacdcbc
# output = abc  | acdb

from typing import List
import collections

#  | gomip | created


class Dup:
    def remove_duplicates(self, input: str) -> str:
        # 집합으로 정렬
        print('1', set(input))
        for char in sorted(set(input)):
            # char 값 뒤를 suffix로 지정
            suffix = input[input.index(char):]
            # 전체를 가리키는 set과 suffix의 값이 같으면 재귀로 뒤에 중복값을 확인한다.
            if set(input) == set(suffix) :
                return char + self.remove_duplicates(suffix.replace(char, ''))
        return ''

    def remove_dup_by_stack(self, input: str) -> str:
        # 모든 알파벳에 대하여 counter를 수행
        counter, seen, stack = collections.Counter(input), set(), []

        for char in input:
            # for문을 통해서 char counter를 한개씩 빼준다. -> 다음에 중복이 제거가 가능한지 확인할수있음
            counter[char] -= 1
            if char in seen:
                print('char', char)
                continue
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                print('seen 1', seen, stack, char)
                seen.remove(stack.pop())
                print('seen 2', seen, stack, char)
            stack.append(char)
            seen.add(char)
            print('after loop', stack, seen)
        return ''.join(stack)


if __name__ == '__main__':
    input = "acbc"
    test = Dup()
    res = test.remove_duplicates(input)
    print(res)

    input2 = "cbacdcbc"
    res2 = test.remove_dup_by_stack(input2)
    print(res2)