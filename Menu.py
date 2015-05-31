#!/usr/bin/env python
# -*-  coding: UTF-8 -*-

from Param import *
from TextItem import *
from Scale import *

try:
	from OpenGL.GL import *
	from OpenGL.GLU import *
	from OpenGL.GLUT import *
except:
	print ('Error! need PyOpenGL')
	raise SystemExit

class Menu:
	'''
	
	'''

	def __init__(self, game):
		self.game = game

		self.AnimationsTime = 0
		self.InAnimation = 0

		self.MenuState = 0
		self.AusSpiel = 0

		# Scale
		self.MenuBackground = None
		self.logo = None;
		self.name = None;
		self.halbe = None;
		self.volle = None
		self.ball = [None]*16
		self.GameStar = None;
		self.SchildArray = [None]*300;
		
		self.TextitemArray = [None]*1000;
		self.dummyTextfeld = TextItem(self.game);

		self.TDL = 0
		self.TTA = 0

		self.SchildAnzahl = 0
		self.TextfeldAnzahl = 0

		self.E_BallTextureSize = 0
		self.E_AnzeigeTexturgroesse = 0
		self.E_TableTextureSize = 0
		self.E_BallGeometry = 0
		self.E_MouseSpeed = .0
		self.E_InvertX = 0
		self.E_InvertY = 0
		self.MenuGesperrt = 0
		self.E_Reflections = 0
		self.E_ColorDepth = 0
		self.E_ScreenResolutions = 0
		self.Quality = 0
		self.E_Shadows = 0

		self.E_AmbientesLicht = 0
		self.E_TableLampes = 0
		self.E_GreenLampe = 0
		self.E_ShowFPS = 0

		self.E_TexMMM = 0
		
	
	def Init(self, display_texture_size):
		if self.TDL != 0:
			self.TDL=dummyTextfeld.dummyInitialisiere(display_texture_size)
		        return
		        
		self.LoadLanguage(900)
		self.LoadLanguage(901)
		self.LoadLanguage(902)

		if ParamDef.Language != 0:
			self.LoadLanguage(ParamDef.Language)

		for tf in range(640, 700):
			if not self.TextitemArray[tf]:
				continue
			self.TextitemArray[tf].SetMaxStrBuf(31.2)
			
		
	def MouseClick(self, btn, state, x, y):
		Signal = 0
		SchildNr = 0
		TextfeldNr = 0

		self.StartAnimation()

		#while (Signal != 0 and SchildNr < self):
			#Signal = 

	def StartAnimation(self):
		self.AnimationsTime = 0
		self.InAnimation = 1
	
	def LoadLanguage(self, id):
		
		pass

	def draw(self):
		pass

	def Update(self, factor):
		pass

	def NewMenuState(self):
		
		pass

	def SetFPS(self, fps):
		pass
