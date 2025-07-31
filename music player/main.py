# commands to import presents

import pygame
import asyncio


pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('leadwave memories.ogg')
pygame.mixer.music.set_volume(.1)
pygame.mixer.music.play(-1)
screen_width = 30
screen_height = 30
screen = pygame.display.set_mode((screen_width, screen_height))
play_image = pygame.image.load('play.png').convert_alpha()
pause_image = pygame.image.load('pause.png').convert_alpha()

button_rect = play_image.get_rect(center=(screen_width // 2, screen_height // 2))




async def main():
    is_playing = True
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button click
                    if button_rect.collidepoint(event.pos):
                        if is_playing:
                            pygame.mixer.music.pause() #pause function with fade out to prevent white noise
                            is_playing = False
                        else:
                            pygame.mixer.music.unpause()  # If paused, unpause
                            if not pygame.mixer.music.get_busy():  # If not currently playing, start from the beginning
                                pygame.mixer.music.play()
                            is_playing = True



        # Clear the screen
        screen.fill((0, 0, 0))  # Black background

        # Draw the appropriate button image
        if is_playing:
            screen.blit(pause_image, button_rect)
        else:
            screen.blit(play_image, button_rect)

        pygame.display.flip()
        await asyncio.sleep(0)

asyncio.run(main())
