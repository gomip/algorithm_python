from typing import List
import collections

# 2021.06.22 | gomip | created

class Keypad:
    def solution(self, numbers: List[int], hand: str) -> str:
        keypad = {
            1: [0, 0], 2: [0, 1], 3: [0, 2],
            4: [1, 0], 5: [1, 1], 6: [1, 2],
            7: [2, 0], 8: [2, 1], 9: [2, 2],
            0: [2,2]
        }
        answer = ''
        cur_left = 10
        cur_right = 12

        for item in numbers:
            if item in [1, 4, 7]:
                answer += 'L'
                cur_left = item
            elif item in [3, 6, 9]:
                answer += 'R'
                cur_right = item
            # 2, 5, 8, 0
            else:
                item = 11 if item == 0 else item
                left = abs(item - cur_left)
                right = abs(item - cur_right)
                if left // 3 +


        print("cur_left", cur_left)
        print("cur_right", cur_right)
        print("answer", answer)

        return answer


if __name__ == '__main__':
    # numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    numbers = [1, 3, 6, 9, 4, 3, 7]
    hand = "right"

    temp = Keypad()
    ans = temp.solution(numbers, hand)
    print("ans", ans)