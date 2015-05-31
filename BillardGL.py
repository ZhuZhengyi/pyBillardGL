#!/usr/bin/env python
# -*- coding: utf8 -*-

'''
#=============================================================================
#   FileName: BillardGL.py
#     Author: zzy
#      Email: zzy@gmail.com
#   HomePage: http://zzy.google.com
# LastChange: 2012-12-25 16:48:58
#=============================================================================
'''

import sys
from math import *
import Image

from LoadingScreen import *
from Camera import *
from Ball import *
from BallTable import *
from Decision import *
from Lighting import *
from Menu import *
from MouseKey import *
from ShotStrength import *
from Param import *

try:
	from OpenGL.GL import *
	from OpenGL.GLU import *
	from OpenGL.GLUT import *
except:
	print ('Error! need PyOpenGL')
	raise SystemExit
	
def ElapsedTime(): 
		return glutGet(GLUT_ELAPSED_TIME)/10;

APP_NAME = "PyBillardGL"

class Game: 
	'''
	'''

	def __init__(self):
		self.loading = LoadingScreen(self)
		self.camera = Camera(self)
		self.lighting = Lighting(self)
		self.balltable = BallTable(self)
		self.menu = Menu(self)
		self.decision = Decision(self)
		self.mousekey = MouseKey(self)
		self.shotStrength = ShotStrength(self)
		self.state = GameState.START
		self.mode = GameMode.TUTORIAL
		self.balls = [ Ball(self) ]*16
		self.ballinHole = [ None ] * 16
		self.LastFrameTimePoint = 0
		
	def Load(self):
		glutInit(sys.argv)
		glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB|GLUT_DEPTH)
		glutInitWindowSize(ParamDef.ScreenResolution[0], ParamDef.ScreenResolution[1])
		glutInitWindowPosition(0,0)
		glutCreateWindow(APP_NAME)
		glClearColor(0,0,0,0)
		glutIdleFunc(self.loading.Idle)
		glutDisplayFunc(self.loading.UpdateGL)
		self.currentWindow = glutGetWindow()
		glutMainLoop()

	def Run(self):
		ParamDef.DelayCompensation=1
		glutIgnoreKeyRepeat(1)
		glEnable(GL_DEPTH_TEST)
		glEnable(GL_CULL_FACE)
		glEnable(GL_NORMALIZE)
		glEnable(GL_BLEND)
		glShadeModel(GL_SMOOTH)
		glHint(GL_POLYGON_SMOOTH_HINT, GL_NICEST)
		glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)

		glutMouseFunc(self.mousekey.MouseClick);
		glutMotionFunc(self.mousekey.MouseMove);
		glutKeyboardFunc(self.mousekey.KeyPress);
		glutKeyboardUpFunc(self.mousekey.KeyRelease);
		glutSpecialFunc(self.mousekey.SpecialKeyPress);
		glutSpecialUpFunc(self.mousekey.SpecialKeyRelease)

		glutVisibilityFunc(self.Visible)
		glutIdleFunc(self.timerEvent)
		glutDisplayFunc(self.updateGL)

	def timerEvent(self):
		#print "timerEvent"
		ParamDef.FrameTimePoint=glutGet(GLUT_ELAPSED_TIME)/10
		ParamDef.Factor=ParamDef.FrameTimePoint-self.LastFrameTimePoint;

		if (ParamDef.DelayCompensation !=0 ) :
			ParamDef.Factor=1;
			ParamDef.DelayCompensation=0;

		if (ParamDef.Factor !=0) :
			if (ParamDef.ShowFPS) :
				if ((ParamDef.FrameTimePoint%200)<(self.LastFrameTimePoint%200)) :
					self.menu.SetFPS(Frames/2);
					ParamDef.Frames=0;
				else:
					ParamDef.Frames+=1

			self.menu.Update(ParamDef.Factor);

			if self.state == GameState.START: 
				self.StartHandling()
			elif self.state == GameState.VIEWING: 
				self.ViewingHandling()
			elif self.state == GameState.AIMING: 
				self.AimHandling()
			elif self.state == GameState.SWING: 
				self.BackswingHandling()
			elif self.state == GameState.SHOT: 
				self.ShotHandling()
			elif self.state == GameState.NEW_WHITE: 
				self.NewWhiteHandling()
			elif self.state == GameState.JUDGEING: 
				self.JudgeHandling()

			self.camera.Ride(ParamDef.Factor);
			self.LastFrameTimePoint=ParamDef.FrameTimePoint;
			glutPostWindowRedisplay(self.currentWindow);

	def updateGL(self):
		'''
		'''
		#print "updateGL"
		if ParamDef.ZBufferDelete != 0:
			glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

		self.camera.draw()
		self.lighting.draw()
		self.balltable.drawSurface()

		glDisable(GL_DEPTH_TEST)
		self.balltable.drawLine()
		for ball in self.balls:
			ball.drawShadow()
		glEnable(GL_DEPTH_TEST)

		self.balltable.drawBorder()

		distance=0;   #distance
		resolution=1; #Display resolution
		for ball in self.balls:
			x=ball.Pos_xCM()-self.camera.Pos_x;
			y=ball.Pos_yCM()-self.camera.Pos_y;
			z=self.camera.Pos_z;
			distance=sqrt(x*x+y*y+z*z);
			resolution=(400/distance)
			if (resolution<3): 
				resolution=3;
			resolution=(resolution/2)*2+1;
			if (resolution>ParamDef.BallResolution):
				resolution=ParamDef.BallResolution;
			ball.draw(resolution);    

		glDisable(GL_DEPTH_TEST);
		glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
		glDisable(GL_LIGHTING);

		self.menu.draw();

		if (self.state != GameState.START) :
			self.shotStrength.draw();

		glEnable(GL_DEPTH_TEST);

		glutSwapBuffers()

	def Visible(self,visible):
		print "Visible"
		if(visible == GLUT_VISIBLE):
			glutIdleFunc(self.timerEvent)

	def StartHandling(self) :
		self.camera.ScenicFlight(ParamDef.Factor)
		self.menu.Update(ParamDef.Factor)

	def ViewingHandling(self) :
		self.menu.Update(ParamDef.Factor)

		if (KEY_UP) :
			self.camera.Move_Front(ParamDef.Factor);
		if (KEY_DOWN) :
			self.camera.Move_Back(ParamDef.Factor);
		if (KEY_RIGHT):
			self.camera.Move_Right(ParamDef.Factor);
		if (KEY_LEFT) :
			self.camera.Move_Left(ParamDef.Factor);
		if (KEY_SHIFT) :
			self.camera.Move_Up(ParamDef.Factor);
		if (KEY_CTRL) :
			self.camera.Move_Down(ParamDef.Factor);
		if (KEY_PAGE_UP) :
			self.camera.Move_In(ParamDef.Factor);
		if (KEY_PAGE_DOWN) :
			self.camera.Move_Out(ParamDef.Factor);
		if (KEY_HOME) :
			self.camera.Zoom_In(ParamDef.Factor);
		if (KEY_END) :
			self.camera.Zoom_Out(ParamDef.Factor);


	'''
	* Aim Handling
	'''
	def AimHandling(self) :
		if (KEY_UP)  :
			self.camera.Move_In(ParamDef.Factor)
		if (KEY_DOWN) :
			self.camera.Move_Out(ParamDef.Factor)
		if (KEY_RIGHT):
			self.camera.SwingRight(2*ParamDef.Factor,self.balls[0].Pos_xCM(),self.balls[0].Pos_yCM())
		if (KEY_LEFT) :
			self.camera.SwingLeft(2*ParamDef.Factor,self.balls[0].Pos_xCM(),self.balls[0].Pos_yCM())
		if (KEY_SHIFT) :
			self.camera.SwingDown(ParamDef.Factor,self.balls[0].Pos_xCM(),self.balls[0].Pos_yCM())
		if (KEY_CTRL)        :
			self.camera.SwingUp(ParamDef.Factor,self.balls[0].Pos_xCM(),self.balls[0].Pos_yCM())
		if (KEY_PAGE_UP)    :
			self.camera.Move_In(ParamDef.Factor)
		if (KEY_PAGE_DOWN)     :
			self.camera.Move_Out(ParamDef.Factor)
		if (KEY_HOME)        :
			self.camera.Vertigo_In(ParamDef.Factor)
		if (KEY_END) :
			self.camera.Vertigo_Out(ParamDef.Factor)


	def BackswingHandling(self) :
		'''
		'''
		if (KEY_UP)  :
			self.camera.Move_In(ParamDef.Factor);
		if (KEY_DOWN) :
			self.camera.Move_Out(ParamDef.Factor);
		if (KEY_RIGHT):
			self.camera.SwingRight(2*ParamDef.Factor,self.balls[0].Pos_xCM(),self.balls[0].Pos_yCM());
		if (KEY_LEFT) :
			self.camera.SwingLeft(2*ParamDef.Factor,self.balls[0].Pos_xCM(),self.balls[0].Pos_yCM());
		if (KEY_SHIFT) :
			self.camera.SwingDown(ParamDef.Factor,self.balls[0].Pos_xCM(),self.balls[0].Pos_yCM());
		if (KEY_CTRL) :
			self.camera.SwingUp(ParamDef.Factor,self.balls[0].Pos_xCM(),self.balls[0].Pos_yCM());
		if (KEY_PAGE_UP)  :
			self.camera.Move_In(ParamDef.Factor);
		if (KEY_PAGE_DOWN)  :
			self.camera.Move_Out(ParamDef.Factor);
		if (KEY_HOME) :
			self.camera.Zoom_In(ParamDef.Factor);
		if (KEY_END) :
			self.camera.Zoom_Out(ParamDef.Factor);

		shotStrength=MaxAusholStaerke*(1-exp((-ParamDef.FrameTimePoint+ParamDef.ShotStartTime)/400.0));
		self.ShotStrength.setShockStrength(shotStrength/3.333);

	'''
	 * 击球处理
	 *
	 '''
	def ShotHandling(self):
		FirstShot=0;
		#WeisseVersetzbar=0;

		if (KEY_UP)  :
			self.camera.Move_Front(ParamDef.Factor)
		if (KEY_DOWN) :
			self.camera.Move_Back(ParamDef.Factor)
		if (KEY_RIGHT):
			self.camera.Move_Right(ParamDef.Factor)
		if (KEY_LEFT) :
			self.camera.Move_Left(ParamDef.Factor)
		if (KEY_SHIFT):
			self.camera.Move_Up(ParamDef.Factor)
		if (KEY_CTRL):
			self.camera.Move_Down(ParamDef.Factor)
		if (KEY_PAGE_UP):
			self.camera.Move_In(ParamDef.Factor)
		if (KEY_PAGE_DOWN):
			self.camera.Move_Out(ParamDef.Factor)
		if (KEY_HOME) :
			self.camera.Zoom_In(ParamDef.Factor)
		if (KEY_END) :
			self.camera.Zoom_Out(ParamDef.Factor)

		#Frames++;                       # F"ur die Frames/sec-Anzeige

		# Zeit seit Stossbeginn
		time=ParamDef.FrameTimePoint-ParamDef.StartTime;  #time

		# Letzten Zustand noch zeichnen, wenn Stoss
		if (time>ParamDef.ShotTime):
			time=ParamDef.ShotTime # eigentlich schon vorbei

		#printf("%i-%i=%i: ",FrameZeitpunkt,Startzeit,Zeit);

		for i in range(16) : # Alle Kugeln neu positionieren
			if (LightingList[time][i][2]<=0) :
				self.balls[i].newPositionD(LightingList[Zeit][i]);


		self.ShotStrength.setShockStrength(shotStrength/3.333-Zeit/3.0);

		if (not (time & 31)) :
			neu=0;
			for i in range(16):
				if (self.ballsInGame[i] and self.ballsInHole[i]!=0
						and (self.balls[i].Pos_x()==3000)):
					self.ballsInHole[i]=1;
					neu=1;
			if (neu) :
				self.menu.NewMenuState()


		if (time==ParamDef.ShotTime and
				not( self.mode == GameMode.TUTORIAL 
					and ParamDef.FrameTimePoint-ParamDef.StartTime < 1900
					)
				):
			# Animation schon fertig?

			##ifndef _WIN32 
			#printf(" %f Frames/sec\n",(Frames*100.0)/(Stossdauer+1.0));
			##endif    

			for i in range(16)  :
				if (self.ballssInGame[i] 
					and not self.ballssInHole[i] 
					and (self.balls[i].Pos_x()==3000) ) :
					self.ballssInHole[i]=1;
			if (self.mode == GameMode.TRAINING or self.mode == GameMode.TUTORIAL ) :
				if (self.balls[0].Pos_x()==3000) :
					self.state=GameState.NEW_WHITE;
					ShotStrength.setShockStrength(0.0);
					ParamDef.LageVerbesserung=1;
					ParamDef.LageVerbesserungKopffeld=1;
					WhiteChosen();
					self.menu.NewMenuState();
				else :
					self.state=GameState.VIEWING;
					ShotStrength.setShockStrength(0.0);
					self.menu.NewMenuState();
			elif self.decision.Decisioning()==0 :
				self.state=GameState.JUDGEING
				ShotStrength.setShockStrength(0.0);
			else :
				self.state=GameState.VIEWING;
				self.shotStrength.setShockStrength(0.0);
				self.menu.NewMenuState();

	'''
	* 放置白球
	'''
	def NewWhiteHandling(self):
		if (self.mode == GameMode.TRAINING) :
			#ParamDef.
			LageVerbesserungKopffeld=0; #Location improving header
			LageVerbesserung=1;

		x=self.balls[0].Pos_xCM();
		y=self.balls[0].Pos_yCM();

		self.Factor2=sqrt((self.balls[0].Pos_xCM()-self.camera.Pos_xCM())*
				(self.balls[0].Pos_xCM()-self.camera.Pos_xCM())+
				(self.balls[0].Pos_yCM()-self.camera.Pos_yCM())*
				(self.balls[0].Pos_yCM()-self.camera.Pos_yCM())+
				self.camera.Pos_zCM()*self.camera.Pos_zCM());

		self.Factor2*=.005;

		if (KEY_UP) :
			x+=.3*Factor*Faktor2*sin(self.camera.Beta*M_PI/180.0);
			y+=.3*Factor*Faktor2*cos(self.camera.Beta*M_PI/180.0);
		if (KEY_DOWN) :
			x-=.3*Factor*Faktor2*sin(self.camera.Beta*M_PI/180.0);
			y-=.3*Factor*Faktor2*cos(self.camera.Beta*M_PI/180.0);
		if (KEY_LEFT) :
			x-=.3*Factor*Faktor2*cos(self.camera.Beta*M_PI/180.0);
			y+=.3*Factor*Faktor2*sin(self.camera.Beta*M_PI/180.0);
		if (KEY_RIGHT) :
			x+=.3*Factor*Faktor2*cos(self.camera.Beta*M_PI/180.0);
			y-=.3*Factor*Faktor2*sin(self.camera.Beta*M_PI/180.0);

		invalid=0;
		if (x<-124 or x>124 or (x>-63.5 and LageVerbesserungKopffeld)) :
			x=self.balls[0].Pos_xCM();

		if (y<-60.5 or y>60.5) :
			y=self.balls[0].Pos_yCM();

		for i in range(16) :
			if ((self.balls[i].Pos_xCM()-x)*(self.balls[i].Pos_xCM()-x)+
					(self.balls[i].Pos_yCM()-y)*(self.balls[i].Pos_yCM()-y)<32.7) :
				invalid=1;  #与其他球太近，无效

		#invalid
		if (not invalid) :
			self.self.balls[0].newPositionCM(x,y);
		if (KEY_SHIFT):
			self.camera.Move_Up(Factor)
		if (KEY_CTRL):
			self.camera.Move_Down(Factor)
		if (KEY_PAGE_UP):
			self.camera.Move_In(Factor)
		if (KEY_PAGE_DOWN):
			self.camera.Move_Out(Factor)
		if (KEY_HOME):
			self.camera.Zoom_In(Factor)
		if (KEY_END):
			self.camera.Zoom_Out(Factor)

	def JudgeHandling(self):
		if (ParamDef.JudgeDecision == -1) :
			ParamDef.JudgeDecision = Judge.Decisioning();
			ParamDef.RecodingChanges = ParamDef.JudgeDecision & 1;
			ParamDef.Foul = ParamDef.JudgeDecision & 2;
			ParamDef.LageVerbesserungKopffeld = ParamDef.JudgeDecision & 4;
			ParamDef.LageVerbesserung = ParamDef.JudgeDecision & 8;
			ParamDef.NeuAufbauenOderWeiterspielen = ParamDef.JudgeDecision & 16;
			ParamDef.NeuAufbauenOderAchtEinsetzen = ParamDef.JudgeDecision & 32;
			ParamDef.Player1Win = ParamDef.JudgeDecision & 64;
			ParamDef.Player2Win = ParamDef.JudgeDecision & 128;

			self.menu.NewMenuState();

if __name__ == "__main__":
	game = Game()
	game.Load()

