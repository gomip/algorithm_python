from typing import List
import collections

# 21. 6. 30. | gomip | created

class FailureRate:
    def solution(self, n: int, stages: List[int]) -> List[int]:
        answer = []
        temp_list = list(filter(lambda x: x < n, stages))
        temp_counter = sorted(list(collections.Counter(temp_list).items()))
        print("temp+", temp_counter)

        for i in range(n):
            print("temp_counter", temp_counter[i])
            # answer.append(temp_counter[i] / len(stages))
        # key = list(temp_counter.keys())
        # value = list(temp_counter.values())
        # print("key", key, "value", value)
        # print("answer", answer)
        return answer


if __name__ == "__main__":
    n = 5
    stages = [2, 1, 6, 2, 4, 3, 3]
    ans = FailureRate().solution(n, stages)
    print("ans", ans)