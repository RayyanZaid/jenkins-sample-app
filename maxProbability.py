from typing import List



def maxProbability(n: int, edges: List[List[int]], succProb: List[float], start: int, end: int):
    
    # convert graph into adj list
    # node ___ has edges to nodes ____
    # node  0      :        nodes  1,2


    nodeToNeighbors = dict()

    i = 0

    for eachEdge in edges:
        startNode = eachEdge[0]
        endNode = eachEdge[1]

        if start not in nodeToNeighbors:
            nodeToNeighbors[startNode] = [[endNode , succProb[i]]]
        else:
            nodeToNeighbors[startNode].append([endNode , succProb[i]])

        if end not in nodeToNeighbors:
            nodeToNeighbors[endNode] = [[startNode , succProb[i]]]
        else:
            nodeToNeighbors[endNode].append([startNode , succProb[i]])

        i+=1




    def bfs():
        queue = [] * n
        # rule : insert at end, remove from beginning   FIFO

        nodeToProbability = dict()

        nodeToProbability[start] = 1.0

        
        queue.append(start)
        

  
        while queue:
            

            currNode = queue[0]
            
            queue.pop(0)

            for eachNode in nodeToNeighbors[currNode]:
                node = eachNode[0]
                probability = eachNode[1]
                eachNodeProbability = nodeToProbability[currNode] * probability
                
                if(node not in nodeToProbability or eachNodeProbability > nodeToProbability[node]):
                    nodeToProbability[node] = eachNodeProbability
                    queue.append(node)
            
        if(end in nodeToProbability):
            return nodeToProbability[end]
        return 0
    
    res = bfs()

    return res
    
