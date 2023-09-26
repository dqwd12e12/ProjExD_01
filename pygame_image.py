import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_image2 = pg.transform.rotozoom(kk_img, 10, 1.0)
    kk_image_list = [kk_img, kk_image2]
    bg_image_list = [bg_img, bg_img2]*2
    tmr = 0
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr%3200
        for i in range(2):
            screen.blit(bg_image_list[i],[3200*i-x,0])

        #screen.blit(bg_img, [-x, 0])
        #screen.blit(bg_img2, [1600-x, 0])
        screen.blit(kk_image_list[tmr//200%2], [300, 200])
        pg.display.update()
        tmr += 1        
        clock.tick(1000) 


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()