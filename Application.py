import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import Astar
import DFS
import BFS
import Greedy

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600


#This will create a window object and automatically display it
WIN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

#Setting window title
pygame.display.set_caption("AI-coursework (Visualiser)")

#Frames per second - determines how many times the window will update each second
FPS = 5
clock = pygame.time.Clock()

#Initialise the fonts module
pygame.font.init()

#A tuple representing the colour used to clear the screen each frame
#(RED, GREEN, BLUE) - values must be from 0 to 255
CLEAR_COLOUR = (0,0,0)

#Importing world object and initialising
from World import World

maze = [[0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0]]

world = World(maze)

def draw():
    #Clear the window with a black colour 
    WIN.fill(CLEAR_COLOUR)
    
    world.draw(WIN)

    #Update the window screen
    pygame.display.update()
    clock.tick(FPS)



#Main loop of the application
def main():
    run = True
    #Adding the agent to the world
    world.set_agent(0,0,lambda maze, start_block, destination_block: Astar.astar(maze=maze,start_point=start_block,destination=destination_block,draw=draw))
    world.set_end_point(5,4)


    while run:
        #Handling all application events: keyboard inputs, mouse inputs, window events, etc.
        for event in pygame.event.get():

            #If the user clicked the close button of the window then stop running the application (DO NOT REMOVE/MODIFY THIS EVENT)
            if event.type == pygame.QUIT:
                run = False
                break


            elif event.type == pygame.KEYUP:

                world.reset_world()
                #Run the agent when space is pressed
                if event.key == pygame.K_SPACE:
                    world.run_agent()
                #Reset the world in it's initial state whe 'R' is pressed
                elif event.key == pygame.K_r:
                    world.reset_world()

        draw()

        
    pygame.quit()


#Executes the main function if this python file is executed directly
if __name__ == "__main__":
    main()