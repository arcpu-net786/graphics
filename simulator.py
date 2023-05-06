import pygame
from math import sin, cos, radians

clock=pygame.time.Clock()
pygame.init()

colors = {"white":(255,255,255), "black":(0,0,0), "red":(255,0,0), "green":(0,255,0), "blue":(0,0,255), "yellow":(253, 218, 22), "road_grey":(70, 70, 70)}
gameDisplay = pygame.display.set_mode((1900,900))
gameDisplay.fill(colors["white"])

class Car:
	def __init__(self, color, x_fl, y_fl, x_fr, y_fr, x_br, y_br, x_bl, y_bl, vel=2, deg=0):
		
		self.x_fl, self.y_fl = x_fl, y_fl
		self.x_fr, self.y_fr = x_fr, y_fr
		self.x_br, self.y_br = x_br, y_br
		self.x_bl, self.y_bl = x_bl, y_bl

		self.center = (self.x_fl + self.x_fr + self.x_br + self.x_bl)/4, (self.y_fl + self.y_fr + self.y_br + self.y_bl)/4
		self.front = (self.x_fl + self.x_fr)/2, (self.y_fl + self.y_fr)/2
		self.back = (self.x_bl + self.x_br)/2, (self.y_bl + self.y_br)/2
		self.vertices = [(self.x_fl, self.y_fl), (self.x_fr, self.y_fr), (self.x_br, self.y_br), (self.x_bl, self.y_bl)]

		self.deg = deg
		self.vel = vel
		self.color = color


	def acc(self, lim, rate = 0.01):
		if self.vel < lim:
			self.vel += rate

	def dec(self, lim = 0, rate = 0.01):
		if self.vel > lim:
			self.vel -= rate


	def rot_back(self, clockwise=True, rot_val=4):
		if clockwise:
			angle = radians(rot_val)
		else:
			angle = -radians(rot_val)
		
		self.x_fl, self.y_fl = cos(angle)*(self.x_fl - self.back[0]) - sin(angle)*(self.y_fl - self.back[1]) + self.back[0], sin(angle)*(self.x_fl - self.back[0]) + cos(angle)*(self.y_fl - self.back[1]) + self.back[1]
		self.x_fr, self.y_fr = cos(angle)*(self.x_fr - self.back[0]) - sin(angle)*(self.y_fr - self.back[1]) + self.back[0], sin(angle)*(self.x_fr - self.back[0]) + cos(angle)*(self.y_fr - self.back[1]) + self.back[1]
		self.x_br, self.y_br = cos(angle)*(self.x_br - self.back[0]) - sin(angle)*(self.y_br - self.back[1]) + self.back[0], sin(angle)*(self.x_br - self.back[0]) + cos(angle)*(self.y_br - self.back[1]) + self.back[1]
		self.x_bl, self.y_bl = cos(angle)*(self.x_bl - self.back[0]) - sin(angle)*(self.y_bl - self.back[1]) + self.back[0], sin(angle)*(self.x_bl - self.back[0]) + cos(angle)*(self.y_bl - self.back[1]) + self.back[1]
		self.center = (self.x_fl + self.x_fr + self.x_br + self.x_bl)/4, (self.y_fl + self.y_fr + self.y_br + self.y_bl)/4
		self.front = (self.x_fl + self.x_fr)/2, (self.y_fl + self.y_fr)/2
		self.back = (self.x_bl + self.x_br)/2, (self.y_bl + self.y_br)/2
		self.deg += rot_val
		self.movelin(vel=2)


	def movelin(self, forward=True, vel=None):
		if forward:
			if vel == None:
				vel = self.vel
		else:
			if vel == None:
				vel = -self.vel

		self.x_fl, self.y_fl = self.x_fl + cos(radians(self.deg))*vel, self.y_fl - sin(radians(self.deg))*vel
		self.x_fr, self.y_fr = self.x_fr + cos(radians(self.deg))*vel, self.y_fr - sin(radians(self.deg))*vel
		self.x_bl, self.y_bl = self.x_bl + cos(radians(self.deg))*vel, self.y_bl - sin(radians(self.deg))*vel
		self.x_br, self.y_br = self.x_br + cos(radians(self.deg))*vel, self.y_br - sin(radians(self.deg))*vel
		self.center = (self.x_fl + self.x_fr + self.x_br + self.x_bl)/4, (self.y_fl + self.y_fr + self.y_br + self.y_bl)/4
		self.front = (self.x_fl + self.x_fr)/2, (self.y_fl + self.y_fr)/2
		self.back = (self.x_bl + self.x_br)/2, (self.y_bl + self.y_br)/2
		self.vertices = [(self.x_fl, self.y_fl), (self.x_fr, self.y_fr), (self.x_br, self.y_br), (self.x_bl, self.y_bl)]


	def draw(self):
		pygame.draw.polygon(gameDisplay, colors[self.color], [(self.x_fl,self.y_fl),(self.x_fr,self.y_fr),(self.x_br,self.y_br),(self.x_bl,self.y_bl)])


