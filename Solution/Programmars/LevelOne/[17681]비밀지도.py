from typing import List
import collections

# 21. 7. 1. | gomip | created

class SecretMap:
    def solution(self, n: int, arr1: List[int], arr2: List[int]) -> List[str]:
        answer = []
        for i in range(n):
            # print(" ========================= ")
            # print("bin_arr1", bin(arr1[i])[2:])
            # print("bin_arr2", bin(arr2[i])[2:])
            # print(" ========================= ")
            answer.append(
                bin(arr1[i] | arr2[i])[2:]
                .zfill(n)
                .replace('1', '#')
                .replace('0', ' ')
            )
        print("ans", answer)
        return answer


if __name__ == "__main__":
    n = 5
    arr1 = [9, 20, 28, 18, 11]
    arr2 = [30, 1, 21, 17, 28]

    ans = SecretMap().solution(n, arr1, arr2)
    print("ans", ans)