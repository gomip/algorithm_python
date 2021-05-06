import heapq
from typing import List
import collections

# 2021.05.06 | gomip | created


class MostFrequent:
    def solUsingHeapQ(self, value: List[int], k: int) -> List[int]:
        freqs = collections.Counter(value)
        freqs_heap = []
        print(freqs)
        for f in freqs:
            # heap은 키순서대로 정렬해줌으로 key, value를 빈도수, f값으로 바꿔준다.
            # heapq는 최소힙만 지원된다. 그래서 빈도수를 음수 처리해준다.
            heapq.heappush(freqs_heap, (-freqs[f], f))

        topk = list()
        for _ in range(k):
            # k번 만큼 추출, 최소 힙이므로 가장 작은 음수 순으로 추출
            topk.append(heapq.heappop(freqs_heap)[1])
        return topk

    def solLikePython(self, value: List[int], k: int):
        print(value)
        print(list(zip(collections.Counter(value).most_common(k))))
        return list(zip(*collections.Counter(value).most_common(k)))[0]


if __name__ == '__main__':
    value = [1, 1, 1, 2, 2, 3]
    k = 2
    temp = MostFrequent()
    ans = temp.solUsingHeapQ(value, k)
    print('ans 1', ans)

    ans2 = temp.solLikePython(value, k)
    print('ans 2', ans2)