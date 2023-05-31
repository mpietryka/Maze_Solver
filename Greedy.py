import pygame, sys, heapq, math

# Define heuristic function (Manhattan distance)
def heuristic(source, destination):
    return abs(source[0]-destination[0]) + abs(source[1]-destination[1])


def greedy(maze, start_point, destination, draw):
    # Define possible moves from each cell (up, down, left, right)
    moves = [(0,-1), (0,1), (-1,0), (1,0)]

    # Initialize priority queue with start point and its heuristic value
    queue = [(heuristic(start_point.get_position(), destination.get_position()), start_point)]

    # Initialize dictionary to keep track of parents
    parents = {start_point: None}

    # Perform greedy search
    while queue:

        #Check for quit events (DO NOT EDIT)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        cell = heapq.heappop(queue)[1]
        cell.make_closed()

        if cell.id == 3:
            break

        for move in moves:
            #Calculate the next cell
            delta_cell = (cell.col + move[0], cell.row + move[1])
            
            #Check if the next cell is within maze bounds. Skip iteration if not within bounds
            if(delta_cell[0] < 0 or delta_cell[0] >= len(maze[0]) or delta_cell[1] < 0 or delta_cell[1] >= len(maze)):
                continue
            
            new_cell = maze[delta_cell[1]][delta_cell[0]]
            
            #Check if the new cell is an obstacle and add it to the queue
            if (new_cell.id != 1 and new_cell not in parents):
                parents[new_cell] = cell
                heapq.heappush(queue, (heuristic(new_cell.get_position(), destination.get_position()), new_cell))
                new_cell.make_open()
        
        draw()

    # Reconstruct path from destination to start point
    path = [destination]
    while path[-1] != start_point:
        path_cell = parents[path[-1]]

        if(path_cell.id != 2):
            path_cell.set_type(4)

        path.append(path_cell)

        draw()

    path.reverse()

    print("path: ")
    print(path)