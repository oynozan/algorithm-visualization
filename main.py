import pygame
import random
import algorithms

algorithms = algorithms.Algorithms()

#Screen
WINDOW_WIDTH = 1000; WINDOW_HEIGHT = 600

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

#Screen Settings
pygame.display.set_caption("Bubble Sort")

#Data
datas = []
dataCount = 1000

for counter in range(dataCount):
	datas.append(random.randint(1, WINDOW_HEIGHT))

#Game Loop
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill((0,0,0))

	#Draw Data Rectangles
	for counter in range(dataCount):
		rectWidth = WINDOW_WIDTH / dataCount
		rectHeight = datas[counter]
		rectX = counter * rectWidth
		rectY = WINDOW_HEIGHT - rectHeight

		pygame.draw.rect(screen, (255,255,255), (rectX, rectY, rectWidth, rectHeight))

	datas = algorithms.BubbleSort(datas)
	
	clock.tick(30)
	pygame.display.update()