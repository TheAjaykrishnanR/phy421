import pygame
import math
import time

# Initialize Pygame
pygame.init()

# Constants
width, height = 800, 600
length1, length2 = 150, 150

with open('theta1_1values', 'r') as file:
    theta1_1values = [float(line.strip()) for line in file]
with open('theta2_1values', 'r') as file:
    theta2_1values = [float(line.strip()) for line in file]
with open('theta1_2values', 'r') as file:
    theta1_2values = [float(line.strip()) for line in file]
with open('theta2_2values', 'r') as file:
    theta2_2values = [float(line.strip()) for line in file]
   # Initial angles for the second pendulum

# Pygame setup
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Double Pendulum Simulation")
clock = pygame.time.Clock()

# Function to convert polar coordinates to Cartesian coordinates
def polar_to_cartesian(theta1, theta2):
    x1 = length1 * math.sin(theta1)
    y1 = length1 * math.cos(theta1)

    x2 = x1 + length2 * math.sin(theta2)
    y2 = y1 + length2 * math.cos(theta2)

    return int(x1), int(y1), int(x2), int(y2)

# Main loop
index = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    # Update angles for the first pendulum
    theta1_1 = theta1_1values[index]
    theta2_1 = theta2_1values[index]

    # Update angles for the second pendulum
    theta1_2 = theta1_2values[index]
    theta2_2 = theta2_2values[index]

    # Draw first pendulum
    x1_1, y1_1, x2_1, y2_1 = polar_to_cartesian(theta1_1, theta2_1)
    pygame.draw.line(screen, (0, 0, 0), (width // 2, height // 2), (x1_1 + width // 2, y1_1 + height // 2), 5)
    pygame.draw.line(screen, (0, 0, 0), (x1_1 + width // 2, y1_1 + height // 2), (x2_1 + width // 2, y2_1 + height // 2), 5)
    pygame.draw.circle(screen, (0, 0, 255), (x1_1 + width // 2, y1_1 + height // 2), 10)
    pygame.draw.circle(screen, (255, 0, 0), (x2_1 + width // 2, y2_1 + height // 2), 10)

    # Draw second pendulum
    x1_2, y1_2, x2_2, y2_2 = polar_to_cartesian(theta1_2, theta2_2)
    pygame.draw.line(screen, (0, 0, 0), (width // 2, height // 2), (x1_2 + width // 2, y1_2 + height // 2), 5)
    pygame.draw.line(screen, (0, 0, 0), (x1_2 + width // 2, y1_2 + height // 2), (x2_2 + width // 2, y2_2 + height // 2), 5)
    pygame.draw.circle(screen, (0, 0, 255), (x1_2 + width // 2, y1_2 + height // 2), 10)
    pygame.draw.circle(screen, (255, 0, 0), (x2_2 + width // 2, y2_2 + height // 2), 10)

    pygame.display.flip()
    clock.tick(10)

    if index == len(theta1_1values):
        index = 0
    if index == 0:
        time.sleep(3)

    index += 10
pygame.quit()
