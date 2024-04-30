import asyncio
import sys

import pygame


COLORS = ('yellow', 'blue', 'red')

async def main():
    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode((1920, 1080))
    clock = pygame.time.Clock()

    color_index = 0

    while True: # EVENT LOOP
        for event in pygame.event.get():
            if not event.type == pygame.KEYUP:
                continue

            if event.key == pygame.K_SPACE:
                color_index = (color_index + 1) % len(COLORS)
                new_color = COLORS[color_index]
                screen.fill(new_color)
                pygame.display.update()

            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        clock.tick(25) # Frame per second (FPS)
        await asyncio.sleep(0)


if __name__ == '__main__':
    asyncio.run(main())
