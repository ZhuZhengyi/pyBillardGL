#!/usr/bin/env python
# -*-  coding: UTF-8 -*-

import numpy
from math import *
from Param import *
from CreateTexture import *
from decimal import *

try:
	from OpenGL.GL import *
	from OpenGL.GLU import *
	from OpenGL.GLUT import *
except:
	print ('Error! need PyOpenGL')
	raise SystemExit



BALL_CNT = 30
ball_vertices = [[]]*BALL_CNT	#ball vertexs
ball_indices = [[]]*BALL_CNT	#ball index
ball_texcoord = [[]]*BALL_CNT	#ball texture coord

def ShadowCircle(Unterteilungen, Innenradius, Aussenradius, InnenAlpha,AussenAlpha ):
	'''
	'''
	vertices = [0.0] *(3*2*Unterteilungen)
	colors   = [0.0]*(4*2*Unterteilungen)
	indices = [0]*(4*(3*(Unterteilungen/2)-1))

	iv=0
	ic=0
	ii=0
	for i in range(0, Unterteilungen+1):
		vertices[iv:iv+3]=[
				Aussenradius*cos(2*i*M_PI/Unterteilungen),
				Aussenradius*sin(2*i*M_PI/Unterteilungen),
				0]
		iv+=3
		colors[ic:ic+4]=[1.0,1.0,1.0,AussenAlpha];
		ic+=4
		vertices[iv:iv+3]=[
				Innenradius*cos(2*i*M_PI/Unterteilungen),
				Innenradius*sin(2*i*M_PI/Unterteilungen),
				0]
		iv+=3
		colors[ic:ic+4]=[1.0,1.0,1.0,InnenAlpha];
		ic+=4

	for j in range(0, Unterteilungen):
		indices[ii:ii+4]=[2*j,2*j+2,2*j+3,2*j+1 ];
		ii+=4

	indices[ii:ii+4]=[2*Unterteilungen-1,0,1,2*Unterteilungen-1]
	ii+=4

	for k in range(0, (Unterteilungen/4)):
		indices[ii:ii+4]=[
				2*k+1,
				2*k+3,
				2*((Unterteilungen/2)-k)-1,
				2*((Unterteilungen/2)-k)+1]
		ii+=4

	for l in range(Unterteilungen/2,3*Unterteilungen/4):
		indices[ii:ii+4]=[
				2*l+1,
				2*l+3,
				2*((3*Unterteilungen/2)-l)-1,
				1 if l==Unterteilungen/2 else 2*((3*Unterteilungen/2)-l)+1
				]
		ii+=4


	glEnableClientState(GL_VERTEX_ARRAY);
	glEnableClientState(GL_COLOR_ARRAY);
	glVertexPointer(3, GL_FLOAT, 0, vertices);
	glColorPointer(4, GL_FLOAT, 0, colors);

	glDisable(GL_LIGHTING);
	glBlendFunc(GL_ZERO,GL_ONE_MINUS_SRC_ALPHA);

	#glDrawElements(GL_QUADS,4*(3*(Unterteilungen/2)-1), GL_UNSIGNED_INT,indices);
	glBlendFunc(GL_SRC_ALPHA,GL_ONE_MINUS_SRC_ALPHA);
	glEnable(GL_LIGHTING);

	glDisableClientState(GL_COLOR_ARRAY);
	glDisableClientState(GL_VERTEX_ARRAY);

def calc_ind2(b, c, resolution):
	return ((c*(2*resolution+3-c))/2)+b

