import pygame

w, h = input(), input()
size = w, h = int(w), int(h)

pygame.init()
surface = pygame.display.set_mode(size)
pygame.display.set_caption(f"{w}x{h}")
pygame.draw.line(surface, (255, 255, 255), (0, 0), (w, h), width=5)
pygame.draw.line(surface, (255, 255, 255), (0, w), (h, 0), width=5)
while pygame.event.wait().type != pygame.QUIT:
    pygame.display.update()
pygame.quit()