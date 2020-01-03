from termcolor import colored
import os
import random

b = 'blue'

w = 'white'

g = 'green'

y = 'yellow'

r = 'red'

o = 'magenta'

configcubestart = []

front = [[b, b, b,],  # front
				[b, b, b,],
				[b, b, b,]]

back = [[g, g, g,],  # back
				[g, g, g,],
				[g, g, g,]]

top = [[y, y, y,],  # top
				[y, y, y,],
				[y, y, y,]]

bottom = [[w, w, w,],  # bottom
				[w, w, w,],
				[w, w, w,]]

right = [[r, r, r,],  # right
				[r, r, r,],
				[r, r, r,]]

left = [[o, o, o,],  # left
				[o, o, o,],
				[o, o, o,]]

configcubestart.append(front)
configcubestart.append(back)
configcubestart.append(top)
configcubestart.append(bottom)
configcubestart.append(right)
configcubestart.append(left)

t = ((0, 0), (0, 1), (0, 2))
r = ((0, 2), (1, 2), (2, 2))
b = ((2, 2), (2, 1), (2, 0))
l = ((2, 0), (1, 0), (0, 0))


class cube:
	def __init__(self):

		self.front = front
		self.back = back
		self.top = top
		self.bottom = bottom
		self.right = right
		self.left = left

	def rotateside(self, side, oldconfig):
		front = oldconfig[0]
		back = oldconfig[1]
		top = oldconfig[2]
		bottom = oldconfig[3]
		right = oldconfig[4]
		left = oldconfig[5]
		configverfront = [left, top, right, bottom]
		confighorizontal = [front, left, back, right]
		configverright = [front, top, back, bottom]
		configverfrontreversed = [bottom, right, top, left]
		confighorizontalreversed = [right, back, left, front]
		configverrightreversed = [bottom, back, top, front]
		if list(side) == front:
			config = configverfront
			rowtotake = [r, b, l, b]
			opposide = back
		if side == back:
			config = configverfrontreversed
			rowtotake = [t, r, t, l]
			opposide = front
		if side == top:
			config = confighorizontal
			rowtotake = [t, t, t, t]
			opposide = bottom
		if side == bottom:
			config = confighorizontalreversed
			rowtotake = [b, b, b, b]
			opposide = top
		if side == right:
			config = configverright
			rowtotake = [r, r, l, l]
			opposide = left
		if side == left:
			config = configverrightreversed
			rowtotake = [r, r, l, l]
			opposide = right
		return config, rowtotake, opposide

	def rotation(self, side, direction, oldconfig):
		if direction == "r":
			rotatedside = list(zip(*reversed(side)))
			#print(rotatedside)

		if direction == "l":
			rotatedside = list(
				zip(*reversed(list(zip(*reversed(list(zip(*reversed(side)))))))))
		rside = []
		for t in rotatedside:
			rside.append(list(t))
		rotatedside = rside
		config, rowtotake, opposide = self.rotateside(side, oldconfig)
		con = []
		for z in config:
			con.append(z)


		if side == oldconfig[0]:
			front = rotatedside
			back = opposide
		if side == oldconfig[1]:
			 back= rotatedside
			 front = opposide
		if side == oldconfig[2]:
			top = rotatedside
			bottom = opposide
		if side == oldconfig[3]:
			bottom = rotatedside
			top = opposide
		if side == oldconfig[4]:
			right = rotatedside
			left = opposide
		if side == oldconfig[5]:
			left = rotatedside
			right = opposide
		cube = self.rotationedges(side, direction, config, rowtotake)
		for p in range(0, len(con)):
			if con[p] == oldconfig[0]:
				front = cube[p]
			if con[p] == oldconfig[1]:
				back = cube[p]
			if con[p] == oldconfig[2]:
				top = cube[p]
			if con[p] == oldconfig[3]:
				bottom = cube[p]
			if con[p] == oldconfig[4]:
				right = cube[p]
			if con[p] == oldconfig[5]:
				left = cube[p]
		configcube = []
		configcube.append(front)
		configcube.append(back)
		configcube.append(top)
		configcube.append(bottom)
		configcube.append(right)
		configcube.append(left)	
		return configcube
	
	def edgeconfiguration(self, config,rowtotake):
		edgeconfig = []
		for q in range(4):
			for coordinates in rowtotake[q]:
				plane = config[q]

				edgeconfig.append(plane[coordinates[0]][coordinates[1]])
		return edgeconfig

	def edgechange(self, config, rowtotake, newedgeconfig):
		i = 0
		#print(newedgeconfig)
		for q in range(4):
			plane = config[q]
			for coordinates in rowtotake[q]:

				listplane = [list(item) for item in plane]
				listplane[coordinates[0]][coordinates[1]] = newedgeconfig[i]
				#print(listplane)
				i += 1
				plane = listplane
			config[q] = plane
		return config
	def shift(self, seq, n):
		a = n % len(seq)
		return seq[-a:] + seq[:-a]
	
	def rotationedges(self, side, direction, config, rowtotake):
		edgeconfig = self.edgeconfiguration(config,rowtotake)
		if direction == "r":
			return self.edgechange(config, rowtotake, self.shift(edgeconfig, 3))
		if direction == "l":
			return self.edgechange(config, rowtotake, self.shift(edgeconfig, -3))
	#def edgeselection(self, direction, config, rowtotake):

