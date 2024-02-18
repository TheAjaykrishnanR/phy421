import pygame
import math
from DoublePendulum import NODES

# Initialize Pygame
pygame.init()

# NODES computation
state = {'x':0, 'y0': 0, 'y1': 0.1, "y2": 0, "y3":0}
evolvers = {'y0': "y1", 
            'y1': "0.01*cos(y2-y0)*(-y1^2*sin(y2-y0)-9.8*sin(y2))/(1.01-0.01*(cos(y2-y0))^2)", 
            "y2": "y3", 
            "y3": "(-y1^2*tan(y2-y0)-(9.8*sin(y2))/cos(y2-y0))/((0.01/1.01)*0.01*cos(y2-y0)+0.01/cos(y2-y0))"}


# Constants
width, height = 800, 800
length1, length2 = 150, 150


 # List of values for theta
with open('theta', 'r') as file:
    theta_values = [float(line.strip()) for line in file]

# Pygame setup
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Double Pendulum Simulation")
clock = pygame.time.Clock()

# Function to convert polar coordinates to Cartesian coordinates
def polar_to_cartesian(theta):
    x1 = length1 * math.sin(theta)
    y1 = length1 * math.cos(theta)

    return int(x1), int(y1)

# Main loop
running = True
index = 0  # Index to track values in the lists
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    # Update angles
    theta1 = theta_values[index]


    # Draw pendulum
    x1, y1 = polar_to_cartesian(theta1)
    pygame.draw.line(screen, (0, 0, 0), (width // 2, height // 2), (x1 + width // 2, y1 + height // 2), 5)
    pygame.draw.circle(screen, (0, 0, 255), (x1 + width // 2, y1 + height // 2), 10)

    pygame.display.flip()
    clock.tick(10)

    # Switch to the next set of angles after a certain time
    if index == len(theta_values) - 1:
        index = 0

    index += 10

pygame.quit()
