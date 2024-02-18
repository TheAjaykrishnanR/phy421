import pygame
from math import sin, cos, pi

class double_pendulum:

    '''pygame vars'''
    
    screen = pygame.display.set_mode([500, 500])
    running = True

    '''pendulum vars'''

    m1: float
    m2: float
    l1: float
    l2: float
    th1: list[float]
    th2: list[float]

    hookpos = (250, 100)

    def __init__(self, data: list):
                
        pygame.init()

        # self.m1, self.m2, self.l1, self.l2, self.th1, self.th2 = data

        while self.running == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()

                self.screen.fill((255, 255, 255))
                pygame.draw.line(self.screen, (0, 0, 0), self.hookpos, self.theta_to_xy(pi/4, 100), 2)

                self.draw_elements()

                # frame render
                pygame.display.flip()
        
    def draw_elements(self):
        pygame.draw.circle(self.screen, (0,0,0), (250, 100), 5, 2)

    def theta_to_xy(self, theta, l):
        x = self.hookpos[0] + l*sin(theta)
        y = self.hookpos[1] + l*cos(theta)
        return (x, y)


dp = double_pendulum([])