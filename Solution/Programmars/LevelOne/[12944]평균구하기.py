from typing import List
import collections

# 21. 7. 3. | gomip | created

class CalculateAverage:
    def solution(self, arr: List[int]) -> float:
        answer = 0
        for item in arr:
            answer += item
        return answer / len(arr)

if __name__ == "__main__":
    input = [1,2,3,4]
    ans = CalculateAverage().solution(input)
    print("ans", ans)