def Triangle(ax,ay,az,
		bx,by,bz,
		cx,cy,cz,
		resolution,iv,ii,it,
		m_vertices, m_indices, m_texcoord) :
	'''
	get ball triangles
	'''
	orient = 99.0
	ivstart = iv/3

	vertices = m_vertices[resolution]
	indices = m_indices[resolution]
	texcoord = m_texcoord[resolution]

	#vertices, texcoord
	#print "-----------"
	#print "resolution:",resolution
	for c in range(resolution+1):
		for b in range(resolution-c+1) :
			nb=float(b)/float(resolution)
			nc=float(c)/float(resolution)
			temp_x=ax+nb*(bx-ax)+nc*(cx-ax)
			temp_y=ay+nb*(by-ay)+nc*(cy-ay)
			temp_z=az+nb*(bz-az)+nc*(cz-az)
			Abstand=sqrt(temp_x*temp_x+temp_y*temp_y+temp_z*temp_z)
			temp_x=temp_x/Abstand
			temp_y=temp_y/Abstand
			temp_z=temp_z/Abstand
			vertices[iv:iv+3]= [temp_x,temp_y,temp_z]
			iv+=3

			angle = 0.0 # angle
			if  temp_y!=0.0 :
				angle=atan(temp_x/temp_y)/M_PI

#			if resolution == 3:
#				print orient,angle,temp_x,temp_y,temp_z

			if isFloatEqual(temp_x,0.0) and isFloatEqual(temp_y, 0.0) :
				angle=orient
			#if not angle :
			#	angle=.0
			if temp_y<0:
				angle+=1
			elif temp_x<0 :
				angle+=2
			if not isFloatEqual(orient, 99.0):
				while (angle<orient-0.5):
					angle+=1
				while (angle>orient+0.5) :
					angle-=1

			orient=angle

			texcoord[it:it+2]=[angle,acos(temp_z)/M_PI-1]
			it+=2

	#indices
	for c in range(resolution):
		for b in range(resolution-c):
			if c!=0 :
				indices[ii:ii+3]=[
						ivstart+calc_ind2(b,c,resolution),
						ivstart+calc_ind2(b+1,c-1,resolution),
						ivstart+calc_ind2(b+1,c,resolution)
						]
				ii+=3

			indices[ii:ii+3]=[
					ivstart+calc_ind2(b,c,resolution),
					ivstart+calc_ind2(b+1,c,resolution),
					ivstart+calc_ind2(b,c+1,resolution)
					]
			ii+=3

	return iv,ii,it

def isFloatEqual(a,b):
	precision = 0.000001
	if abs(a-b) < precision :
		return True
	return False

quadratic=None

