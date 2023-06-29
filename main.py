
from typing import List

def maxProbability(n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
    
    vertexToEdges = dict()

    counter = 0

    for eachEdgeIndex in edges:
        startingVertex = eachEdgeIndex[0]
        endingVertex = eachEdgeIndex[1]

        if startingVertex not in vertexToEdges:
            vertexToEdges[startingVertex] = [counter]
            
        else:
            vertexToEdges[startingVertex].append(counter)
            
        
        if endingVertex not in vertexToEdges:
            vertexToEdges[endingVertex] = [counter]
        else:
            vertexToEdges[endingVertex].append(counter)

        counter += 1




    def search(vertexToEdgesDict, start, end):
        
        stack = []
        visited = set()
        visited.add(start)
        probabilityDictionary = dict()
        probabilityDictionary[start] = 1
        # add initial edges to stack

        for eachEdgeIndex in vertexToEdgesDict[start]:
            stack.append(eachEdgeIndex)
        

        
        # dfs

        prevNode = start
        currNode = None

        while len(stack) != 0:
            # visit each node in the stack 
                # 1) Visit
                #   a) If not in the vistied set, add it 
                #   b) else, stop traversing this path and clear visited set

            edgeIndex = stack[-1]

            temp = currNode
            if currNode == None:
                prevNode = start
            else:
                prevNode = currNode
            
            if prevNode == edges[edgeIndex][0]:
                currNode = edges[edgeIndex][1]
            else:
                currNode = edges[edgeIndex][0]

            stack.pop()
            if currNode in visited:
                currNode = temp
                continue

            probabilityOfCurrNodeOnCurrPath = probabilityDictionary[prevNode] * succProb[edgeIndex]



                # 2) compare the probability it took to get there with the stored probability
                #   a) If <= , then stop traversing this path and clear the visited set
                #   b) else, update the probability
            
            if currNode not in probabilityDictionary or probabilityOfCurrNodeOnCurrPath > probabilityDictionary[currNode]:
                probabilityDictionary[currNode] = probabilityOfCurrNodeOnCurrPath
            else:
                currNode = temp
                continue
                
                # 3) If it's the end node, do step 2 but stop traversing and clear visited set
            if currNode == end:
                currNode = temp
                visited = {start}
                continue
                # 4) Add all the neighbors of the current node to the stack

            visited.add(currNode)

            for eachEdgeIndex in vertexToEdgesDict[currNode]:
                stack.append(eachEdgeIndex)
        
        return probabilityDictionary[end]

    return search(vertexToEdges, start, end)

        
    

print(maxProbability(n = 5, edges = [[1,4],[2,4],[0,4],[0,3],[0,2],[2,3]], succProb = [0.37,0.17,0.93,0.23,0.39,0.04], start = 3, end = 4))
        

