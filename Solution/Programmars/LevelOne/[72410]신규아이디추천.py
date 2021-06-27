from typing import List
import collections
import re

# 2021.06.26 | gomip | created
# 1. 대문자 -> 소문자
# 2. 알파벳 (소문자) , 숫자, -, _, . 제외 전부 제거
# 3. .가 두번 이상연속된 부분은 하나의 .으로
# 4. .가 끝과 처음이면 제거
# 5. 빈 문자열이면 a를 입력
# 6. 16자 이상이면 15번재 뒤는 전부 제거. 제거 후 마지막이 .이라면 마지막 .도 제거
# 7. 길이가 2자 이하면, 마지막 단어를 3이 될때까지 반복

class NewId:
    def solution(self, new_id: str) -> str:
        answer = ''

        # 1번 조건
        ans = new_id.lower()

        # 2번 조건
        ans = re.sub('[^a-z0-9-_.]', '', ans)

        # 3번 조건
        ans = re.sub('[.]{2,}', '.', ans)

        # 4번 조건
        if ans.startswith('.'):
            ans = ans[1:]
        if ans.endswith('.'):
            ans = ans[:-1]

        # 5번 조건
        if len(ans) == 0:
            ans = 'a'
        # 7번 조건
        if len(ans) <= 2:
            while len(ans) < 3:
                ans += ans[-1]
        # 6번 조건
        if len(ans) > 15:
            ans = ans[:15]
            if ans.endswith('.'):
                ans = ans[:-1]

        answer = ans
        return answer


if __name__ == '__main__':
    new_id = 'z-+.^.'
    # new_id = '...!@BaT#*..y.abcdefghijklm'
    temp = NewId()
    ans = temp.solution(new_id)
    print(ans)