from typing import List
import collections

# 21. 6. 29. | gomip | created

class DeleteDuplicates:
    def solution(self, s: str) -> int:
        answer = 0
        stack = []

        for c in s:
            if stack:
                if stack[-1] == c:
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)

        if len(stack) == 0:
            answer = 1
        else:
            answer = 0
        return answer


if __name__ == "__main__":
    input = "baabaa"
    temp = DeleteDuplicates()
    ans = temp.solution(input)
    print(ans)