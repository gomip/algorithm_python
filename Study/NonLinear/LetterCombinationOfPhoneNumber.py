# 2021.05.07 | gomip | created

from typing import List


class LetterCombination:
    def solution(self, digits: str) -> List[str]:
        def dfs(index, path):
            print(path,len(path))
            # 끝까지 탐색하며 백트래킹
            if len(path) == len(digits):
                print('im here 1')
                result.append(path)
                return
            # 입력값 자릿수 반복
            print('im here 2')
            for i in range(index, len(digits)):
                for j in dic[digits[i]]:
                    dfs(i+1, path+j)

        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []
        dfs(0, "")
        return result


if __name__ == '__main__':
    digits = "23"
    temp = LetterCombination()
    ans = temp.solution(digits)
    print(len(ans))