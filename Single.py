import pygame,sys
from pygame import *

pygame.init()

screen=pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption("Pong!")

## create bars
bar=pygame.Surface((12,70))
bar1=bar.convert()
bar1.fill((255,0,0))
bar2=bar.convert()
bar2.fill((0,0,255))


## making definitions
bg=pygame.Surface((640,480)).convert()
pygame.font.init()
font=pygame.font.SysFont("calibri",40)
y_1=205
y_2=205
movey_1=0
movey_2=0
speedy1=300
speedy2=250
speed_ball=250
bar_1_score=0
bar_2_score=0
move_ball_x=1
move_ball_y=1
x_ball,y_ball=320,240


while True:
	
	## Set up frame and backround
	screen.blit(bg,(0,0))
	frame=pygame.draw.rect(screen,(255,255,255),Rect((5,5),(630,470)),2)
	divider=pygame.draw.line(screen,(255,255,255),(319,5),(319,475),2)
	
	
	## Set up clock
	clock=pygame.time.Clock()
	milli=clock.tick(60)
	seconds=milli/1000.
	dy1=speedy1*seconds
	dy2=speedy2*seconds
	milli2=clock.tick()
	seconds2=milli/1000.
	d_ball=speed_ball*seconds2
	
	## Set up score
	score_1=font.render(str(bar_1_score),True,(255,255,255))
	score_2=font.render(str(bar_2_score),True,(255,255,255))
	
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
			
		## Bar_1 movement
		if event.type==KEYDOWN:
			if event.key==K_UP:
				movey_1=-dy1
			elif event.key==K_DOWN:
				movey_1=dy1
		if event.type==KEYUP:
			if event.key==K_UP:
				movey_1=0
			elif event.key==K_DOWN:
				movey_1=0
	y_1+=movey_1
	
	## keep bars from going off the screen
	if y_1<7:
		y_1=7
	if y_1>403:
		y_1=403
		
	## create ball and movement
	pygame.draw.circle(screen,(0,255,0),(int(x_ball),int(y_ball)),8)
	if x_ball<635 and move_ball_x>0:
		move_ball_x=d_ball
	if y_ball<475 and move_ball_y>0:
		move_ball_y=d_ball
	
	## bounce or score
	if (y_ball>475 and move_ball_y>0):
		move_ball_y=-d_ball
	elif y_ball<5 and move_ball_y<0:
		move_ball_y=d_ball
	if (x_ball>623 and move_ball_x>0):
		if y_ball>=y_2-8 and y_ball<=y_2+78:
			move_ball_x=-d_ball
			speed_ball+=10
		else:
			bar_1_score+=1
			x_ball,y_ball=320,240
			speed_ball=250
			move_ball_x=-d_ball
			
	if x_ball<17 and move_ball_x<0:
		if y_ball>=y_1-8 and y_ball<=y_1+78:
			move_ball_x=d_ball
			speed_ball+=10
		else:	
			bar_2_score+=1
			x_ball,y_ball=320,240
			speed_ball=250
			move_ball_x=d_ball
		
	x_ball+=move_ball_x
	y_ball+=move_ball_y
	
	## opponent movement
	if x_ball>320:
		
		if y_ball>y_2+35.:
			movey_2=dy2
		elif y_ball<y_2+35.:
			movey_2=-dy2
		elif y_2==y_ball:
			y_2=y_ball-35.
	if x_ball<320:
		movey_2=0
	
	y_2+=movey_2
	
	
	screen.blit(bar1,(7,y_1))
	screen.blit(bar2,(621,y_2))
	
	screen.blit(score_1,(280,20))
	screen.blit(score_2,(340,20))
	
	pygame.display.update()
	
	
	