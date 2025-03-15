import pygame
import datetime

pygame.init()

# Экран өлшемдері
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock() #Кадр жиілігін басқару

# Терезе атауы
pygame.display.set_caption("Mickey Clock")

# Суреттерді жүктеу
second_arm = pygame.image.load("images/second_arm.png")
minute_arm = pygame.image.load("images/minute_arm.png")
mainclock = pygame.transform.scale(pygame.image.load("images/clock.png"), (800, 600))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # Терезені жапқанда тоқтайды
            done = True  
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: # ESC батырмасын басқанда да тоқтайды
            done = True                                                     # KEYDOWN басқан кезде,KEYUP жіберген кезде істейді
                                                                            # Ойындарда керек мысалы ату үшін,
                                                                            # KEYUP көздеп барып жіберген кезде атады

    # Қазіргі уақытқа 9 минут қосамыз әйтпесе жергілікті уақыттан қалып есептеп жатыр,
    # 9 секунд азайтамыз сонда тура 12ден асқанда минут өзгереді
    now = datetime.datetime.now() + datetime.timedelta(minutes=9, seconds=-9)
    minute = now.minute
    second = now.second

    # Бұрыштарды есептеу
    # Pygame-де оң бағыт – сағат тіліне қарсы.сондықтан "минус" қойылды
    minute_angle = - (minute * 6 + second / 10)  # Минуттық тіл
    second_angle = - (second * 6)  # Секундтық тіл

    # Фонды салу
    screen.blit(mainclock, (0,0))

    # Минуттық тіл (оң қол)
    rotated_minute_arm = pygame.transform.rotate(minute_arm, minute_angle)
    minute_rect = rotated_minute_arm.get_rect(center=(400, 300))
    screen.blit(rotated_minute_arm, minute_rect)

    # Секундтық тіл (сол қол)
    rotated_second_arm = pygame.transform.rotate(second_arm, second_angle)
    second_rect = rotated_second_arm.get_rect(center=(400, 300))
    screen.blit(rotated_second_arm, second_rect)

    pygame.display.flip()  # Терезені жаңарту
    clock.tick(60)  # FPS

pygame.quit()
