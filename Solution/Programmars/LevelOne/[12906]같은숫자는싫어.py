from typing import List
import collections

# 21. 7. 3. | gomip | created

class RemoveDuplicateNumber:
    def solution(self, n: List[int]) -> List[int]:
        answer = []
        for item in n:
            if answer:
                if item != answer[-1]:
                    answer.append(item)
            else:
                answer.append(item)
        return answer


if __name__ == "__main__":
    input = [1,1,3,3,0,1,1]
    ans = RemoveDuplicateNumber().solution(input)
    print("ans", ans)