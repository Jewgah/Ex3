class Edge_data:
    #my edge data
    def __init__(self,src:int,dest:int,weight:float):
        self.__src=src
        self.__dest=dest
        self.__weight = weight
        self.tag=0
        self.info=""

    def getsrc(self) -> int:
        return self.__src

    def getdest(self) -> int:
        return self.__dest

    def getweight(self) ->float:
        return self.__weight

    def __str__(self):
        return "Edge_data(src: %s , dest: %s , weight %s)" % (
            self.__src, self.__dest,self.__weight)