def draw_horiz_road(num_lanes=3):
	y = 350
	pygame.draw.polygon(gameDisplay, colors["road_grey"], [(0, y-10), (1900, y-10), (1900, y+211), (0, y+211)])
	pygame.draw.polygon(gameDisplay, colors["white"], [(0, y), (1900, y), (1900, y+1), (0, y+1)])
	pygame.draw.polygon(gameDisplay, colors["white"], [(0, y+200), (1900, y+200), (1900, y+201), (0, y+201)])

	pygame.draw.polygon(gameDisplay, colors["yellow"], [(0, y+97), (1900, y+97), (1900, y+98), (0, y+98)])
	pygame.draw.polygon(gameDisplay, colors["yellow"], [(0, y+103), (1900, y+103), (1900, y+104), (0, y+104)])

	for i in range(0, 1900, 40):
		pygame.draw.polygon(gameDisplay, colors["white"], [(i, y+31), (i+10, y+31), (i+10, y+32), (i, y+32)])
		pygame.draw.polygon(gameDisplay, colors["white"], [(i+5, y+64), (i+15, y+64), (i+15, y+65), (i+5, y+65)])
		
		pygame.draw.polygon(gameDisplay, colors["white"], [(i, y+135), (i+10, y+135), (i+10, y+136), (i, y+136)])
		pygame.draw.polygon(gameDisplay, colors["white"], [(i+5, y+168), (i+15, y+168), (i+15, y+169), (i+5, y+169)])


def draw_vert_road(num_lanes=3):
	x = 850
	pygame.draw.polygon(gameDisplay, colors["road_grey"], [(x-10, 0), (x+211, 0), (x+211, 900), (x-10, 900)])
	pygame.draw.polygon(gameDisplay, colors["white"], [(x, 0), (x+1, 0), (x+1, 900), (x, 900)])
	pygame.draw.polygon(gameDisplay, colors["white"], [(x+200, 0), (x+201, 0), (x+201, 900), (x+200, 900)])

	pygame.draw.polygon(gameDisplay, colors["yellow"], [(x+97, 0), (x+97, 900), (x+98, 900), (x+98, 0)])
	pygame.draw.polygon(gameDisplay, colors["yellow"], [(x+103, 0), (x+103, 900), (x+104, 900), (x+104, 0)])


	for i in range(0, 900, 40):
		pygame.draw.polygon(gameDisplay, colors["white"], [(x+31, i), (x+31, i+10), (x+32, i+10), (x+32, i)])
		pygame.draw.polygon(gameDisplay, colors["white"], [(x+64, i+5), (x+64, i+15), (x+65, i+15), (x+65, i+5)])
		
		pygame.draw.polygon(gameDisplay, colors["white"], [(x+135, i), (x+135, i+10), (x+136, i+10), (x+136, i)])
		pygame.draw.polygon(gameDisplay, colors["white"], [(x+168, i+5), (x+168, i+15), (x+169, i+15), (x+169, i+5)])

def draw_intersection():
	x = 850
	y = 350
	pygame.draw.polygon(gameDisplay, colors["road_grey"], [(800, 340), (1100, 340), (1100, 560), (800, 560)])
	pygame.draw.polygon(gameDisplay, colors["road_grey"], [(840, 300), (1060, 300), (1060, 600), (840, 600)])


car1 = Car("red", 50, 460, 50, 480, 10, 480, 10, 460, vel=4, deg=0)
car2 = Car("green", 1650, 407, 1650, 387, 1690, 387, 1690, 407, vel=2.5, deg=180)
car3 = Car("blue", 993, 850, 1013, 850, 1013, 890, 993, 890, vel=3, deg=90)

rot = 0
while True:
	clock.tick(30)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

	pygame.display.update()
	gameDisplay.fill(colors["white"])
	
	draw_horiz_road()
	draw_vert_road()
	draw_intersection()

	if car1.front[0] >= 850:
		if car1.deg < 90:
			# car.forward()
			car1.rot_back(False, 0.59)
		else:
			car1.movelin()
	else:
		car1.movelin()

	car3.movelin()

	if car2.front[0] > 1100:
		car2.movelin()
	else:
		pass #rotate


	car1.draw()
	car2.draw()
	car3.draw()
