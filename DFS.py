import pygame
import sys


def dfs(maze, start_point, destination, draw):
    # Stack keeps track of the cells to visit
    stack = [start_point]
    # visited keeps track of the visited nodes
    visited = set()
    # parents dictionary keeps track of the parent nodes for each visited node
    parents = {start_point: None}
    f = open("log.txt", "w")
    f.write("Find the path to the final destination cell (4,5)\n")

    while stack:

        # Check for quit events (DO NOT EDIT)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        current_node = stack.pop()
        visited.add(current_node)
        current_node.make_closed()

        # If we have reached the destination, we can stop the search
        if current_node == destination:
            break

        # Check the neighbors of the current node
        for delta_col, delta_row in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            neighbour_col, neighbour_row = current_node.col + delta_col, current_node.row + delta_row

            # if the next delta cell is out of bounds skip this iteration
            if (neighbour_col < 0 or neighbour_col >= len(maze[0]) or neighbour_row < 0 or neighbour_row >= len(maze)):
                continue

            neighbour = maze[neighbour_row][neighbour_col]
            # If the neighbour is a valid cell and has not been visited, add it to the stack
            if ((neighbour.id != 1) and
                    neighbour not in visited):
                neighbour.make_open()
                stack.append(neighbour)

                # print current node and surrounding neighbour
                f.write(f'\ncurrent cell: {str(current_node.get_position())}\n')
                f.write(
                    f'cell {str(current_node.get_position())} has an available neighbour cell: {neighbour.get_position()}\n\n')

                parents[neighbour] = current_node
                draw()

    # If we have not found the destination, return None
    if destination not in parents:
        return None

    # Backtrack from the destination to the start point to get the path
    path = [destination]
    f.write("Backtrack from the destination to the start point to get the path, then reverse\n")
    f.write(f'last visited cell(destination) {str(path)}\n')
    while path[-1] != start_point:
        path_cell = parents[path[-1]]
        if (path_cell.id != 2):
            path_cell.set_type(4)
        path.append(path_cell)
        draw()
        f.write("move back to the previously visited cell\n\n")
        f.write(f'current cell {str(path_cell.get_position())}\n')
        f.write(f'current path from the destination back to the starting point: {str(path)}\n')

    path.reverse()

    # remove duplicates
    stack = list(set(stack))

    # find all discovered unvisited cells
    for i in stack[:]:
        if (i in path):
            stack.remove(i)

    f.write(f'\nall discovered unvisited cells: {str(stack)}\n')
    f.write(f'\nreversed(final path): {str(path)}\n')
    f.write(f'\nfinal path length: {str(len(path) - 1)} steps')