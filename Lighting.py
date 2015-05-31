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

class Lighting:
	'''
	
	'''
	def __init__(self,game):
		self.game = game
		self.LightingIndex=None
		
	def Init(self, env_light, table_lamps, green_lamp,reflections):
		'''

		'''
		if not self.LightingIndex:
			self.LightingIndex=glGenLists(2)      # Display List erzeugen
		
		glNewList(self.LightingIndex,GL_COMPILE)
		#glNewList(self.LightingIndex,GL_COMPILE_AND_EXECUTE)

		glEnable(GL_LIGHTING)

		if (env_light) :
			ambient_light =[.15,.15,.15,1.0]
			glLightModelfv(GL_LIGHT_MODEL_AMBIENT,ambient_light)
		

		Helligkeit=1.0/table_lamps;

		glDisable(GL_LIGHT0)
		glDisable(GL_LIGHT1)
		glDisable(GL_LIGHT2)
		glDisable(GL_LIGHT3)

		if (table_lamps>=2) :
			#LampeMitte:  
			light_position1=[63.5,0.0,100.0,1.0]
			white_light1=[Helligkeit,Helligkeit,Helligkeit,1]
			glLightfv(GL_LIGHT1,GL_POSITION, light_position1)
			glLightfv(GL_LIGHT1,GL_DIFFUSE,white_light1)
			glLightfv(GL_LIGHT1,GL_SPECULAR,white_light1)
			glEnable(GL_LIGHT1)
		

		if (table_lamps==1 or table_lamps==3) :
			#LampeRechts:
			light_position0=[0.0,0.0,100.0,1.0] 
			white_light0=[Helligkeit,Helligkeit,Helligkeit,1]
			glLightfv(GL_LIGHT0,GL_POSITION, light_position0)
			glLightfv(GL_LIGHT0,GL_DIFFUSE, white_light0)
			glLightfv(GL_LIGHT0,GL_SPECULAR, white_light0)
			glEnable(GL_LIGHT0)
		

		if (table_lamps>=2) :
			#LampeLinks:
			light_position2=[-63.5,0.0,100.0,1.0]
			white_light2= [Helligkeit,Helligkeit,Helligkeit,1]
			glLightfv(GL_LIGHT2,GL_POSITION, light_position2)
			glLightfv(GL_LIGHT2,GL_DIFFUSE, white_light2)
			glLightfv(GL_LIGHT2,GL_SPECULAR, white_light2)
			glEnable(GL_LIGHT2)
		

		if (green_lamp) :
			#LampeUnten:
			light_position3=[0,0,-1,0]
			white_light3=[0.05, 0.225, 0.1, 1]
			specular=[0,0,0,1]
			glLightfv(GL_LIGHT3,GL_POSITION, light_position3)
			glLightfv(GL_LIGHT3,GL_DIFFUSE, white_light3)
			glLightfv(GL_LIGHT3,GL_SPECULAR, specular)
			glEnable(GL_LIGHT3)
		

		glEndList()

		if (reflections): 
			glLightModelf(33272, 33274)

	def draw(self) :
		glCallList(self.LightingIndex)


