# This program is a simulation of informed and uninformed space search algorithms finding its way through the maze.

## This program requires Python version 3.9 or later and Pygame.

## How to run

* Install Pygame using
* Run the Application.py file
* Press space to run

## By default this application uses the A* algorithm

To change the algorithm open the Application.py, in line 57.  
  
``world.set_agent(0,0,lambda maze, start_block, destination_block: Astar.astar(maze=maze,start_point=start_block,destination=destination_block,draw=draw))``   
  
  
Substitute **Astar.astar** with **DFS.dfs** to use the Depth first search algorithm  
**BFS.bfs** use Breadth first search algorithm  
or **Greedy.greedy** to use Greedy search algorithm
  
