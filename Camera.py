#!/usr/bin/env python


from math import *
from Param import *

try:
	from OpenGL.GL import *
	from OpenGL.GLU import *
	from OpenGL.GLUT import *

except:
	print ('Error! need PyOpenGL')
	raise SystemExit

class Camera:
	'''

	'''

	def __init__(self,game):
		self.game = game
		self.positions = []
		self.Pos_x = 0
		self.Pos_y = 0
		self.Pos_z = 0
		self.Alpha = 0
		self.Beta = 0
		self.FOV = 0
		self.Aspect = 0
		self.Close = 0

		self.Aspect = 1.333333
		self.Persecution = -1
		self.Alpha = 100
		self.Beta = 0
		self.Pos_x = 0
		self.Pos_y = -200
		self.Pos_z = 200
		self.FOV = 38.6

		self.Target_Pos_x = 0.0
		self.Target_Pos_y = 0.0
		self.Target_Pos_z = 0.0
		self.Target_Alpha = 0.0
		self.Target_Beta = 0.0
		self.Target_FOV = 0.0

		self.Near = 0.0
		self.Remote = 0.0

		self.CameraNumber = 0

		self.initPositions()

	def initPositions(self):
		self.Alpha=60.0;
		self.Beta=60.0;
		self.Pos_x=-100.0;
		self.Pos_y=-50.0;
		self.Pos_z=50.0;
		self.FOV=38.6;
		self.savePosition(0);

		self.Alpha=0;
		self.Beta=0;
		self.Pos_x=0;
		self.Pos_y=0;
		self.Pos_z=400;
		self.FOV=30.7;
		self.savePosition(1);

		self.Alpha=80;
		self.Beta=90;
		self.Pos_x=-170;
		self.Pos_y=0;
		self.Pos_z=30;
		self.FOV=38.6;
		self.savePosition(2);

		self.Alpha=80
		self.Beta=-90;
		self.Pos_x=170;
		self.Pos_y=0;
		self.Pos_z=30;
		self.FOV=38.6;
		self.savePosition(3);

		self.Alpha=53;
		self.Beta=90;
		self.Pos_x=-220;
		self.Pos_y=0;
		self.Pos_z=120;
		self.FOV=38.6;
		self.savePosition(4);

		self.Alpha=53;
		self.Beta=-90;
		self.Pos_x=220;
		self.Pos_y=0;
		self.Pos_z=120;
		self.FOV=38.6;
		self.savePosition(5);

		self.Alpha=48;
		self.Beta=56.5;
		self.Pos_x=-229;
		self.Pos_y=-121;
		self.Pos_z=176;
		self.FOV=38.6;
		self.savePosition(6)

		self.Alpha=48
		self.Beta=123.5
		self.Pos_x=-229
		self.Pos_y=121
		self.Pos_z=176
		self.FOV=38.6
		self.savePosition(7)


	def savePosition(self,idx):
		self.positions.append( [self.Pos_x,self.Pos_y,self.Pos_z,self.Alpha,self.Beta,self.FOV])

  	def loadPosition(self,place):
		setToPosition(self.positions[place])
		self.Persecution = -1;

	def setToPosition( old_Pos) :
		self.Target_Pos_x = old_Pos[0];
		self.Target_Pos_y = old_Pos[1];
		self.Target_Pos_z = old_Pos[2];
		self.Target_Alpha = old_Pos[3];
		self.Target_Beta  = old_Pos[4];
		self.Target_FOV   = old_Pos[5];
		self.Beta=fmod(self.Beta,360);
		self.Target_Beta=fmod(self.Target_Beta,360);

		if self.Target_Beta>self.Beta+180 :
			self.Target_Beta-=360;

		if self.Target_Beta < self.Beta-180 :
			self.Target_Beta+=360;

		self.UpdateViewDepth();
		self.Persecution=-1;

	def draw(self):
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		gluPerspective(self.FOV, self.Aspect, self.Close, self.Remote)
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		glRotatef(self.Alpha,-1,0,0)
		glRotatef(self.Beta,0,0,1)
		glTranslatef(-self.Pos_x,-self.Pos_y,-self.Pos_z)

	def UpdateViewDepth(self) :
		ax=fabs(self.Pos_x)
		ay=fabs(self.Pos_y)
		az=self.Pos_z

		if ax<150 :
			if ay<80 :
		            self.Near=az-5;
			else:
		            self.Near=sqrt((ay-80)*(ay-80)+(az-5)*(az-5));
		else:
			if (ay<80) :
		            self.Near=sqrt((ax-150)*(ax-150)+(az-5)*(az-5));
			else:
		            self.Near=sqrt((ax-150)*(ax-150)+(ay-80)*(ay-80)+(az-5)*(az-5));

		self.Near*=.8;

		if self.Near<1:
			self.Near=1

		self.Remote=sqrt((ax+150)*(ax+150)+(ay+80)*(ay+80)+az*az);

	def ScenicFlight(self, frame):
		if self.Target_Pos_y == 0 :
			self.Target_Pos_y=0.00001
		self.Target_Beta+=0.1*frame;
		self.Target_Pos_x=(-30*sin(self.Target_Beta*M_PI/180)-280)*sin(self.Target_Beta*M_PI/180);
		self.Target_Pos_y=(-30*sin(self.Target_Beta*M_PI/180)-280)*cos(self.Target_Beta*M_PI/180);
		self.Target_Pos_z=100-50*sin(self.Target_Beta*M_PI/180);
		self.Target_FOV=36.8;
		self.Target_Alpha=atan(sqrt(self.Target_Pos_x*self.Target_Pos_x+self.Target_Pos_y*self.Target_Pos_y)/self.Target_Pos_z)*180/M_PI;

	def Ride(self, frame):
		pass

	def Move_Front(self, frame):
		pass

	def Move_Back(self, frame):
		pass

	def Move_Right(self, frame):
		pass

	def Move_Left(self, frame):
		pass

	def Move_Up(self, frame):
		pass

	def Move_Down(self, frame):
		pass

	def Move_In(self, frame):
		pass

	def Move_Out(self, frame):
		pass

	def Zoom_In(self, frame):
		pass

	def Zoom_Out(self, frame):
		pass

	def SwingLeft(self, frame, Mitte_x,  Mitte_y):
		pass

	def SwingRight(self, frame, Mitte_x,  Mitte_y):
		pass

	def SwingUp(self, frame, Mitte_x,  Mitte_y):
		pass

	def SwingDown(self, frame, Mitte_x,  Mitte_y):
		pass

	def Vertigo_In(self, frame):
		pass

	def Vertigo_Out(self, frame):
		pass
