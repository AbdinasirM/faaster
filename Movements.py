def BasicMove(pygame,pos,t,isJumping,jumpCount,m):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]: 
       #pygame.draw.circle(screen, "Purple", pos + (20,10), 40) 
        pos.x += 10
    if keys[pygame.K_a]: 
       #pygame.draw.circle(screen, "Purple", pos + (20,10), 40) 
        pos.x += -10
    
  