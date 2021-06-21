from typing import List
import collections

# 21. 6. 9. | gomip | created


class Problem:
    def solution(self, phone_book: List[str]) -> bool:
        for i in range(len(phone_book)):
            for j in range(i+1, len(phone_book)):
                if len(phone_book[i]) < len(phone_book[j]) and phone_book[j].startswith(phone_book[i]):
                    return False
        return True

    def solution_2(self, phone_book: List[str]) -> bool:
        phone_book.sort()
        # for i in range(len(phone_book)-1):
        #     if phone_book[i] in phone_book[i+1]:
        #         return False

        for p1, p2 in zip(phone_book, phone_book[1:]):
            if p2.startswith(p1):
                return False
        return True

    def solution_hahs(self, phone_book: List[str]) -> bool:
        answer = True
        temp_map = {}
        for num in phone_book:
            temp_map[num] = 1
        print("num", temp_map)
        for pn in phone_book:
            temp = ""
            for n in pn:
                temp += n
                print("n",temp)
                if temp in temp_map and temp != pn:
                    answer = False
        return answer


if __name__ == "__main__":
    input = ["119", "97674223", "1195524421"]
    input2 = ["123","456","789"]
    input3 = ["12","123","1235","567","88"]

    ans = Problem().solution(input)
    print("ans", ans)
    ans2 = Problem().solution_2(input2)
    print("ans2", ans2)
    ans3 = Problem().solution_hahs(input2)
    print("ans3", ans3)
