import pygame
import sys

w, h = input(), input()
if (w.isdigit() and h.isdigit()):
    w = int(w)
    h = int(h)
    if __name__ == '__main__':
        # инициализация Pygame:
        pygame.init()
        # размеры окна:
        #w = 600
        #h = 800
        size = width, height = w, h
        # screen — холст, на котором нужно рисовать:
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption('Crest')
        # формирование кадра:
        # команды рисования на холсте
        pygame.draw.line(screen, (255, 255, 255), (0, 0), (w, h), width=5)
        pygame.draw.line(screen, (255, 255, 255), (w, 0), (0, h), width=5)
        # ...
        # ...
        # смена (отрисовка) кадра:
        pygame.display.flip()
        # ожидание закрытия окна:
        while pygame.event.wait().type != pygame.QUIT:
            pass
        # завершение работы:
        pygame.quit()
else:
    print("Неправильный формат ввода")