def initBallMatrixs(resolution):
	'''

	'''
	#print "resolution:",resolution
	global quadratic

	quadratic = gluNewQuadric();
	gluQuadricNormals(quadratic, GLU_SMOOTH);#
	gluQuadricTexture(quadratic, GL_TRUE);

	if resolution<1:
		resolution=1
	if resolution>29:
		resolution=29

	a=sqrt(0.8);       # 0.8944271
	b=sqrt(0.2);       # 0.4472136
	c=a*sin(0.4*M_PI); # 0.8506508
	d=a*cos(0.4*M_PI); # 0.2763932
	e=a*sin(0.8*M_PI); # 0.5257311
	f=a*cos(0.8*M_PI); # 0.7236068

	triangle_points = [
			[[a,0,b],[d,c,b],[0,0,1]],
			[[d,c,b],[f,e,b],[0,0,1]],
			[[f,e,b],[f,-e,b],[0,0,1]],
			[[f,-e,b],[d,-c,b],[0,0,1]],
			[[d,-c,b],[a,0,b],[0,0,1]],
			[[-f,-e,-b],[-f,e,-b],[a,0,b]],
			[[a,0,b],[-f,e,-b],[d,c,b]],
			[[-f,e,-b],[-d,c,-b],[d,c,b]],
			[[d,c,b],[-d,c,-b],[f,e,b]],
			[[-d,c,-b],[-a,0,-b],[f,e,b]],
			[[f,e,b],[-a,0,-b],[f,-e,b]],
			[[-a,0,-b],[-d,-c,-b],[f,-e,b]],
			[[f,-e,b],[-d,-c,-b],[d,-c,b]],
			[[-d,-c,-b],[-f,-e,-b],[d,-c,b]],
			[[d,-c,b],[-f,-e,-b],[a,0,b]],
			[[-f,e,-b],[0,0,-1],[-d,c,-b]],
			[[-d,c,-b],[0,0,-1],[-a,0,-b]],
			[[-a,0,-b],[0,0,-1],[-d,-c,-b]],
			[[-d,-c,-b],[0,0,-1],[-f,-e,-b]],
			[[-f,-e,-b],[0,0,-1],[-f,e,-b]]
	]

	for A in range(1, resolution+1):
		#print A, ball_vertices[A]
		if ( (ball_vertices[A]==[]) and (A%2) ) :
			ball_vertices[A] = [0.0]*(20*3*(A+1)*(A+2)/2)
			ball_texcoord[A] = [0.0]*(20*(A+1)*(A+2))
			ball_indices[A] = [0]*(20*3*A*A)

			iv,ii,it = 0,0,0
			for points in triangle_points :
				iv,ii,it = Triangle(points[0][0],points[0][1],points[0][2],
						points[1][0],points[1][1],points[1][2],
						points[2][0],points[2][1],points[2][2],
						A,iv,ii,it,
						ball_vertices,ball_indices,ball_texcoord
						)
				#print iv,ii,it

			#if A == 3 :
				#print "ball_vertices: ",A," ",ball_vertices[A]
				#print "ball_indices: ",A," ",ball_indices[A]
				#print "ball_texcoord: ",A," ",ball_texcoord[A]

			#gespart=0
			for test in range(ii) :
				for vergleich in range(test) :
					vi2=3*ball_indices[A][test]
					ii2=3*ball_indices[A][vergleich]
					if ( isFloatEqual(ball_vertices[A][vi2+0],ball_vertices[A][ii2+0])
					and isFloatEqual(ball_vertices[A][vi2+1],ball_vertices[A][ii2+1])
					and isFloatEqual(ball_vertices[A][vi2+2],ball_vertices[A][ii2+2]) ):
						ti2=2*ball_indices[A][test]
						tv2=2*ball_indices[A][vergleich]
						if (isFloatEqual(ball_texcoord[A][ti2+0],ball_texcoord[A][tv2+0])
						and isFloatEqual(ball_texcoord[A][ti2+1],ball_texcoord[A][tv2+1])):
							ball_indices[A][test]=ball_indices[A][vergleich]
							#gespart+=1
							#print str(ball_indices[A][vergleich])+","
							break


	#print ball_vertices
	#print ball_indices
	#print ball_texcoord

def exp2(a):
	return 1<<a

