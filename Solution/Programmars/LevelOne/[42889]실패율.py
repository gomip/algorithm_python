from typing import List
import collections

# 21. 6. 30. | gomip | created

class FailureRate:
    def solution(self, n: int, stages: List[int]) -> List[int]:
        answer = []
        # temp_counter = sorted(list(collections.Counter(stages).items()))
        l = len(stages)
        # print(temp_counter)
        temp = {}

        # print("l", l)
        # for key,value in temp_counter:
        #     print("key", key, "value", value, "l", l)
        #     temp.append(value / (8-value))
        #     l -= value
        # print(temp)

        for i in range(1, n+1):
            if l != 0:
                cnt = stages.count(i)
                temp[i] = cnt / l
                l -= cnt
            else:
                temp[i] = 0
        print("temp", temp)
        answer = sorted(temp, key = lambda x: temp[x])
        # temp_list = list(filter(lambda x: x < n, stages))
        # temp_counter = sorted(list(collections.Counter(temp_list).items()))
        # print("temp+", temp_counter)

            # answer.append(temp_counter[i] / len(stages))
        # key = list(temp_counter.keys())
        # value = list(temp_counter.values())
        # print("key", key, "value", value)
        # print("answer", answer)
        return answer


if __name__ == "__main__":
    n = 5
    stages = [2, 1, 2, 6, 2, 4, 3, 3]
    ans = FailureRate().solution(n, stages)
    print("ans", ans)