import pygame
import os
import sys

pygame.init()
size = width, height = 1366, 768
screen = pygame.display.set_mode(size)
color = (255, 0, 0, 0)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


# Загрузка начального изображения
image_start_background = load_image("menu.png")
image_start_background = pygame.transform.scale(image_start_background, size)

# Создание непрозрачных прямоугольников для кнопок на начальном экране
button_play_start = pygame.Rect(560, 470, 280, 80)

surface3 = pygame.Surface(button_play_start.size, pygame.SRCALPHA)
surface3.fill(color)

# Загрузка изображений стен
image_wall1 = load_image("1.png")
image_wall2 = load_image("2.png")
image_wall3 = load_image("4.png")
image_wall4 = load_image("3.png")
image_wall1 = pygame.transform.scale(image_wall1, size)
image_wall2 = pygame.transform.scale(image_wall2, size)
image_wall3 = pygame.transform.scale(image_wall3, size)
image_wall4 = pygame.transform.scale(image_wall4, size)

sp_images = [image_wall1, image_wall2, image_wall3, image_wall4]
ind = 0
background = sp_images[ind]

# Загрузка изображений стрелок
image_arrow_left = load_image("arrow_left.png")
image_arrow_right = load_image("arrow_right.png")
image_arrow_left = pygame.transform.scale(image_arrow_left, (50, 50))
image_arrow_right = pygame.transform.scale(image_arrow_right, (50, 50))

# Создание непрозрачных прямоугольников для стрелок
change_area = pygame.Rect(10, (height - 50) // 2, 30, 50)
change_area2 = pygame.Rect(width - 40, (height - 50) // 2, 30, 50)

surface = pygame.Surface(change_area.size, pygame.SRCALPHA)
surface.fill(color)

surface2 = pygame.Surface(change_area2.size, pygame.SRCALPHA)
surface2.fill(color)

if __name__ == '__main__':
    pygame.display.set_caption('Room')
    all_sprites = pygame.sprite.Group()

    fps = 30
    clock = pygame.time.Clock()
    running = True
    flag = True
    while running:
        if flag:
            # Отображение фона
            screen.blit(image_start_background, (0, 0))
            screen.blit(surface3, button_play_start.topleft)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if button_play_start.collidepoint(event.pos):
                        flag = False
                    # Смена стен в левую сторону
                    if change_area.collidepoint(event.pos):
                        background = sp_images[(ind - 1) % len(sp_images)]
                        ind -= 1
                    # Смена стен в правую сторону
                    if change_area2.collidepoint(event.pos):
                        background = sp_images[(ind + 1) % len(sp_images)]
                        ind += 1
        if not flag:
            # Отображение стены
            screen.blit(background, (0, 0))

            ar_left = screen.blit(image_arrow_left, (0, (height - 50) // 2))
            ar_right = screen.blit(image_arrow_right, (width - 50, (height - 50) // 2))

            # Отображение области для обработки нажатия на стрелку
            screen.blit(surface, change_area.topleft)
            screen.blit(surface2, change_area2.topleft)

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
