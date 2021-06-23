from typing import List

# 2021.06.05 | gomip | created

class SumOfTwoIntegers:
    def solution(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF

        a_bin = bin(a & MASK)[2:].zfill(32)
        b_bin = bin(b & MASK)[2:].zfill(32)

        result = []
        carry = 0
        sum = 0

        for i in range(32):
            print("=============== i : ", i," ===============")
            temp_a = int(a_bin[31-i])
            temp_b = int(b_bin[31-i])
            print("a_bin", a_bin, "temp_a", temp_a)
            print("b_bin", b_bin, "temp_b", temp_b)

            q1 = temp_a & temp_b
            q2 = temp_a ^ temp_b
            q3 = q2 & carry
            sum = carry ^ q2
            carry = q1 | q3
            print("sum", sum)

            result.append(str(sum))
        if carry == 1:
            result.append('1')

        # 초과 자릿수 처리
        result = int(''.join(result[::-1]), 2) & MASK
        print("result", result)
        # 음수 처리
        if result > INT_MAX:
            result = ~(result ^ MASK)
        return result

    def solution_simple(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF

        while b != 0:
            a,b = (a^b) & MASK , ((a & b) << 1) & MASK

        # 음수처리
        if a > INT_MAX:
            a = ~(a^ MASK)
        return a


if __name__ == '__main__':
    a = 1
    b = 2

    temp = SumOfTwoIntegers()
    ans = temp.solution(a,b)

    print(ans)