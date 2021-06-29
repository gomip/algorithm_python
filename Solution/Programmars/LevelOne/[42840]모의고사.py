from typing import List
import collections

# 2021.06.27 | gomip | created
# 1번 : 1 -> 2 -> 3 -> 4 -> 5 반복
# 2번 : 2 -> 1 -> 2 -> 3 -> 2 -> 4 -> 2 -> 5 반복
# 3번 : 33 -> 11 -> 22 -> 44 -> 55 반복

class Test:
    def solution(self, answers: List[int]) -> List[int]:
        answer = collections.defaultdict(int)
        user1 = [1, 2, 3, 4, 5]
        user2 = [2, 1, 2, 3, 2, 4, 2, 5]
        user3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

        for i in range(len(answers)):
            # 1번 수포자
            if answers[i] == user1[i % 5]:
                answer[0] += 1
            # 2번 수포자
            if answers[i] == user2[i % 8]:
                answer[1] += 1
            # 3번 수포자
            if answers[i] == user3[i % 10]:
                answer[2] += 1

        value_list = answer.values()
        # max_value = max(value_list)

        ans = []
        # if answer[0] == max_value:
        #     ans.append(1)
        # if answer[1] == max_value:
        #     ans.append(2)
        # if answer[2] == max_value:
        #     ans.append(3)

        # 다른 사람 풀이
        for idx,s in enumerate(answer):
            if s == max(answer):
                ans.append(idx+1)

        return ans


if __name__ == '__main__':
    input = [1, 2, 3, 4, 5]
    temp = Test()
    ans = temp.solution(input)
    print(ans)