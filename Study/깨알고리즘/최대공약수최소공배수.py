from typing import List
import collections

# 2021.07.04 | gomip | created
# gcd : 유클리드 호제법
# => a 를 b로 나눈 나머지 r이 있을때, b 를 r로 나눈 r'가 존재
# => r / r`를 반복적으로 했을때 나머지가 0이 되면 그 값이 a,b의 최대공약수
# lcm : a * b / gcd(a,b)

class GcdLcm:
    def gcd(self, a: int, b:int) -> int:
        while b > 0:
            a, b = b, a%b
        return b

    def lcm(self, a:int, b:int, g: int) -> float:
        return a * b / g
    

if __name__ == '__main__':
    a = 3
    b = 12
    g = GcdLcm().gcd(a, b)
    l = GcdLcm().lcm(a, b, g)

    print("gcd", g, "lcm", l)