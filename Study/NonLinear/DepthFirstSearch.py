# 2021.05.07 | gomip | created

from typing import List


class DepthFirstSearch:
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

    def dfsUsingRecursive(self, v: int, discovered=[]) -> List[int]:
        discovered.append(v)
        for w in self.graph[v]:
            if w not in discovered:
                discovered = self.dfsUsingRecursive(w, discovered)
        return discovered

    def dfsUsingStack(self, v: int) -> List[int]:
        discovered = []
        stack = [v]
        while stack:
            v = stack.pop()
            if v not in discovered:
                discovered.append(v)
                for w in self.graph[v]:
                    stack.append(w)
        return discovered


if __name__ == '__main__':
    dfs = DepthFirstSearch()
    recursive = dfs.dfsUsingRecursive(1)
    print('recurive : ', recursive)
    stack = dfs.dfsUsingStack(1)
    print('   stack : ', stack)