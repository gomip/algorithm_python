from typing import List
import collections
import sys


# 2021.03.10 | gomip | created


def buy_sell(prices: List[int]) -> int:
    profit = 0
    min_price = sys.maxsize

    for p in prices:
        min_price = min(min_price, p)
        profit = max(profit, p - min_price)
    return profit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    res = buy_sell(prices)
    print('res', res)
