# 매일의 화씨 온도 리스트 T를 입력받아서 더 따뜻한 날씨를 위해서는 며칠을 더 기다려야 하는지를 출력
# input = T = [73,74,75,71,69,72,76,73]
# output = [1,1,4,2,1,1,0,0]

from typing import List

class stackThree:
    def daily_temp(self, T: List[int]) -> List[int]:
        answer = [0] * len(T)
        stack = []
        for i, cur in enumerate(T):
            while stack and cur > T[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)
        return answer


if __name__ == '__main__':
    input = [73,74,75,71,69,72,76,73]
    a = stackThree()
    res = a.daily_temp(input)
    print(res)