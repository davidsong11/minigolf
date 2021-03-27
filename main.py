import pygame

pygame.init()
wn = pygame.display.set_mode((600,600))

xball = 500 
yball = 550
xspeed = 0
yspeed = 0
holeR = 30
strokes = 0

water = [(400,50,150,400), (50,400,200,70)]
sand = [(200,200,70,70), (260,70,70,150), (10,10,50,150), (10,10,150,50)]

font = pygame.font.Font('VGAFIX.FON', 30)

while True:
  wn.fill((24,110,47))
  pygame.time.delay(10)
  
  xball += xspeed
  yball += yspeed
  
  cursorpos = pygame.mouse.get_pos()
  # pos is a (x, y)

  if xball >= 600 or xball <= 0:
    xspeed *= -1
  if yball >= 600 or yball <= 0:
    yspeed *= -1
  
  if abs(xspeed) < 0.01 and abs(yspeed) < 0.01:
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONUP:
        xspeed = (cursorpos[0] - xball)/15
        yspeed = (cursorpos[1] - yball)/15
        strokes += 1
  
  xspeed *= 0.95
  yspeed *= 0.95

  

  for x in water:
    waterbox = pygame.draw.rect(wn, (54, 84, 217), x)
    if waterbox.collidepoint(xball,yball):
      xball = 500
      yball = 500
      xspeed = 0
      yspeed = 0

  for x in sand:
    sandbox = pygame.draw.rect(wn, (217, 163, 69), x)
    if sandbox.collidepoint(xball,yball):
      xspeed *= 0.95
      yspeed *= 0.95
  
  if abs(xspeed) < 0.1 and abs(yspeed) < 0.1:
    pygame.draw.line(wn,(255,165,0),(xball,yball),cursorpos)

  hole = pygame.draw.circle(wn,(255,255,255),(100,100),holeR)

  if hole.collidepoint(xball,yball) and abs(xspeed) < 0.01 and abs(yspeed) < 0.01:
    winmsg = font.render(f'Nice! {strokes} strokes!', True, (255,255,255), (24,110,47))
    wn.blit(winmsg, (250,250))

  pygame.draw.circle(wn,(0,0,0),(100,100),28)
  pygame.draw.circle(wn,(255,255,255),(xball,yball),20)

  pygame.display.update()