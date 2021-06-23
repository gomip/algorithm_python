from typing import List
import collections

# 2021.06.22 | gomip | created

class Keypad:
    def solution(self, numbers: List[int], hand: str) -> str:
        keypad = {
            1: [0, 0], 2: [0, 1], 3: [0, 2],
            4: [1, 0], 5: [1, 1], 6: [1, 2],
            7: [2, 0], 8: [2, 1], 9: [2, 2],
            10: [3, 0], 0: [3, 1], 12: [3, 2]
        }
        answer = ''
        cur_left = [3, 0]
        cur_right = [3, 2]

        for item in numbers:
            if item in [1, 4, 7]:
                answer += 'L'
                cur_left = keypad[item]
            elif item in [3, 6, 9]:
                answer += 'R'
                cur_right = keypad[item]
            else:
                print("==============")
                item_pos = keypad[item]

                # 두지점간의 거리
                dist_left = abs(item_pos[0]-cur_left[0]) + abs(item_pos[1] - cur_left[1])
                dist_right = abs(item_pos[0]-cur_right[0]) + abs(item_pos[1] - cur_right[1])

                if dist_right > dist_left:
                    answer += 'L'
                    cur_left = item_pos
                elif dist_left > dist_right:
                    answer += 'R'
                    cur_right = item_pos
                else:
                    # 왼손 잡이의 경우
                    if hand == "left":
                        answer += 'L'
                        cur_left = item_pos
                    # 오른손 잡이의 경우
                    else:
                        answer += 'R'
                        cur_right = item_pos
        return answer

# [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"
# 기댓값 〉	"LRLLLRLLRRL"
# 실행 결과 〉	실행한 결괏값 "LRLLRRLLRRL"이(가) 기댓값 "LRLLLRLLRRL"와(과) 다릅니다.

if __name__ == '__main__':
    numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    # numbers = [1, 3, 4, 5, 8]
    # numbers = [1, 3, 6, 9, 4, 3, 7]
    # numbers = [1, 2]
    hand = "right"

    temp = Keypad()
    ans = temp.solution(numbers, hand)
    print("ans", ans)