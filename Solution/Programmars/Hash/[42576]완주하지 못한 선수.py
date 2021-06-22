from typing import List
import collections

# 2021.06.08 | gomip | created

class Problem:
    def solution(self, participant: List[str], completion: List[str]) -> str:
        # 시간초과
        # freq = collections.Counter(participant)
        # for i in range(len(participant)):
        #     if participant[i] in completion:
        #         freq[participant[i]] -= 1
        # answer = freq.most_common(1)[0][0]
        # freqs = collections.defaultdict()

        # 일단 됨
        temp = sorted(participant)
        temp2 = sorted(completion)

        temp2.append("")
        print(temp, temp2)
        for i in range(len(temp)):
            if temp[i] != temp2[i]:
                return temp[i]

    def other(self,  participant: List[str], completion: List[str]) -> str:
        answer = collections.Counter(participant) - collections.Counter(completion)
        return list(answer.keys())[0]
    

if __name__ == '__main__':
    participant = ["mislav", "stanko", "mislav", "ana"]
    completion = ["stanko", "ana", "mislav"]

    temp = Problem()
    ans = temp.solution(participant, completion)
    print("ans", ans)

    ans2 = temp.other(participant, completion)
    print("ans2", ans2)