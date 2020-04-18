import pygame as pg
from pgquadtree import quad_tree, cell, point

if __name__ == '__main__':

################################ EXAMPLE ########################################
    #
    # c  = cell(400, 400, 400)
    # qt = quad_tree(c, 4)
    #
    # qt.insert(point(100, 200))      
    # qrcell = cell(500, 500, 100)
    # fnd    = qt.query(qrcell)
    #
############################ INITIALIZATION ####################################


    c  = cell(400, 400, 400, 400)
    qt = quad_tree(c, 4)

###################### OPERATIONS AND GRAPHICS ##################################
    class button:
        def __init__(self, position, size, clr=[100, 100, 100], cngclr=None, func=None, text='', font="Segoe Print", font_size=16, font_clr=[0, 0, 0]):
            self.clr    = clr
            self.size   = size
            self.func   = func
            self.surf   = pg.Surface(size)
            self.rect   = self.surf.get_rect(center=position)

            if cngclr:
                self.cngclr = cngclr
            else:
                self.cngclr = clr

            if len(clr) == 4:
                self.surf.set_alpha(clr[3])


            self.font = pg.font.SysFont(font, font_size)
            self.txt = text
            self.font_clr = font_clr
            self.txt_surf = self.font.render(self.txt, 1, self.font_clr)
            self.txt_rect = self.txt_surf.get_rect(center=[wh//2 for wh in self.size])

        def draw(self):
            self.mouseover()

            self.surf.fill(self.curclr)
            self.surf.blit(self.txt_surf, self.txt_rect)
            screen.blit(self.surf, self.rect)

        def mouseover(self):
            self.curclr = self.clr
            pos = pg.mouse.get_pos()
            if self.rect.collidepoint(pos):
                self.curclr = self.cngclr

        def call_back(self, *args):
            if self.func:
                self.func(*args)

    class text:
        def __init__(self, msg, position, clr=[100, 100, 100],  font="Segoe Print", font_size=15, mid=False):
            self.position = position
            self.font = pg.font.SysFont(font, font_size)
            self.txt_surf = self.font.render(msg, 1, clr)

            if len(clr) == 4:
                self.txt_surf.set_alpha(clr[3])

            if mid:
                self.position = self.txt_surf.get_rect(center=position)


        def draw(self):
            screen.blit(self.txt_surf, self.position)



    def button_fn(*args):
        global insert_flag, query_flag, box
        insert_flag, query_flag = query_flag, insert_flag
        box = []
        surf.fill(bg)
        qt.draw(surf)

                        

    pg.init()

    screen_size = (1540, 800)
    bg          = (0, 0, 0)
    position    = (350, 0)
    surf        = pg.Surface((800, 800))
    rect        = surf.get_rect(topleft=position)

    font_size = 15
    font = pg.font.SysFont("Segoe Print", font_size)

    screen = pg.display.set_mode(screen_size)
    pg.display.set_caption('QUAD TREE')
    clock = pg.time.Clock()
  
    surf.fill(bg)
    qt.draw(surf)



    irt = button(( 150, 100), (200, 50), (220, 220, 220), (255, 255, 0), button_fn, 'insert/query')

    crash       = True
    insert_flag = True
    query_flag  = False
    box         = []
    fnd         = []

    while crash:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                crash = False

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    crash = False


            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pg.mouse.get_pos()
                    if irt.rect.collidepoint(pos):
                        irt.call_back()


                    if rect.collidepoint(pos):
                        if insert_flag:
                            qt.insert(point(pos[0]-position[0], pos[1]-position[1]))
                            surf.fill(bg)
                            qt.draw(surf)

                        elif query_flag:
                            if len(box) < 2:
                                box.append((pos[0]-position[0], pos[1]-position[1]))
                            if len(box) == 2:   
                                qrcell = cell((box[0][0]+box[1][0])/2, (box[0][1]+box[1][1])/2, abs((box[0][0]-box[1][0]))/2, abs((box[0][1]-box[1][1]))/2)
                                fnd = qt.query(qrcell)
                                qrcell.draw(surf, (0, 0, 255))
                                for pt in fnd:
                                    pt.draw(surf, (0, 255, 0))


        screen.fill(bg)
        irt.draw()

        screen.blit(surf, position)
        
        cur_fps = font.render(str(int(clock.get_fps())), False, (255, 0, 0))
        screen.blit(cur_fps, (10, 10))
        
        t = text("current mode: insert" if insert_flag else "current mode: query", (150, 450), clr=[255, 255, 255], font_size=25, mid=True)
        t.draw()        
        t = text("QUAD TREE DETAILS", (1350, 250), clr=[255, 0, 255], font_size=30, mid=True)
        t.draw()        
        t = text("node capacity: "+str(qt.capacity), (1350, 350), clr=[255, 255, 255], font_size=25, mid=True)
        t.draw()   
        t = text("tree height  : "+str(qt.hgt), (1350, 400), clr=[255, 255, 255], font_size=25, mid=True)
        t.draw()
        t = text("total points : "+str(qt.n_points), (1350, 450), clr=[255, 255, 255], font_size=25, mid=True)
        t.draw()
        if query_flag:
            t = text(str(len(fnd))+" - points found", (150, 490), clr=[255, 255, 255], font_size=18, mid=True)
            t.draw()    

        pg.display.update()
        clock.tick(144)

