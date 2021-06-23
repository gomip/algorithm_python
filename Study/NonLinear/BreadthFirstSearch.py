# 2021.05.07 | gomip | created

from typing import List


class BreadhFirstSearch:
    def __init__(self):
        self.graph = {
            1: [2, 3, 4],
            2: [5],
            3: [5],
            4: [],
            5: [6, 7],
            6: [],
            7: []
        }

    def bfsUsingQueue(self, v: int) -> List[int]:
        discovered = [v]
        queue = [v]
        while queue:
            v = queue.pop(0)
            for w in self.graph[v]:
                if w not in discovered:
                    discovered.append(w)
                    queue.append(w)
        return discovered


if __name__ == '__main__':
    bfs = BreadhFirstSearch()
    q = bfs.bfsUsingQueue(1)
    print('queue : ', q)