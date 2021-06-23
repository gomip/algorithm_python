from typing import List
import collections

# 2021.05.30 | gomip | created


class SortColors:
    def solution(self, input: List[int]) -> List[int]:
            red, white, blue = 0, 0, len(input)
            print("red", red)
            print("white", white)
            print("blue", blue)
            while white < blue:
                if input[white] < 1:
                    input[red], input[white] = input[white], input[red]
                    white += 1
                    red += 1
                elif input[white] > 1:
                    blue -= 1
                    input[white], input[blue] = input[blue], input[white]
                else:
                    white += 1
            return input


if __name__ == '__main__':
    input = [2, 0, 2, 1, 1, 0]
    temp = SortColors()
    ans = temp.solution(input)
    print(ans)