#!/usr/bin/env python


from math import *
from BallTable import *
from Ball import *
from Param import *
from CreateTexture import *

try:
    from OpenGL.GL import *
    from OpenGL.GLU import *
    from OpenGL.GLUT import *
except:
    print ('Error! need PyOpenGL')
    raise SystemExit

class LoadingScreen:
    """

    """
    def __init__(self,game):
    	self.game = game
    	self.load_progress = -1
    	self.Ball13Texture = 0
    	self.LogoTexture = 0
    
    def Init(self):
    	#print "LoadingScreen init"
    	glEnable(GL_BLEND)
    	glDisable(GL_LIGHTING)
    	glClear(GL_COLOR_BUFFER_BIT)
    
    	self.Ball13Texture = glGenTextures(1)
    	glBindTexture(GL_TEXTURE_2D, self.Ball13Texture)   
    	CreateTexture("images/1/dreizehn.bmp")
        
        self.LogoTexture=glGenTextures(1)
    	glBindTexture(GL_TEXTURE_2D, self.LogoTexture)  
    	CreateTextureAlpha("images/1/logo.bmp")
    
    def Idle(self):
    	'''
    	'''
    	self.load_progress += 1
    
    	#print "load_progress:"+str(self.load_progress)
    
    	if self.load_progress == 0:
    	    self.Init()
    	elif self.load_progress == 1:
    	    initBallMatrixs(ParamDef.BallResolution)
    	elif self.load_progress == 2:
    	    self.game.balls[0].Init(0,ParamDef.TextureSize,ParamDef.BallResolution,ParamDef.Shadow)
    	elif self.load_progress == 3:
    	    self.game.balls[1].Init(1,ParamDef.TextureSize,ParamDef.BallResolution,ParamDef.Shadow)
    	elif self.load_progress == 4:
    	    self.game.balls[2].Init(2,ParamDef.TextureSize,ParamDef.BallResolution,ParamDef.Shadow)
    	elif self.load_progress == 5:
    	    self.game.balls[3].Init(3,ParamDef.TextureSize,ParamDef.BallResolution,ParamDef.Shadow)
    	elif self.load_progress == 6:
    	    self.game.balls[4].Init(4,ParamDef.TextureSize,ParamDef.BallResolution,ParamDef.Shadow)
    	elif self.load_progress == 7:
    	    self.game.balls[5].Init(5,ParamDef.TextureSize,ParamDef.BallResolution,ParamDef.Shadow)
    	elif self.load_progress == 8:
    	    self.game.balls[6].Init(6,ParamDef.TextureSize,ParamDef.BallResolution,ParamDef.Shadow)
    	elif self.load_progress == 9:
    	    self.game.balls[7].Init(7,ParamDef.TextureSize,ParamDef.BallResolution,ParamDef.Shadow)
    	elif self.load_progress == 10:
    	    self.game.balls[8].Init(8,ParamDef.TextureSize,ParamDef.BallResolution,ParamDef.Shadow)
    	elif self.load_progress == 11:
    	    self.game.balls[9].Init(9,ParamDef.TextureSize,ParamDef.BallResolution,ParamDef.Shadow)
    	elif self.load_progress == 12:
    	    self.game.balls[10].Init(10,ParamDef.TextureSize,ParamDef.BallResolution,ParamDef.Shadow)
    	elif self.load_progress == 13:
    	    self.game.balls[11].Init(11,ParamDef.TextureSize,ParamDef.BallResolution,ParamDef.Shadow)
    	elif self.load_progress == 14:
    	    self.game.balls[12].Init(12,ParamDef.TextureSize,ParamDef.BallResolution,ParamDef.Shadow)
    	elif self.load_progress == 15:
    	    self.game.balls[13].Init(13,ParamDef.TextureSize,ParamDef.BallResolution,ParamDef.Shadow)
    	elif self.load_progress == 16:
    	    self.game.balls[14].Init(14,ParamDef.TextureSize,ParamDef.BallResolution,ParamDef.Shadow)
    	elif self.load_progress == 17:
    	    self.game.balls[15].Init(15,ParamDef.TextureSize,ParamDef.BallResolution,ParamDef.Shadow)
    	elif self.load_progress == 18:
    	    self.game.balltable.Init(ParamDef.TableTextureSize)
    	elif self.load_progress == 19:
    	    self.game.lighting.Init(ParamDef.AmbientLighting,ParamDef.TableLamps,ParamDef.GrueneLamp,ParamDef.Reflections)
    	elif self.load_progress == 20:
    	    self.game.shotStrength.Init()
    	elif self.load_progress == 21:
    	    self.game.menu.Init(ParamDef.DisplayTextureSize)
    	elif self.load_progress == 22:
    	    self.game.menu.LoadLanguage(900)
    	elif self.load_progress == 23:
    	    self.game.menu.LoadLanguage(901)
    	elif self.load_progress == 24:
    	    self.game.menu.LoadLanguage(902)
    	elif self.load_progress == 25:
    	    self.game.menu.Init(ParamDef.DisplayTextureSize)
    	elif self.load_progress == 26:
    	    ''''''
    	    #self.game.BallsLayout()
    	elif self.load_progress == 27:
    	    ''''''
    	    #self.game.Decision.NewGame(gameType)
    	elif self.load_progress == 28:
    	#   glDeleteTextures(self.Ball13Texture)
    	    self.game.Run()
    	    print "load done!"
    
    	glutPostWindowRedisplay(self.game.currentWindow)
    
    def UpdateGL(self):
    	'''
    
    	'''
    	#print "UpdateGL!"
    	glEnable(GL_BLEND)
    	glDisable(GL_LIGHTING)
    
    	glMatrixMode(GL_PROJECTION)
    	glLoadIdentity()
    	gluOrtho2D(-4,4,-3,3)
    	glMatrixMode(GL_MODELVIEW)
    	glLoadIdentity()
    
    	glClear(GL_COLOR_BUFFER_BIT)
    
    	# No.13 ball
    	glBindTexture(GL_TEXTURE_2D, self.Ball13Texture)
    	glEnable(GL_TEXTURE_2D)
    	glColor4f(1.0, 1.0, 1.0, 1.0)
    	glBegin(GL_QUADS)
    	glTexCoord2f(0,0); glVertex2f(-1, -1-0.5)
    	glTexCoord2f(1,0); glVertex2f( 1, -1-0.5)
    	glTexCoord2f(1,1); glVertex2f( 1,  1-0.5)
    	glTexCoord2f(0,1); glVertex2f(-1,  1-0.5)
    	glEnd()
    	glDisable(GL_TEXTURE_2D)
    
    	# fan
    	angle =(1-(self.load_progress/29.0))*2*pi
    	radius = 2.0
    	glColor4f(0.0, 0.0, 0.0, 0.2)
    	glBegin(GL_TRIANGLE_FAN)
    	glVertex2f( 0.0, 0.0-0.5)
    	glVertex2f(-1*radius*sin(1.00*angle), radius*cos(1.00*angle)-0.5)
    	glVertex2f(-1*radius*sin(0.75*angle), radius*cos(0.75*angle)-0.5)
    	glVertex2f(-1*radius*sin(0.50*angle), radius*cos(0.50*angle)-0.5)
    	glVertex2f(-1*radius*sin(0.25*angle), radius*cos(0.25*angle)-0.5)
    	glVertex2f( 0.0, radius-0.5)
    	glEnd()
    
    	# logo
    	glBindTexture(GL_TEXTURE_2D, self.LogoTexture)
    	glEnable(GL_TEXTURE_2D)
    	glColor4f(1.0, 1.0, 1.0, 0.7)
    	glBegin(GL_QUADS)
    	glTexCoord2f(0,0);	glVertex2f(-2,0)
    	glTexCoord2f(1,0);	glVertex2f( 2,0)
    	glTexCoord2f(1,1);	glVertex2f( 2,1)
    	glTexCoord2f(0,1);	glVertex2f(-2,1)
    	glEnd()
    	glDisable(GL_TEXTURE_2D);
    
    	glutSwapBuffers()
    
