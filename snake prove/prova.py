#in class Main
#grass pattern

def draw_grass(self):
    grass_color=(167,209,61) #color of that
    for row in range(cell_number):
        if row % 2 == 0:
          for col in range(cell_number):
        
           if col % 2 == 0:
               grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
               pygame.draw.rect(screen,grass_color,grass_rect)
        else:
             for col in range(cell_number):
        
                if col % 2 != 0:
                   grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                   pygame.draw.rect(screen,grass_color,grass_rect)
                   
def draw_score(self):
    score_text = str(len(self.snake.body) - 3)     
    score_surface = game_font.render(score_text,True,(56,74,12))   
    score_x = int(cell_size * cell_number - 60)
    score_y = int(cell_size * cell_number - 40)
    score_rect = score_surface.get_rect(center = (score_x,score_y))
    apple_rect = apple.get_rect(midright = (score_rect.left,score_rect.centery))
    bg_rect = pygame.Rect(apple_rect.left,apple_rect.top,apple_rect.width + score_rect.width + 6,apple_rect.height)
   
    pygame_draw.rect(screen,(167,209,61),bg_rect)
    screen.blit(score_surface,score_rect)  
    screen.blit(apple,apple_rect)   
    pygame_draw.rect(screen,(56,74,12),bg_rect,2)    
#after def draw_element(self)
# write: self.draw_grass()

#adding thw score

#after apple=pygame.image.load(.....)
game_font =pygame.font.Font(None,25)
# in def draw_element(self)
# 4 position we write self.draw_score()

#adding sound 
#class SNAKE 

self.crunch_sound = pygame.mixer.Sound('') #name of file

#afrer def add_block(self):

def play_crunch_sound(self):
    self.crunch_sound.play()
    
    #in main class in def check_collision(self):
    # write self.snake.play_crunch_sound()
    
    #pygame.mixer.pre_init(44100,-16,2,512)te punoj sound n koh
    #pygame.init() at m lart e shkruajm nj rrjsht mbi kt