#!/usr/bin/env python
# -*-  coding: UTF-8 -*-

from Param import *

try:
	from OpenGL.GL import *
	from OpenGL.GLU import *
	from OpenGL.GLUT import *
except:
	print ('Error! need PyOpenGL')
	raise SystemExit

	
class Judge:
	'''
	'''
	def __init__(self, game):
		self.game = game

	def NewGame(self, type):
		self.game.type = type
		
		pass

	def NewShot(self):

		pass

	def Decisioning(self):
		pass

	def CorrectBallWithPlay(self):
		pass

	def BallBall(self):
		pass

	def BallBand(self):
		pass

	def BallHole(self):

if __name__ == '__main__':
	pass
	
