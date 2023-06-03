from heapq import heappop,heappush

INF = int(1e9)

class FindShortestPath:
    def __init__(self, nodeNum = 7):
        self.__nodeNum = nodeNum
        self.__fileData = None
        self.__adjList = [[] for _ in range(self.__nodeNum+1)]
        self.__parent = [i for i in range(self.__nodeNum+1)]
        self.__dist = [INF for _ in range(self.__nodeNum+1)]

    def load_data(self, filename):
        try:
            with open(filename, "r") as f:
                self.__fileData = f.readlines()
        except:
            print("File load fail...")

    def initialize(self):
        for line in self.__fileData:
            start, end, weight = map(int, line.strip().split(','))
            self.__adjList[start].append([end, weight])
        self.__dist = [INF for _ in range(self.__nodeNum+1)]
        self.__parent = [i for i in range(self.__nodeNum+1)]
    
    def find_path(self, start):
        queue = []
        self.__dist[start] = 0
        heappush(queue, (0, start))

        while queue:
            distance, nowNode = heappop(queue)
            if distance > self.__dist[nowNode]:
                continue
            for nextNode, cost in self.__adjList[nowNode]:
                nextDist = distance + cost
                if nextDist < self.__dist[nextNode]:
                    self.__parent[nextNode] = nowNode
                    self.__dist[nextNode] = nextDist
                    heappush(queue, (nextDist, nextNode))
    
    def print_path(self, r):
        for i in range(self.__nodeNum+1):
            node = i
            path = [node]
            while node != 0:
                node = self.__parent[node]
                path.append(node)
            path.reverse()
            print(f"[ {i} ]: {path[0]}",end="")
            for n in path[1:]:
                print(f"=>{n}",end="")
            print(f" : {self.__dist[i]}")
        