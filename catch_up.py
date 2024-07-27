from pygame import *

#create game window
window = display.set_mode((700, 500))
display.set_caption("Catch Up")

timer = time.Clock()

#set scene background
image_bg = image.load('background.png')
background = transform.scale(image_bg, (700, 500))

vibol = transform.scale(image.load('sprite1.png'), (100, 100))
vibol_x = 100
vibol_y = 100




running = True

while running:
    window.blit(background, (0,0))
    window.blit(vibol, (vibol_x, vibol_y))

    for e in event.get():
        if e.type == QUIT:
            running = False

    keys_pressed = key.get_pressed()

    if keys_pressed[K_d] and vibol_x < 600:
        vibol_x += 2
    if keys_pressed[K_a] and vibol_x >= 0:
        vibol_x -= 2
    if keys_pressed[K_w] and vibol_y >= 0:
        vibol_y -= 2
    if keys_pressed[K_s] and vibol_y < 400:
        vibol_y += 2


    timer.tick(60)
    display.update()


