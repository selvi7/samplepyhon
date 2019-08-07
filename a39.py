class Graph(): 
  
    def __init__(self, v): 
        self.v = v 
        self.graph = [[0 for column in range(v)] 
                                for row in range(v)] 
  
    def isBipartite(self, src): 
        colorArr = [-1] * self.v 
       colorArr[src] = 1
  
        queue = [] 
        queue.append(src) 
  
        while queue: 
  
            u = queue.pop() 
  
            # Return false if there is a self-loop 
            if self.graph[u][u] == 1: 
                return False; 
  
            for v in range(self.v): 
  
                if self.graph[u][v] == 1 and colorArr[v] == -1: 
  
                    colorArr[v] = 1 - colorArr[u] 
                    queue.append(v) 
  
                elif self.graph[u][v] == 1 and colorArr[v] == colorArr[u]: 
                    return False
  
        return True
  
g = Graph(4) 
g.graph = [[0, 1, 0, 1], 
            [1, 0, 1, 0], 
            [0, 1, 0, 1], 
            [1, 0, 1, 0] 
            ] 
              
print "Yes" if g.isBipartite(0) else "No"
