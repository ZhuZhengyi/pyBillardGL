#!/usr/bin/env python
# -*-  coding: UTF-8 -*-

try:
	from OpenGL.GL import *
	from OpenGL.GLU import *
	from OpenGL.GLUT import *
except:
	print ('Error! need PyOpenGL')
	raise SystemExit

class Decision:
	'''
	
	'''

	def __init__(self, game):
		self.game = game

	def NewGame(self, game_type):
		pass

	def NewShot(self):
		pass
