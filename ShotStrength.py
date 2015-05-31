#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#=============================================================================
#   FileName: ShotStrength.py
#     Author: zzy
#      Email: zzy@gmail.com
#   HomePage: http://zzy.google.com
# LastChange: 2013-02-18 14:04:15
#=============================================================================
'''

from Param import *

try:
	from OpenGL.GL import *
	from OpenGL.GLU import *
	from OpenGL.GLUT import *
except:
	print ('Error! need PyOpenGL')
	raise SystemExit

class ShotStrength:
	def __init__(self, game):
		self.game = game
		self.shotStrength = 0.0

	def draw(self):
		if self.shotStrength>0.0:
			glPushMatrix();
			glBegin(GL_QUADS);
			glColor4f(1.0, 1.0, 1.0, 0.2-0.2/self.shotStrength);
			glVertex2f(14.0, 2.0);
			glVertex2f(15.0, 2.0);
			glColor4f(1.0, 1.0, 1.0, .7*self.shotStrength/45.0);
			glVertex2f(15.0, 2.0+self.shotStrength*0.2666);
			glVertex2f(14.0, 2.0+self.shotStrength*0.2666);
			glColor4f(1.0,1.0,1.0,0.1-0.1/self.shotStrength);
			glVertex2f(15.0, 10.0);
			glVertex2f(14.0, 10.0);
			glColor4f(1.0,1.0,1.0,.1*self.shotStrength/45.0);
			glVertex2f(14.0,2.0+self.shotStrength*0.2666);
			glVertex2f(15.0,2.0+self.shotStrength*0.2666);
			glEnd();
			glPopMatrix();

	def Init(self) :
		pass

	def setShockStrength(self, newShockStrength) :
		self.shotStrength=newShockStrength;


if __name__ == '__main__':
	pass


