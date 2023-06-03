from heapq import heappop,heappush

INF = 987654321

class FindShortestPath:
    def __init__(self, nodeNum = 7):
        self.__nodeNum = nodeNum
        self.__adjList = [[] for _ in range(self.__nodeNum+1)]
        self.__shortPaths = [INF for _ in range(self.__nodeNum+1)]
        self.__queue = []

    def load_data(self, filename):
        try:
            with open(f"{filename}", "r") as f:
                lines = f.readlines()
                for line in lines:
                    start, end, weight = map(int, line.strip().split(','))
                    self.__adjList[start].append([end, weight])
        except:
            print("File load fail...")

    def initialize(self):
        self.__adjList = [[] for _ in range(self.__nodeNum+1)]
        self.__queue = []
        self.__shortPaths = [INF for _ in range(self.__nodeNum+1)]    
    
    def find_path(self, start):
        self.__shortPaths[start] = 0
        heappush(self.__queue, (0, start))

        while self.__queue:
            pathWeight, nowNode = heappop(self.__queue)
            for nextNode, cost in self.__adjList[nowNode]:
                if (pathWeight + cost) < self.__shortPaths[nextNode]: #등호에 따라 결과값 바뀔 수 있음
                    self.__shortPaths[nextNode] = self.__shortPaths[nowNode] + weight
                    heappush(self.__adjList, )

    
    def print_path(self, r):
        print("print_path ...")