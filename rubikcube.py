import pygame

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

# Initialize Pygame
pygame.init()

# Set window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Create window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Rubik\'s Cube')

# Set cube dimensions
CUBE_SIZE = 50
CUBE_GAP = 10

# Define cube faces
FACES = {
    'U': WHITE,
    'L': GREEN,
     'F': BLUE,
    'R': RED,
        'B': YELLOW,
        'D': ORANGE
    }

# Define cube layout
layout = [
     ['U1', 'U2', 'U3', 'U4', 'U5', 'U6', 'U7', 'U8', 'U9'],
      ['L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8', 'L9'],
      ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9'],
      ['R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9'],
      ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9'],
      ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9']
     ]

 # Define cube position
 cube_x = (WINDOW_WIDTH - ((CUBE_SIZE + CUBE_GAP) * 3)) / 2
  cube_y = (WINDOW_HEIGHT - ((CUBE_SIZE + CUBE_GAP) * 4)) / 2

   # Draw cube face
   def draw_face(face, color):
        for row in range(3):
            for col in range(3):
                x = int(cube_x + ((CUBE_SIZE + CUBE_GAP) * col))
                y = int(cube_y + ((CUBE_SIZE + CUBE_GAP) * row))
                pygame.draw.rect(
                    screen, color, (x, y, CUBE_SIZE, CUBE_SIZE), 0)
                pygame.draw.rect(
                    screen, BLACK, (x, y, CUBE_SIZE, CUBE_SIZE), 1)

    # Draw cube
    def draw_cube():
        for i, face in enumerate(FACES):
            x_offset = 0
            y_offset = 0
            if face == 'U':
                x_offset = CUBE_SIZE + CUBE_GAP
                y_offset = 0
            elif face == 'L':
                x_offset = 0
                y_offset = CUBE_SIZE + CUBE_GAP
            elif face == 'F':
                x_offset = CUBE_SIZE + CUBE_GAP
                y_offset = CUBE_SIZE + CUBE_GAP
            elif face == 'R':
                x_offset = (CUBE_SIZE + CUBE_GAP) * 2
                y_offset = CUBE_SIZE + CUBE_GAP
            elif face == 'B':
                x_offset = (CUBE_SIZE + CUBE_GAP) * 3
                y_offset = CUBE_SIZE + CUBE_GAP
            elif face == 'D':
                x_offset = CUBE_SIZE + CUBE_GAP
                y_offset = (CUBE_SIZE + CUBE_GAP) * 2
            draw_face(face, FACES[face])
            for j, square in enumerate(layout[i]):
                x = int(cube_x + x_offset + ((CUBE_SIZE + CUBE_GAP) * (j % 3)))
                y = int(cube_y + y_offset + ((CUBE_SIZE + CUBE_GAP) * (j // 3)))
                pygame.draw.rect(
                    screen, BLACK, (x, y, CUBE_SIZE, CUBE_SIZE), 1)

    # Main game loop
    running = True
    while running:
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # Update screen
        screen.fill(BLACK)
        draw_cube
