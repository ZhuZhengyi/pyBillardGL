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

class MouseKey:
	'''
	
	'''
	MouseButton = 0

	def __init__(self, game):
		self.game = game
		self.KEY_UP = 0
		self.KEY_DOWN = 0
		self.KEY_RIGHT = 0
		self.KEY_LEFT = 0
		self.KEY_SHIFT = 0
		self.KEY_CTRL = 0
		self.KEY_PAGE_UP = 0
		self.KEY_PAGE_DOWN = 0
		self.KEY_HOME = 0
		self.KEY_END = 0


		self.MouseButtonIntercepted = 0
		self.MouseLookLast_x = 0
		self.MouseLookLast_y = 0

	def MouseClick(self, btn, state, x, y):
		if self.game.menu.MouseClick(btn, state, x, y) != 0:
			self.MouseButtonIntercepted = 1
		else:
			self.MouseButtonIntercepted = 0
			self.MouseLookLast_x = x
			self.MouseLookLast_y = y

		if (btn == GLUT_LEFT_BUTTON and state == GLUT_DOWN):
			MouseButton = GLUT_LEFT_BUTTON
		if (btn == GLUT_RIGHT_BUTTON and state == GLUT_DOWN):
			MouseButton = GLUT_RIGHT_BUTTON
		if (btn == GLUT_MIDDLE_BUTTON and state == GLUT_DOWN):
			MouseButton = GLUT_LEFT_BUTTON	
			if (self.game.state == GameState.VIEWING):
				self.game.state = GameState.AIMING
				self.game.menu.NewMenuState()
				self.game.camera.EyesOn(self.game.balls[0].Pos_xCM(), balls[0].Pos_yCM())
			elif (self.game.state == GameState.AIMING):
				self.game.state = GameState.SWING
				self.game.menu.NewMenuState()
			elif (self.game.state == GameState.SHOT):
				pass
			
		pass
	
	def MouseMove(self, x, y):
		pass

	def KeyPress(self,key, x, y):
		pass

	def KeyRelease(self, key, x, y):
		pass
	
	def SpecialKeyPress(self, key, x, y):
		if  self.game.state != GameState.START:
			if key == GLUT_KEY_F1:
				if ( self.game.state != GameState.SWING ):
					if (self.game.state != GameState.SHOT 
					and self.game.state!= GameState.NEW_WHITE 
					and self.game.state!= GameState.JUDGEING) :
						self.game.state=GameState.VIEWING
						self.game.menu.NewMenuState()
					self.game.camera.loadPosition(0);
			elif  key == GLUT_KEY_F2:
				if (self.game.state!=GameState.SWING) :
					if (machineState!=GameState.SHOT 
					and machineState!=GameState.NEW_WHITE 
					and machineState!=GameState.JUDGEING) :
						self.game.state=GameState.VIEWING;
						self.game.menu.NewMenuState();
					self.game.camera.loadPosition(1);
				
	def SpecialKeyRelease(self, key, x, y):
		pass
		
