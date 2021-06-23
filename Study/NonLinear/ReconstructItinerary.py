from typing import List
import collections

# 2021.05.11 | gomip | created
# [from, to] 로 이루어진 목록에서 JFK 에서 출발하는 여행 일정 구상

class ReconstructItinerary:
    def solutionUsingQueue(self, ticket: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for a, b in sorted(ticket):
            graph[a].append(b)

        print("graph 1 : ", graph)

        graph2 = collections.defaultdict(list)
        for a, b in ticket:
            graph2[a].append(b)
        print("graph 2 : ", graph2)
        route = []

        # def dfs(start: str):
        #     while graph[start]:
        #         dfs(graph[start].pop(0))
        #     route.append(start)
        #
        # dfs("JFK")
        return route[::-1]

    def solutionUsingStack(self, ticket: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for a, b in sorted(ticket, reverse=True):
            graph[a].append(b)

        print("answer 2 graph : ", graph)

        route = []

        def dfs(start: str):
            while graph[start]:
                dfs(graph[start].pop())
            route.append(start)

        dfs("JFK")
        return route[::-1]


if __name__ == '__main__':
    ticket = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    temp = ReconstructItinerary()
    ans1 = temp.solutionUsingQueue(ticket)
    print("answer 1 : ", ans1)
    ans2 = temp.solutionUsingStack(ticket)
    print("answer 2 : ", ans2)