#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
#=============================================================================
#   FileName: TextItem.py
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

left_list = [
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0, 
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0, 
		0,	9, 11,	9,	9,	8,	8,	7,	8,	7,	7,	7,	6,	8,	9,	7, 
		9,	7,	8,	7,	7,	7,	8,	7,	7,	7,	9,	6,	8,	7,	7,	7, 
		9,	7,	9,	8,	9,	9,	9,	8,	8,	8,	7,	8,	8,	7,	8,	7, 
		9,	8,	9,	7,	6,	8,	6,	7,	7,	6,	6, 10,	7,	7,	9,	5, 
		5,	8,	9,	8,	8,	8,	6,	7,	8,	8,	8,	8,	8,	7,	8,	7, 
		9,	8,	9,	8,	7,	8,	7,	7,	7,	7,	7,	7,	9,	6,	8,	0, 
	
		0,	0,	0,	8,	7, 10,	8,	8,	3,	7,	0,	9,	7,	0,	0,	0, 
		0,	7,	8,	8,	7, 10,	7,	8,	3,	9,	0, 10,	7,	0,	0,	0, 
		0,	9, 11,	8, 10,	8, 10,	9,	4,	8,	7,	9,	7,	0,	7,	0, 
		0,	8,	8,	8,	7,	8,	8,	9,	7,	7,	7,	9,	8,	8,	8,	7, 
		8,	7,	8,	7,	7,	7,	7,	8,	8,	8,	8,	8,	4,	7,	3,	4, 
		6,	9,	8,	8,	8,	8,	8,	0,	7,	8,	8,	8,	8,	6,	8,	8, 
		8,	8,	8,	8,	8,	8,	8,	7,	7,	7,	7,	7,	4,	6,	3,	3, 
		9,	9,	8,	8,	8,	8,	8,	0,	7,	8,	8,	8,	8,	6,	8,	6
	]

right_list=[
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0, 
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0, 
		10, 15, 22, 28, 29, 33, 33, 15, 15, 14, 20, 29, 14, 21, 14, 23, 
		31, 17, 26, 26, 30, 26, 27, 25, 27, 27, 15, 14, 28, 28, 28, 25, 
		37, 32, 29, 30, 32, 24, 24, 34, 32, 14, 21, 30, 23, 39, 32, 34,
		29, 36, 29, 27, 25, 32, 30, 43, 30, 28, 27, 19, 23, 16, 27, 26, 
		15, 28, 29, 24, 28, 27, 20, 27, 27, 13, 13, 26, 13, 38, 26, 27, 
		28, 28, 20, 23, 19, 27, 25, 37, 26, 26, 24, 19, 12, 19, 28,  0, 
	
		0,	0,	0, 28, 25, 43, 28, 28, 18, 47,	0, 17, 43,	0,	0,	0, 
		0, 16, 16, 25, 25, 23, 26, 22, 18, 44,	0, 17, 42,	0,	0,	0, 
		0, 15, 28, 31, 29, 30, 13, 28, 17, 37, 20, 27, 29,	0, 36,	0, 
		0, 30, 20, 20, 17, 27, 29, 15, 15, 13, 20, 27, 42, 41, 42, 24, 
		32, 32, 32, 31, 31, 31, 40, 30, 24, 24, 24, 24, 15, 17, 18, 17, 
		32, 33, 35, 35, 34, 35, 35,  0, 35, 32, 32, 32, 32, 27, 28, 27, 
		28, 28, 28, 28, 28, 28, 43, 24, 27, 27, 27, 27, 14, 17, 18, 17, 
		28, 27, 28, 28, 28, 28, 28,  0, 28, 26, 26, 26, 26, 25, 28, 25
	]



class TextItem:
	'''
	
	'''
	A_EGAL  = 0      #
	A_LEFT = 1       #left
	A_MIDDLE =  2  #middle
	A_RIGHT = 3      #right
	
	HIDDEN =  0.0          #HIDDEN
	TRANSPARENT =   0.2    #
	APPEAR =  0.6          #appear
	SELECTED =   0.8      #ANGEWAEHLT selected
	VISIBLE =  1.0    #VISIBLE fullvisible

	ANIMATIONSDAUER = 100 #animation length
	
	def __init__(self, game):	
		self.game = game
		self.x=.0
		self.y=.0,
		self.Height=.0
		self.Aspect=.0
		self.Alpha=.0

		self.old_x=.0
		self.old_y=.0
		self.old_Height=.0
		self.vold_Alpha=.0

		self.soll_x=.0
		self.soll_y=.0
		self.soll_Height=.0
		self.soll_Alpha=.0

		self.MaxWidth = .0

		self.Alignment = 0
		self.InAnimation = 0
		self.Signal = 0
		self.nTime = 0
		self.DisplayListStart = 0
		
		self.TextfeldIndex = 0
		self.Horchen = 0
		self.nLines = 0

		self.TexturesStart = [.0] *512; #TexturenAnfang

	def dummyInitialisiere(self, TexGr):
		pass

	def Initialisiere(self, DLA):
		pass

	def Initialisiere(self, DLA, TextZ):
		pass

	def InitialisiereKDL(self, DLA, TextZ):
		pass

	def male(self):
		pass

	def PositioniereFix(self, X,Y,H,A):
		pass

	def Positioniere(self, X,Y,H,A):
		pass

	def SetText(self, text):
		pass

	def SetMaxStrBuf(self, mb):
		if (mb<0):
			mb=0
		self.MaxWidth=mb

	def TextboxHeight(self):
		return 0.7*self.nLines

	def GenerateDisplayList(self):
		if (self.TextfeldIndex != 0):
			self.TextfeldIndex=glGenLists(1);
	
	