class Ball:
	'''

	'''

	def __init__(self, game):
		self.game = game
		self.Position = [0,0,0]
		self.Number = -1
		self.shadowIndex = 0
		self.shadowIndexStatic = 0
		self.shadow2Index = 0
		self.Shadow = 0
		self.InAnimation = 0
		self.ballIndex = [0]*BALL_CNT       	#
		self.ballIndexStatic = [0]*BALL_CNT 	#
		self.StaticExists = [0]*BALL_CNT    	#
		self.StaticExistShadow = 0
		self.RotateMatrix = [.0]*16
		self.OldTextureSize = 1
		self.Textures = [0]*9
		self.Shadow1_x = 0
		self.Shadow1_y=0
		self.Shadow1_scale=0
		self.Shadow1_angle=0
		self.Shadow2_x = 0
		self.Shadow2_y=0
		self.Shadow2_scale=0
		self.Shadow2_angle=0
		self.Shadow3_x = 0
		self.Shadow3_y=0
		self.Shadow3_scale=0
		self.Shadow3_angle=0

	def Init(self, Nr, TextureSize, Maxresol_size, shadow):
		'''

		'''
		global quadratic

		self.Shadow = shadow

		if self.ballIndex[3] == 0 :
			self.Position[0:2]=[3000.0,3000.0]
			glPushMatrix()
			glLoadIdentity()
			self.RotateMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
			glPopMatrix()

		self.Number = Nr

		for resol_size in range(3,Maxresol_size+1,2):
			if ((self.ballIndex[resol_size] == 0)
					or(self.OldTextureSize!=TextureSize)) :
				self.ballIndex[resol_size]=glGenLists(1)
				self.ballIndexStatic[resol_size]=glGenLists(1)

				if (TextureSize==0)or(self.Number==0):
					mat_diffuse=[1.0, 1.0, 1.0, 1.0]
					mat_specular=[0.5, 0.5, 0.5, 1.0]
					mat_shininess = 80.0
					#glNewList(self.ballIndex[resol_size], GL_COMPILE_AND_EXECUTE)
					glNewList(self.ballIndex[resol_size], GL_COMPILE)
					glMaterialfv(GL_FRONT, GL_AMBIENT,mat_diffuse)
					glMaterialfv(GL_FRONT, GL_DIFFUSE,mat_diffuse)
					glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
					glMaterialf(GL_FRONT, GL_SHININESS, mat_shininess)

					gluSphere(quadratic,1.0,32,32)

					'''
					glEnableClientState(GL_VERTEX_ARRAY)
					glEnableClientState(GL_NORMAL_ARRAY)
					glNormalPointer(GL_FLOAT, 0, ball_vertices[resol_size])
					glVertexPointer(3, GL_FLOAT, 0, ball_vertices[resol_size])
					glDrawElements(GL_TRIANGLES,len(ball_indices[resol_size]),
							GL_UNSIGNED_INT,ball_indices[resol_size])
					glDisableClientState(GL_NORMAL_ARRAY)
					glDisableClientState(GL_VERTEX_ARRAY)
					'''

					glEndList()
				else :
					TG=exp2((7-resol_size)/2);
					if (TG<TextureSize):
						TG=TextureSize
					if (TG>8):
						TG=1

					if self.Textures[TG] == 0:
						self.Textures[TG] = glGenTextures(1)
					glBindTexture(GL_TEXTURE_2D, self.Textures[TG]);
					Name="images/"+str(TG)+"/"+str(Nr)+".bmp"
					CreateTexture(Name)

					'''
					texcoord = []
					if (w!=h) :
						Aspekt=(w+1.0)/(h+1.0)
						texcoord = [.0] *(20*(resol_size+1)*(resol_size+2))
						for a in range(0,(20*(resol_size+1)*(resol_size+2)),2):
							texcoord[a]=ball_texcoord[resol_size][a]/Aspekt
							texcoord[a+1]=ball_texcoord[resol_size][a+1];
					'''

					glNewList(self.ballIndex[resol_size],GL_COMPILE_AND_EXECUTE);
					mat_diffuse = [1.0, 1.0, 1.0, 1.0]
					mat_specular = [0.5, 0.5, 0.5, 1.0]
					mat_shininess = 80.0
					glMaterialfv(GL_FRONT, GL_AMBIENT,mat_diffuse);
					glMaterialfv(GL_FRONT, GL_DIFFUSE,mat_diffuse);
					glMaterialfv(GL_FRONT, GL_SPECULAR,mat_specular);
					glMaterialf(GL_FRONT, GL_SHININESS,mat_shininess);
					glBindTexture(GL_TEXTURE_2D,self.Textures[TG])
					glEnable(GL_TEXTURE_2D)
					glTexEnvf(GL_TEXTURE_ENV,GL_TEXTURE_ENV_MODE,GL_MODULATE)

					gluSphere(quadratic,1.0,32,32)

					'''
					glEnableClientState(GL_VERTEX_ARRAY)
					glEnableClientState(GL_NORMAL_ARRAY)
					glEnableClientState(GL_TEXTURE_COORD_ARRAY)
					glNormalPointer(GL_FLOAT,0,ball_vertices[resol_size])
					glVertexPointer(3, GL_FLOAT,0,ball_vertices[resol_size])
					#if tex_r.nrh!=tex_r.nch:
					if w!=h:
						glTexCoordPointer(2, GL_FLOAT, 0, texcoord);
					else:
						glTexCoordPointer(2, GL_FLOAT, 0, ball_texcoord[resol_size]);

					glDrawElements(GL_TRIANGLES,20*3*resol_size*resol_size,
							GL_UNSIGNED_INT,ball_indices[resol_size])
					glDisableClientState(GL_TEXTURE_COORD_ARRAY)
					glDisableClientState(GL_NORMAL_ARRAY)
					glDisableClientState(GL_VERTEX_ARRAY)
					'''
					glDisable(GL_TEXTURE_2D)
					glEndList()

				self.StaticExists[resol_size]=0;
				self.StaticExistShadow=0;
				self.InAnimation=1;

		if self.shadowIndex==0:
			self.shadowIndex=glGenLists(1);
			self.shadowIndexStatic=glGenLists(1);

			glNewList(self.shadowIndex,GL_COMPILE_AND_EXECUTE);
			ShadowCircle(18, .7, 1.2, 0.2, 0.0);
			glEndList();

			self.Shadow=shadow
			self.Shadow1_x=0
			self.Shadow1_y=0
			self.Shadow1_scale=1
			self.Shadow1_angle=0
			self.Shadow2_x=0
			self.Shadow2_y=0
			self.Shadow2_scale=1
			self.Shadow2_angle=0
			self.Shadow3_x=0
			self.Shadow3_y=0
			self.Shadow3_scale=1
			self.Shadow3_angle=0

		if self.shadow2Index == 0:
			self.shadow2Index=glGenLists(1);
			glNewList(self.shadow2Index, GL_COMPILE_AND_EXECUTE);
			ShadowCircle(14, 0.1, 0.5, 0.5, 0.0);
			glEndList();

		self.OldTextureSize=TextureSize

	def draw(self, resol_size):
		'''
		'''
		if self.Position[0]!=3000:
			if self.InAnimation!=0:

				glPushMatrix();
				glScalef(2.8575,2.8575,2.8575)
				glTranslatef(self.Position[0], self.Position[1], self.Position[2]);
				glMultMatrixf(self.RotateMatrix);
				glCallList(self.ballIndex[resol_size]);
				glPopMatrix();
				self.InAnimation=0;
				for i in range(0,BALL_CNT):
					self.StaticExists[i]=0;
			elif self.StaticExists[resol_size]!=0:
				glCallList(self.ballIndexStatic[resol_size]);
			else:
				glNewList(self.ballIndexStatic[resol_size],GL_COMPILE_AND_EXECUTE)
				glPushMatrix();
				glScalef(2.8575,2.8575,2.8575)
				glTranslatef(self.Position[0],self.Position[1],self.Position[2])
				glMultMatrixf(self.RotateMatrix)
				glCallList(self.ballIndex[resol_size])
				glPopMatrix();
				glEndList();
				self.StaticExists[resol_size]=1;

	def drawShadow(self):
		if (self.Shadow and (self.Position[0]!=3000) and (self.Position[2]>=0)) :
			if (self.InAnimation) :
				glPushMatrix();

				glScalef(2.8575,2.8575,2.8575)
				glTranslatef(self.Position[0],self.Position[1],self.Position[2]-1);
				glCallList(self.shadow2Index);

				glPushMatrix();
				glTranslatef(self.Shadow1_x,self.Shadow1_y,0);
				glRotatef(self.Shadow1_angle,0,0,1);
				glScalef(self.Shadow1_scale,1,1);
				glCallList(self.shadowIndex);
				glPopMatrix();

				glPushMatrix();
				glTranslatef(self.Shadow2_x,self.Shadow2_y,0);
				glRotatef(self.Shadow2_angle,0,0,1);
				glScalef(self.Shadow2_scale,1,1);
				glCallList(self.shadowIndex);
				glPopMatrix();

				glPushMatrix();
				glTranslatef(self.Shadow3_x,self.Shadow3_y,0);
				glRotatef(self.Shadow3_angle,0,0,1);
				glScalef(self.Shadow3_scale,1,1);
				glCallList(self.shadowIndex);
				glPopMatrix();

				glPopMatrix();

				self.StaticExistShadow=0;

			elif (self.StaticExistShadow):
				glCallList(self.shadowIndexStatic);
			else :

				glNewList(self.shadowIndexStatic,GL_COMPILE_AND_EXECUTE);
				glPushMatrix();
				glScalef(2.8575,2.8575,2.8575)
				glTranslatef(self.Position[0],self.Position[1],self.Position[2]-1);

				glCallList(self.shadow2Index);

				glPushMatrix();
				glTranslatef(self.Shadow1_x,self.Shadow1_y,0);
				glRotatef(self.Shadow1_angle,0,0,1);
				glScalef(self.Shadow1_scale,1,1);
				glCallList(self.shadowIndex);
				glPopMatrix();

				glPushMatrix();
				glTranslatef(self.Shadow2_x,self.Shadow2_y,0);
				glRotatef(self.Shadow2_angle,0,0,1);
				glScalef(self.Shadow2_scale,1,1);
				glCallList(self.shadowIndex);
				glPopMatrix();

				glPushMatrix();
				glTranslatef(self.Shadow3_x,self.Shadow3_y,0);
				glRotatef(self.Shadow3_angle,0,0,1);
				glScalef(self.Shadow3_scale,1,1);
				glCallList(self.shadowIndex);
				glPopMatrix();
				glPopMatrix();
				glEndList();

				self.StaticExistShadow=1;

	def newPosition(self, newPos):
		dx=newPos[0]-self.Position[0]
		dy=newPos[1]-self.Position[1]

		if (dx!=0 or dy!=0) :
			glPushMatrix();
			glLoadIdentity();
			glRotatef(sqrt(dx*dx+dy*dy)*20.051016*2,-dy,dx,0.0);
			glMultMatrixf(self.RotateMatrix);
			glGetFloatv(GL_MODELVIEW_MATRIX,self.RotateMatrix);
			glPopMatrix();
			self.Position[0]=newPos[0];
			self.Position[1]=newPos[1];
			self.Position[2]=(0 if newPos[2]>0 else newPos[2])

			if (self.Shadow) :
				self.Shadow1_x=newPos[0]/34;
				self.Shadow1_x= (self.Shadow1_x if(self.Shadow1_x) else .0001);
				self.Shadow1_y=newPos[1]/34;
				self.Shadow1_scale=sqrt(self.Shadow1_x*self.Shadow1_x+self.Shadow1_y*self.Shadow1_y+1);
				self.Shadow1_angle=57.3*atan(self.Shadow1_y/self.Shadow1_x);

				self.Shadow2_x=(newPos[0]-22.22)/34;
				self.Shadow2_x= (self.Shadow2_x if (self.Shadow2_x) else .0001);
				self.Shadow2_y=self.Shadow1_y;
				self.Shadow2_scale=sqrt(self.Shadow2_x*self.Shadow2_x+self.Shadow2_y*self.Shadow2_y+1);
				self.Shadow2_angle=57.3*atan(self.Shadow2_y/self.Shadow2_x);

				self.Shadow3_x=(newPos[0]+22.22)/34;
				self.Shadow3_x= self.Shadow3_x if(self.Shadow3_x) else .0001;
				self.Shadow3_y=self.Shadow1_y;
				self.Shadow3_scale=sqrt(self.Shadow3_x*self.Shadow3_x+self.Shadow3_y*self.Shadow3_y+1);
				self.Shadow3_angle=57.3*atan(self.Shadow3_y/self.Shadow3_x);

		self.InAnimation=1;

	def disappear(self) :
		Pos =[3000.0, 3000.0, 0.0]
		self.newPosition(Pos)

	def Pos_x(self) :
		return self.Position[0]

	def Pos_y(self) :
		return self.Position[1];

	def Pos_xD(self) :
		return self.Position[0]*0.5;

	def Pos_yD(self) :
		return self.Position[1]*0.5;

	def Pos_xCM(self) :
		return self.Position[0]*2.8575;

	def Pos_yCM(self) :
		return self.Position[1]*2.8575;

	def Pos_zCM(self) :
		return self.Position[2]*2.8575;
