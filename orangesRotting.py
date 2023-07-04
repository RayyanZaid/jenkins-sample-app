from typing import List

def orangesRotting(grid: List[List[int]]) -> int:

    numOranges = 0
    numRotten = 0

    queue = []  
        # Push - append 
        # Pop  - remove from the front

        # each node will be in the tuple format :   ( (row,col) , minutes )

    # calculate total number of oranges and total number of rotten

    rows = len(grid)
    cols = len(grid[0])


        
    for i in range(rows):
        

        for j in range(cols):

            if grid[i][j] == 1 or grid[i][j] == 2:
                numOranges += 1

                if grid[i][j] == 2:
                    node : tuple = (i,j), 0
                    queue.append(node)
                    
                    numRotten += 1
    
    # need to do BFS until the queue is empty OR numOranges == numRotten

    
    if numRotten == numOranges:
            return 0
    
    visited = set()

    while queue:

        node = queue[0]
        queue.pop(0)

        
        coordinates = node[0]

        if coordinates in visited:
            continue
        
        visited.add(coordinates)

        row = coordinates[0]
        col = coordinates[1]
        minutes = node[1]

        if  grid[row][col] == 1:
            numRotten += 1
            grid[row][col] = 2
            
        if numRotten == numOranges:
            return minutes
        
        # check all four directions

        #              up      right   down     left
        directions = [[0,-1] , [1,0] , [0,1] , [-1,0]]

        for eachDirection in directions:

            newRow = row + eachDirection[0]
            newCol = col + eachDirection[1]

            if newRow >= 0 and newRow < rows and newCol >= 0 and newCol < cols and grid[newRow][newCol] != 0:
                queue.append(((newRow,newCol) , minutes + 1))


    return -1


print(orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
print(orangesRotting([[0,2]]))