# def reorder(newconfigcube):
# 	endconfigcube = [0,0,0,0,0,0]
# 	for side in configcube:
# 		print(side)
# 		if side == front:
# 			endconfigcube[0] = side
# 		if side == back:
# 			endconfigcube[1] = side
# 		if side == top:
# 			endconfigcube[2] = side
# 		if side == bottom:
# 			endconfigcube[3] = side
# 		if side == right:
# 			endconfigcube[4] = side
# 		if side == left:
# 			endconfigcube[5] = side
# 		print(side)
# 	return endconfigcube


def rotate(side, direction, configcubecube):
	p = cube()
	p.front = configcubecube[0]
	p.back = configcubecube[1]
	p.top = configcubecube[2]
	p.bottom = configcubecube[3]
	p.right = configcubecube[4]
	p.left = configcubecube[5]
	return p.rotation(side, direction, configcubecube)
	# endconfigcube = [0,0,0,0,0,0]
	# for face in p.rotation(side, direction):
	# 	if face == front:
	# 		endconfigcube[0] = face
	# 	if face == back:
	# 		endconfigcube[1] = face
	# 	if face == top:
	# 		endconfigcube[2] = face
	# 	if face == bottom:
	# 		endconfigcube[3] = face
	# 	if face == right:
	# 		endconfigcube[4] = face
	# 	if face == left:
	# 		endconfigcube[5] = face
	# return endconfigcube

def show(configcube):
	#os.system('clear')
	for row in configcube[2]:
		print('       ', end='')
		for color in row:
			print(colored('#', color), end=' ')
		print('\n', end='')
	print('')
	for i in range(0,3):
		for color in configcube[5][i]:
			print(colored('#', color), end=' ')
		print(' ', end='')
		for color in configcube[0][i]:
			print(colored('#', color), end=' ')
		print(' ', end='')
		for color in configcube[4][i]:
			print(colored('#', color), end=' ')
		print(' ', end='')
		for color in configcube[1][i]:
			print(colored('#', color), end=' ')
		print('')
	print('')
	for  g in range(0,3):
		print('       ', end='')
		for z in range(0,3):
			print(colored('#', configcube[3][-(g + 1)][-(z + 1)]), end=' ')
		print('\n', end='')

class player:
	def __init__(self):
		ier = 0
	def play(self, side=None, direction=None, configcubecube=None):
		if side == None:
			side = input("What side do you want to rotate?")
			if side == "front":
				side = front
			if side == "back":
				side = back
			if side == "top":
				side = top
			if side == "bottom":
				side = bottom
			if side == "right":
				side = right
			if side == "left":
				side = left
		if direction == None:
			direction = input("What direction do you want to rotate?")
			if direction == "r":
				direction = "r"
			if direction == "l":
				direction = "l"
		if configcubecube == None:
			p = cube()
			p.front = configcubestart[0]
			p.back = configcubestart[1]
			p.top = configcubestart[2]
			p.bottom = configcubestart[3]
			p.right = configcubestart[4]
			p.left = configcubestart[5]
			configcubecube = p.rotation(side, direction, configcubestart)
			return configcubecube

		if not configcubecube == None:
			p = cube()
			p.front = configcubecube[0]
			p.back = configcubecube[1]
			p.top = configcubecube[2]
			p.bottom = configcubecube[3]
			p.right = configcubecube[4]
			p.left = configcubecube[5]
			configcubecube = p.rotation(side, direction, configcubecube)
	
			return configcubecube


def randomize():
	u = player()
	configcubecube = None
	sides = [front, back, top, bottom, right, left]
	for i in range(1 , random.randint(2,10)):
		directions = ["r","l"]
		side = random.choice(sides)
		direction = random.choice(directions)
		configcubecube = u.play(side = side, direction = direction, configcubecube = configcubecube)
		sides = []
		sides.append(configcubecube[0])
		sides.append(configcubecube[1])
		sides.append(configcubecube[2])
		sides.append(configcubecube[3])
		sides.append(configcubecube[4])
		sides.append(configcubecube[5])
	if configcubecube == None:
		print(side, direction, configcubecube)	
	
	show(configcubecube)
	return configcubecube