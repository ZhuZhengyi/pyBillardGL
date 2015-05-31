#!/usr/bin/env python
# -*-  coding: UTF-8 -*-

from math import *
from CreateTexture import *
from Param import *

try:
	from OpenGL.GL import *
	from OpenGL.GLU import *
	from OpenGL.GLUT import *
except:
	print ('Error! need PyOpenGL')
	raise SystemExit

#Table surface
def TableSurface() :
	xteile=16;     # Anzahl muss gerade sein
	yteile=8;     # Anzahl muss gerade sein; 

	vertices = [0.0]*(3*(xteile+1)*(yteile+1));
	normals = [0.0]*(3*(xteile+1)*(yteile+1));
	indices = [0]*(4*xteile*yteile);

	glEnableClientState(GL_VERTEX_ARRAY);
	glEnableClientState(GL_NORMAL_ARRAY);

	widthx=264.0/xteile;
	widthy=137.0/yteile;

	iv=0
	for x in range(xteile+1):
		for y in range(yteile+1):
			vertices[iv:iv+3]=[-132+x*widthx,-68.5+y*widthy,0]
			normals[iv:iv+3]=[0,0,1]
			iv+=3

	ii=0;
	for xi in range(xteile):
		for yi in range(yteile):
			if (((yi==0)and((xi==0)or(xi==(xteile/2)-1)or(xi==xteile/2)or(xi==xteile-1)))or((yi==yteile-1)and((xi==0)or(xi==(xteile/2)-1)or(xi==xteile/2)or(xi==xteile-1)))):
				continue
						
			indices[ii:ii+4]=[(yteile+1)*xi+yi,(yteile+1)*(xi+1)+yi,(yteile+1)*(xi+1)+yi+1,(yteile+1)*xi+yi+1]
			ii+=4

	glVertexPointer(3, GL_FLOAT, 0, vertices)
	glNormalPointer(GL_FLOAT, 0, normals)

	glDrawElements(GL_QUADS,4*xteile*yteile-8*4 , GL_UNSIGNED_INT,indices)

	glDisableClientState(GL_VERTEX_ARRAY)
	glDisableClientState(GL_NORMAL_ARRAY)


#Table surface Texture
def TableSurfaceTexture() :
	'''
	'''

	xteile, yteile = 16, 8
	widthx=264.0/xteile
	widthy=137.0/yteile
	vertices = [.0]* (3*(xteile+1)*(yteile+1))
	normals = [.0]* (3*(xteile+1)*(yteile+1))
	texcoord = [.0]* (2*(xteile+1)*(yteile+1))
	indices = [0]*(4*xteile*yteile)

	iv=0
	it=0
	for x in range(xteile+1):
		for y in range(yteile+1) :
			vertices[iv:iv+3]=[-132+x*widthx,-68.5+y*widthy,0]
			normals[iv:iv+3]=[0,0,1]
			iv+=3
			texcoord[it:it+2]=[(-132+x*widthx)/8.5,(-68.5+y*widthy)/8.5]
			it+=2
		
	ii=0;
	for xi in range(xteile) :
		for yi in range(yteile) :
			if (((yi==0)and((xi==0)or(xi==(xteile/2)-1)or(xi==xteile/2)or(xi==xteile-1)))
			or((yi==yteile-1)and((xi==0)or(xi==(xteile/2)-1)or(xi==xteile/2)or(xi==xteile-1)))):
				continue
			indices[ii:ii+4] = [
				(yteile+1)*xi+yi,
				(yteile+1)*(xi+1)+yi,
				(yteile+1)*(xi+1)+yi+1,
				(yteile+1)*xi+yi+1 ]
			ii+=4
	
	glEnableClientState(GL_VERTEX_ARRAY);
	glEnableClientState(GL_NORMAL_ARRAY);
	glEnableClientState(GL_TEXTURE_COORD_ARRAY);
	glVertexPointer(3, GL_FLOAT, 0, vertices);
	glNormalPointer(GL_FLOAT, 0, normals);
	glTexCoordPointer(2, GL_FLOAT, 0, texcoord);
	glDrawElements(GL_QUADS,4*xteile*yteile-8*4 , GL_UNSIGNED_INT,indices);
	glDisableClientState(GL_VERTEX_ARRAY)
	glDisableClientState(GL_NORMAL_ARRAY)
	glDisableClientState(GL_TEXTURE_COORD_ARRAY)


#Center hole panel
def MidHolePanel() :
	mat_ambient = [0, 0, 0, 1]
	mat_diffuse = [0.6, 0.45, 0, 1]
	mat_specular = [2, 2, 2, 2]
	mat_shininess = 127.0
	glMaterialfv(GL_FRONT, GL_AMBIENT,mat_ambient);
	glMaterialfv(GL_FRONT, GL_DIFFUSE,mat_diffuse);
	glMaterialfv(GL_FRONT, GL_SPECULAR,mat_specular);
	glMaterialf(GL_FRONT, GL_SHININESS,mat_shininess);

	glEnableClientState(GL_VERTEX_ARRAY);
	glEnableClientState(GL_NORMAL_ARRAY);

	iv=0
	#in=0

	#0
	vertices = [
		7.5, 68.5, 5,
		7.5, 72.7, 3.3+1.5,
		7.5, 76.5, 2.9+1.5,
		7.5, 80, 2.1+1.5,
		3.75, 80, 2.1+1.5,
		0, 80, 2.1+1.5,
		-3.75, 80, 2.1+1.5,
		-7.5, 80, 2.1+1.5,
		-7.5, 76.5, 2.9+1.5,
		-7.5, 72.7, 3.3+1.5,
		-7.5, 68.5, 5,
		6.5, 68.5, 5,
		5.6, 72.7, 3.3+1.5,
		5, 74.6, 3.15+1.5,
		3.75, 76.25, 2.9+1.5,
		2.05, 77.2, 2.7+1.5,
		0, 77.6, 2.65+1.5,
		-2.05, 77.2, 2.7+1.5,
		-3.75, 76.25, 2.9+1.5,
		-5, 74.6, 3.15+1.5,
		-5.6, 72.7, 3.3+1.5,
		-6.5, 68.5, 5,
		7.5, 81.8, 1.1+1.5,
		3.75, 81.8, 1.1+1.5,
		0, 81.8, 1.1+1.5,
		-3.75, 81.8, 1.1+1.5,
		-7.5, 81.8, 1.1+1.5,
		7.5, 82.5, 0.0+1.5,
		3.75, 82.5, 0.0+1.5,
		0, 82.5, 0.0+1.5,
		-3.75, 82.5, 0+1.5,
		-7.5, 82.5, 0+1.5,
		7.5, 82.5, -10,
		3.75, 82.5, -10,
		0, 82.5, -10,
		-3.75, 82.5, -10,
		-7.5, 82.5, -10
	]
	normals = [
		0, 0, 1,
		0, 0.1, 1,
		0, 0.25, 0.97,
		0, 0.4, 0.91,
		0, 0.4, 0.91,
		0, 0.4, 0.91,
		0, 0.4, 0.91,
		0, 0.4, 0.91,
		0, 0.25, 0.97,
		0, 0.1, 1,
		0, 0, 1,
		0, 0, 1,
		0, 0.1, 1,
		0, 0.2, 0.97,
		0, 0.25, 0.97,
		0, 0.3, 0.95,
		0, 0.3, 0.95,
		0, 0.3, 0.95,
		0, 0.25, 0.97,
		0, 0.25, 0.97,
		0, 0.1, 1,
		0, 0, 1,
		0, 0.71, 0.71,
		0, 0.71, 0.71,
		0, 0.71, 0.71,
		0, 0.71, 0.71,
		0, 0.71, 0.71,
		0, 1, 0,
		0, 1, 0,
		0, 1, 0,
		0, 1, 0,
		0, 1, 0,
		0, 1, 0,
		0, 1, 0,
		0, 1, 0,
		0, 1, 0,
		0, 1, 0
	]
	
	indices=[0,1,12,11,
		1,2,13,12,
		2,3,14,13,
		3,4,15,14,
		4,5,16,15,
		5,6,17,16,
		6,7,18,17,
		7,8,19,18,
		8,9,20,19,
		9,10,21,20,
		3,22,23,4,
		4,23,24,5,
		5,24,25,6,
		6,25,26,7,
		22,27,28,23,
		23,28,29,24,
		24,29,30,25,
		25,30,31,26,
		27,32,33,28,
		28,33,34,29,
		29,34,35,30,
		30,35,36,31
	]

	glVertexPointer(3, GL_FLOAT, 0, vertices);
	glNormalPointer(GL_FLOAT, 0, normals);

	glDrawElements(GL_QUADS,22*4 , GL_UNSIGNED_INT,indices);

	glDisableClientState(GL_VERTEX_ARRAY);
	glDisableClientState(GL_NORMAL_ARRAY);

#Loch Eck panel
def EdgeHolePanel() :
	vertices=[
		0,-9,5,
		4.2,-9,4.8,
		0,-8.2,5,
		4.6,-3.2,4.8,
		5.6,0,4.8,
		5.2,2.1,4.8,
		4,4,4.8,
		2.1,5.2,4.8,
		0,5.6,4.8,
		-3.2,4.6,4.8,
		-8.2,0,5,
		-9,0,5,
		-9,4.2,4.8,
		8,-9,4.4,
		8,-4.5,4.4,
		8,0,4.4,
		7.4,3,4.4,
		5.7,5.7,4.4,
		3,7.4,4.4,
		0,8,4.4,
		-4.5,8,4.4,
		-9,8,4.4,
		11.5,-9,3.6,
		11.5,-4.5,3.6,
		11.5,0,3.6,
		10.6,4.4,3.6,
		8.1,8.1,3.6,
		4.4,10.6,3.6,
		0,11.5,3.6,
		-4.5,11.5,3.6,
		-9,11.5,3.6,
		13.3,-9,2.6,
		13.3,-4.5,2.6,
		13.3,0,2.6,
		12.2,5.1,2.6,
		9.4,9.4,2.6,
		5.1,12.2,2.6,
		0,13.3,2.6,
		-4.5,13.3,2.6,
		-9,13.3,2.6,
		14,-9,1.5,
		14,-4.5,1.5,
		14,0,1.5,
		12.9,5.3,1.5,
		9.9,9.9,1.5,
		5.3,12.9,1.5,
		0,14,1.5,
		-4.5,14,1.5,
		-9,14,1.5,
		14,-9,-10,
		14,-4.5,-10,
		14,0,-10,
		12.9,5.3,-10,
		9.9,9.9,-10,
		5.3,12.9,-10,
		0,14,-10,
		-4.5,14,-10,
		-9,14,-10
	]

	normals=[
		0,0,1,
		0.1,0,1,
		0,0,1,
		0.1,0,1,
		0.1,0,1,
		0.08,0.01,1,
		0.07,0.07,1,
		0.01,0.08,1,
		0,0.1,1,
		0,0.1,1,
		0,0,1,
		0,0,1,
		0,0.1,1,
		0.25,0,0.97,
		0.25,0,0.97,
		0.25,0,0.97,
		0.23,0.1,0.97,
		0.17,0.17,0.97,
		0.1,0.23,0.97,
		0,0.25,0.97,
		0,0.25,0.97,
		0,0.25,0.97,
		0.4,0,0.91,
		0.4,0,0.91,
		0.4,0,0.91,
		0.37,0.15,0.91,
		0.28,0.28,0.91,
		0.15,0.37,0.91,
		0,0.4,0.91,
		0,0.4,0.91,
		0,0.4,0.91,
		0.71,0,.71,
		0.71,0,.71,
		0.71,0,.71,
		0.66,.27,.71,
		0.5,.5,.71,
		0.27,.66,.71,
		0,.71,.71,
		0,.71,.71,
		0,.71,.71,
		1,0,0,
		1,0,0,
		1,0,0,
		0.92,.38,0,
		0.71,.71,0,
		0.38,.92,0,
		0,1,0,
		0,1,0,
		0,1,0,
		1,0,0,
		1,0,0,
		1,0,0,
		0.92,.38,0,
		0.71,.71,0,
		0.38,.92,0,
		0,1,0,
		0,1,0,
		0,1,0
	]

	indices=[
		0,1,3,2,
		1,13,14,3,
		3,14,15,4,
		4,15,16,5,
		5,16,17,6,
		6,17,18,7,
		7,18,19,8,
		8,19,20,9,
		9,20,21,12,
		9,12,11,10,
		13,22,23,14,
		14,23,24,15,
		15,24,25,16,
		16,25,26,17,
		17,26,27,18,
		18,27,28,19,
		19,28,29,20,
		20,29,30,21,
		22,31,32,23,
		23,32,33,24,
		24,33,34,25,
		25,34,35,26,
		26,35,36,27,
		27,36,37,28,
		28,37,38,29,
		29,38,39,30,
		31,40,41,32,
		32,41,42,33,
		33,42,43,34,
		34,43,44,35,
		35,44,45,36,
		36,45,46,37,
		37,46,47,38,
		38,47,48,39,
		40,49,50,41,
		41,50,51,42,
		42,51,52,43,
		43,52,53,44,
		44,53,54,45,
		45,54,55,46,
		46,55,56,47,
		47,56,57,48
	]

	mat_ambient=[0,0,0,1]
	mat_diffuse=[.6,.45,0,1]
	mat_specular=[2,2,2,2]
	mat_shininess = 127.0;
	glMaterialfv(GL_FRONT, GL_AMBIENT,mat_ambient);
	glMaterialfv(GL_FRONT, GL_DIFFUSE,mat_diffuse);
	glMaterialfv(GL_FRONT, GL_SPECULAR,mat_specular);
	glMaterialf(GL_FRONT, GL_SHININESS,mat_shininess);

	glEnableClientState(GL_VERTEX_ARRAY);
	glEnableClientState(GL_NORMAL_ARRAY);

	glVertexPointer(3, GL_FLOAT, 0, vertices);
	glNormalPointer(GL_FLOAT, 0, normals);

	glDrawElements(GL_QUADS,42*4 , GL_UNSIGNED_INT,indices);

	glDisableClientState(GL_VERTEX_ARRAY);
	glDisableClientState(GL_NORMAL_ARRAY);


#Center hole inner panel
def MidHoleInnerPanel() :

	vertices=[
		6.5,68.5,5,
		5.6,72.7,4.8,
		5,74.6,4.65,
		3.75,76.25,4.4,
		2.05,77.2,4.2,
		0,77.6,4.15,
		-2.05,77.2,4.2,
		-3.75,76.25,4.4,
		-5,74.6,4.65,
		-5.6,72.7,4.8,
		-6.5,68.5,5,
		6.5,68.5,2.5,
		7.1,74.2,2.5,
		6.2,75.5,2.5,
		4.6,77.2,2.5,
		2.8,78.4,2.5,
		0,79,2.5,
		-2.8,78.4,2.5,
		-4.6,77.2,2.5,
		-6.2,75.5,2.5,
		-7.1,74.2,2.5,
		-6.5,68.5,2.5,
		6.5,68.5,-10,
		7.1,74.2,-10,
		6.2,75.5,-10,
		4.6,77.2,-10,
		2.8,78.4,-10,
		0,79,-10,
		-2.8,78.4,-10,
		-4.6,77.2,-10,
		-6.2,75.5,-10,
		-7.1,74.2,-10,
		-6.5,68.5,-10]

	normals=[
		-5.8,-1,-5,
		-5.8,-1,-5,
		-4,-2.8,-5,
		-3.8,-4.4,-5,
		-2,-5.6,-5,
		0,-5.8,-5,
		2,-5.6,-5,
		3.8,-4.4,-5,
		4,-2.8,-5,
		5.8,-1,-5,
		5.8,-1,-5,
		-6.5,3.2,0,
		-7.1,-.9,0,
		-6.2,-3.8,0,
		-4.6,-5.5,0,
		-2.8,-6.8,0,
		0,-7.2,0,
		2.8,-6.8,0,
		4.6,-5.5,0,
		6.2,-3.8,0,
		7.1,-.9,0,
		-6.5,3.2,0,
		-6.5,3.2,0,
		-7.1,-.9,0,
		-6.2,-3.8,0,
		-4.6,-5.5,0,
		-2.8,-6.8,0,
		0,-7.2,0,
		2.8,-6.8,0,
		4.6,-5.5,0,
		6.2,-3.8,0,
		7.1,-.9,0,
		-6.5,3.2,0
	]

	indices=[
		0,1,12,11,
		1,2,13,12,
		2,3,14,13,
		3,4,15,14,
		4,5,16,15,
		5,6,17,16,
		6,7,18,17,
		7,8,19,18,
		8,9,20,19,
		9,10,21,20,
		11,12,23,22,
		12,13,24,23,
		13,14,25,24,
		14,15,26,25,
		15,16,27,26,
		16,17,28,27,
		17,18,29,28,
		18,19,30,29,
		19,20,31,30,
		20,21,32,31
	]

	mat_ambient=[0,0,0,1.0]
	mat_diffuse=[.3,.3,.3,1]
	mat_specular=[10.0,10.0,10.0,10.0]
	mat_shininess = 127.0;

	glMaterialfv(GL_FRONT, GL_AMBIENT,mat_ambient);
	glMaterialfv(GL_FRONT, GL_DIFFUSE,mat_diffuse);
	glMaterialfv(GL_FRONT, GL_SPECULAR,mat_specular);
	glMaterialf(GL_FRONT, GL_SHININESS,mat_shininess);

	glEnableClientState(GL_VERTEX_ARRAY);
	glEnableClientState(GL_NORMAL_ARRAY);

	glVertexPointer(3, GL_FLOAT, 0, vertices);
	glNormalPointer(GL_FLOAT, 0, normals);

	glDrawElements(GL_QUADS,4*20, GL_UNSIGNED_INT,indices);

	glDisableClientState(GL_VERTEX_ARRAY);
	glDisableClientState(GL_NORMAL_ARRAY);

def EckLochInnenverkleidung() :
	vertices=[0,-8.2,5,
		4.6,-3.2,4.8,
		5.6,0,4.8,
		5.2,2.1,4.8,
		4,4,4.8,
		2.1,5.2,4.8,
		0,5.6,4.8,
		-3.2,4.6,4.8,
		-8.2,0,5,
		0,-8.2,2.5,
		5.7,-4,2.5,
		6.3,0,2.5,
		5.7,2.3,2.5,
		4.3,4.3,2.5,
		2.3,5.7,2.5,
		0,6.3,2.5,
		-4,5.7,2.5,
		-8.2,0,2.5,
		0,-8.2,-10,
		5.7,-4,-10,
		6.3,0,-10,
		5.7,2.3,-10,
		4.3,4.3,-10,
		2.3,5.7,-10,
		0,6.3,-10,
		-4,5.7,-10,
		-8.2,0,-10]

	normals=[0,8.2,-5,
		-4.6,3.2,-4.8,
		-5.6,0,-4.8,
		-5.2,-2.1,-4.8,
		-4,-4,-4.8,
		-2.1,-5.2,-4.8,
		0,-5.6,-4.8,
		3.2,-4.6,-4.8,
		8.2,0,-5,
		0,8.2,0,
		-5.7,4,0,
		-6.3,0,0,
		-5.7,-2.3,0,
		-4.3,-4.3,0,
		-2.3,-5.7,0,
		0,-6.3,0,
		4,-5.7,0,
		8.2,0,0,
		0,8.2,0,
		-5.7,4,0,
		-6.3,0,0,
		-5.7,-2.3,0,
		-4.3,-4.3,0,
		-2.3,-5.7,0,
		0,-6.3,0,
		4,-5.7,0,
		8.2,0,0,]

	indices=[0,1,10,9,
		1,2,11,10,
		2,3,12,11,
		3,4,13,12,
		4,5,14,13,
		5,6,15,14,
		6,7,16,15,
		7,8,17,16,
		9,10,19,18,
		10,11,20,19,
		11,12,21,20,
		12,13,22,21,
		13,14,23,22,
		14,15,24,23,
		15,16,25,24,
		16,17,26,25]

	mat_ambient=[0,0,0,1.0]
	mat_diffuse=[.3,.3,.3,1]
	mat_specular=[10.0,10.0,10.0,10.0]
	mat_shininess = 127.0;


	glMaterialfv(GL_FRONT, GL_AMBIENT,mat_ambient);
	glMaterialfv(GL_FRONT, GL_DIFFUSE,mat_diffuse);
	glMaterialfv(GL_FRONT, GL_SPECULAR,mat_specular);
	glMaterialf(GL_FRONT, GL_SHININESS,mat_shininess);


	glEnableClientState(GL_VERTEX_ARRAY);
	glEnableClientState(GL_NORMAL_ARRAY);

	glVertexPointer(3, GL_FLOAT, 0, vertices);
	glNormalPointer(GL_FLOAT, 0, normals);

	glDrawElements(GL_QUADS,4*16, GL_UNSIGNED_INT,indices);

	glDisableClientState(GL_VERTEX_ARRAY);
	glDisableClientState(GL_NORMAL_ARRAY);




#木边
def WoodBand(Breite, Unterteilungen, TexFaktorX, TexFaktorY):

	mat_diffuse=[1.0,1.0,1.0,1.0]
	mat_specular=[1.0,1.0,1.0,1.0]
	mat_shininess = 127.0;

	glMaterialfv(GL_FRONT, GL_AMBIENT,mat_diffuse);
	glMaterialfv(GL_FRONT, GL_DIFFUSE,mat_diffuse);
	glMaterialfv(GL_FRONT, GL_SPECULAR,mat_specular);
	glMaterialf(GL_FRONT, GL_SHININESS,mat_shininess);

	vertices = [.0]* (3*7*(Unterteilungen+1));
	normals = [.0]* (3*7*(Unterteilungen+1));
	indices = [0]*(1000+4*6*Unterteilungen); 
	texcoord = [.0]* (2*7*(Unterteilungen+1));

	TeilBreite=Breite/Unterteilungen;

	glEnableClientState(GL_VERTEX_ARRAY);
	glEnableClientState(GL_NORMAL_ARRAY);
	glEnableClientState(GL_TEXTURE_COORD_ARRAY);

	iv,ii,it=0,0,0
	for u in range(Unterteilungen+1) :
		vertices[iv:iv+3*7] = [
			u*TeilBreite, 0, 5,
			u*TeilBreite, 4.2, 4.8,
			u*TeilBreite, 8, 4.4,
			u*TeilBreite, 11.5, 3.6,
			u*TeilBreite, 13.3, 2.6,
			u*TeilBreite, 14, 1.5,
			u*TeilBreite, 14, -10
		]
		normals[iv:iv+3*7] = [
			0, 0, 1,
			0, .1, 1,
			0, .25, .97,
			0, .4, .91,
			0, .71, .71,
			0, 1, 0,
			0, 1, 0
		]
		texcoord[it:it+2*7] = [
			u*TexFaktorX/Unterteilungen, 0,
			u*TexFaktorX/Unterteilungen, .3*TexFaktorY,
			u*TexFaktorX/Unterteilungen, .57*TexFaktorY,
			u*TexFaktorX/Unterteilungen, .82*TexFaktorY,
			u*TexFaktorX/Unterteilungen, .95*TexFaktorY,
			u*TexFaktorX/Unterteilungen, TexFaktorY,
			u*TexFaktorX/Unterteilungen, .5*TexFaktorY
		]
		iv+=3*7
		it+=2*7
	

	for y in range(6):
		for x in range(Unterteilungen):
			indices[ii:ii+4]=[x*7+y+1,x*7+y,(x+1)*7+y,(x+1)*7+y+1]
			ii+=4

	glNormalPointer(GL_FLOAT, 0, normals);
	glVertexPointer(3, GL_FLOAT, 0, vertices);
	glTexCoordPointer(2, GL_FLOAT, 0, texcoord);

	glDrawElements(GL_QUADS,4*6*Unterteilungen, GL_UNSIGNED_INT,indices);

	glDisableClientState(GL_VERTEX_ARRAY);
	glDisableClientState(GL_NORMAL_ARRAY);
	glDisableClientState(GL_TEXTURE_COORD_ARRAY);


def WoodBandOT(Breite, Unterteilungen):

	mat_diffuse=[.45,.19,.03,1.0]
	mat_specular=[1.0,1.0,1.0,1.0]
	mat_shininess = 127.0;

	glMaterialfv(GL_FRONT, GL_AMBIENT,mat_diffuse);
	glMaterialfv(GL_FRONT, GL_DIFFUSE,mat_diffuse);
	glMaterialfv(GL_FRONT, GL_SPECULAR,mat_specular);
	glMaterialf(GL_FRONT, GL_SHININESS,mat_shininess);

	vertices = [.0]* (3*7*(Unterteilungen+1));
	normals = [.0]* (3*7*(Unterteilungen+1));
	indices = [0]*(1000+4*6*Unterteilungen); 

	TeilBreite=Breite/Unterteilungen;

	glEnableClientState(GL_VERTEX_ARRAY);
	glEnableClientState(GL_NORMAL_ARRAY);

	N=7
	iv=0
	ii=0
	for u in range(Unterteilungen+1) :
		vertices[iv:iv+3*N] = [
			u*TeilBreite, 0, 5,
			u*TeilBreite, 4.2, 4.8,
			u*TeilBreite, 8, 4.4,
			u*TeilBreite, 11.5, 3.6,
			u*TeilBreite, 13.3, 2.6,
			u*TeilBreite, 14, 1.5,
			u*TeilBreite, 14, -10
		]
		normals[iv:iv+3*N] = [
			0, 0, 1,
			0, .1, 1,
			0, .25, .97,
			0, .4, .91,
			0, .71, .71,
			0, 1, 0,
			0, 1, 0
		]
		iv+=3*N
		
	for y in range(6):
		for x in range(Unterteilungen):
			indices[ii:ii+4]=[x*7+y+1,x*7+y,(x+1)*7+y,(x+1)*7+y+1]
			ii+=4
		
	glNormalPointer(GL_FLOAT, 0, normals);
	glVertexPointer(3, GL_FLOAT, 0, vertices);

	glDrawElements(GL_QUADS,4*6*Unterteilungen, GL_UNSIGNED_INT,indices);

	glDisableClientState(GL_VERTEX_ARRAY);
	glDisableClientState(GL_NORMAL_ARRAY);



def Banden(richtung, Multiply): 
	# Banden berechnen

	#richtung=0 --> Banden links und rechts
	#richtung=1 --> Banden oben und unten

	vertices = [0.0]* (3*8);
	normals = [0.0]* (3*8);
	indices = [0]*(4*6); 

	# Banden links und rechts 

	if (richtung==0):
		vertices = [
			-132, -60.3, 0,
			-127, -53.56, 3.429,
			-127, -53.56, 3.829,
			-132, -60.3, 5,
			-132, 60.3, 0,
			-127, 53.56, 3.429,
			-127, 53.56, 3.829,
			-132, 60.3, 5
		]
		normals = [
			3.429, -1, -5,
			3.429, -1, -5,
			1.371, -1, 5,
			-3.829, -1, 5,
			3.429, 1, -5,
			3.429, 1, -5,
			1.371, 1, 5,
			-3.829, 1, 5
		]
		
		indices = [
			0, 4, 5, 1,
			1, 5, 6, 2,
			2, 6, 7, 3,
			0, 3, 7, 4,
			0, 1, 2, 3,
			4, 7, 6, 5
		]
	else:
		vertices = [
			-123.8*Multiply, 68.5, 0,
			-117.16*Multiply, 63.5, 3.429,
			-117.16*Multiply, 63.5, 3.829,
			-123.8*Multiply, 68.5, 5,
			-6.5*Multiply, 68.5, 0,
			-7.38*Multiply, 63.5, 3.429,
			-7.38*Multiply, 63.5, 3.829,
			-6.5*Multiply, 68.5, 5
		]
		normals = [
			-1, -3.429, -5,
			-1, -3.429, -5,
			-1, -1.371, 5,
			-1, 3.829, 5,
			1, -3.429, -5,
			1, -3.429, -5,
			1, -1.372, 5,
			1, 3.829, 5
		]

		if (Multiply == 1):
			indices = [
				0, 4, 5, 1,
				1, 5, 6, 2,
				2, 6, 7, 3,
				0, 3, 7, 4,
				0, 1, 2, 3,
				4, 7, 6, 5
			]
		elif (Multiply == -1):
			indices = [
				4, 0, 1, 5,
				5, 1, 2, 6,
				6, 2, 3, 7,
				4, 7, 3, 0,
				4, 5, 6, 7,
				1, 0, 3, 2
			]

	glEnableClientState(GL_VERTEX_ARRAY);
	glEnableClientState(GL_NORMAL_ARRAY);

	glNormalPointer(GL_FLOAT, 0, normals);
	glVertexPointer(3, GL_FLOAT, 0, vertices);

	glDrawElements(GL_QUADS, 16+8 , GL_UNSIGNED_INT,indices);

	glDisableClientState(GL_VERTEX_ARRAY);
	glDisableClientState(GL_NORMAL_ARRAY);


#Center hole edge
def MittelLochRand() :

	vertices=[
		6.3,70.8,4.8,
		6.2,72.7,4.7,
		5.5,75,4.55,
		4.1,76.6,4.3,
		2.3,77.7,4.2,
		0,78,4.05,
		-2.3,77.7,4.1,
		-4.1,76.6,4.2,
		-5.5,75,4.55,
		-6.2,72.7,4.7,
		-6.3,70.8,4.8,
		6.3,70.8,5.2,
		6.2,72.7,5.1,
		5.5,75,4.95,
		4.1,76.6,4.7,
		2.3,77.7,4.5,
		0,78,4.45,
		-2.3,77.7,4.5,
		-4.1,76.6,4.6,
		-5.5,75,4.95,
		-6.2,72.7,5.1,
		-6.3,70.8,5.2,
		5.8,70.7,5.2,
		5.3,72.8,5.1,
		4.6,74.7,4.95,
		3.3,75.7,4.7,
		1.7,76.4,4.5,
		0,76.5,4.45,
		-1.7,76.4,4.5,
		-3.3,75.7,4.7,
		-4.6,74.7,4.95,
		-5.3,72.8,5.1,
		-5.8,70.7,5.2,
		5.8,70.7,4.8,
		5.3,72.8,4.7,
		4.6,74.7,4.55,
		3.3,75.7,4.3,
		1.7,76.4,4.1,
		0,76.5,4.05,
		-1.7,76.4,4.1,
		-3.3,75.7,4.3,
		-4.6,74.7,4.55,
		-5.3,72.8,4.7,
		-5.8,70.7,4.8
	]


	normals=[
		1,.1,-3,
		1,0,-3,
		.8,.6,-3,
		.7,.7,-3,
		.4,.9,-3,
		0,1,-3,
		-.4,.9,-3,
		-.7,.7,-3,
		-.8,.6,-3,
		-1,0,-3,
		-1,.1,-3,
		1,.1,3,
		1,0,3,
		.8,.6,3,
		.7,.7,3,
		.4,.9,3,
		0,1,3,
		-.4,.9,3,
		-.7,.7,3,
		-.8,.6,3,
		-1,0,3,
		-1,.1,3,
		-1,-.1,3,
		-1,0,3,
		-.8,-.6,3,
		-.7,-.7,3,
		-.4,-.9,3,
		0,-1,3,
		.4,-.9,3,
		.7,-.7,3,
		.8,-.6,3,
		1,0,3,
		1,-.1,3,
		-1,-.1,-3,
		-1,0,-3,
		-.8,-.6,-3,
		-.7,-.7,-3,
		-.4,-.9,-3,
		0,-1,-3,
		.4,-.9,-3,
		.7,-.7,-3,
		.8,-.6,-3,
		1,0,-3,
		1,-.1,-3]

	indices=[0,1,12,11,
		1,2,13,12,
		2,3,14,13,
		3,4,15,14,
		4,5,16,15,
		5,6,17,16,
		6,7,18,17,
		7,8,19,18,
		8,9,20,19,
		9,10,21,20,

		11,12,23,22,
		12,13,24,23,
		13,14,25,24,
		14,15,26,25,
		15,16,27,26,
		16,17,28,27,
		17,18,29,28,
		18,19,30,29,
		19,20,31,30,
		20,21,32,31,

		22,23,34,33,
		23,24,35,34,
		24,25,36,35,
		25,26,37,36,
		26,27,38,37,
		27,28,39,38,
		28,29,40,39,
		29,30,41,40,
		30,31,42,41,
		31,32,43,42,
		0,11,22,33,
		10,43,32,21]

	mat_ambient=[.1,.1,.1,1.0]
	mat_diffuse=[.3,.3,.3,1]
	mat_specular=[1.0,1.0,1.0,1.0]
	mat_shininess = 127.0;

	glMaterialfv(GL_FRONT, GL_AMBIENT,mat_ambient);
	glMaterialfv(GL_FRONT, GL_DIFFUSE,mat_diffuse);
	glMaterialfv(GL_FRONT, GL_SPECULAR,mat_specular);
	glMaterialf(GL_FRONT, GL_SHININESS,mat_shininess);


	glEnableClientState(GL_VERTEX_ARRAY);
	glEnableClientState(GL_NORMAL_ARRAY);

	glVertexPointer(3, GL_FLOAT, 0, vertices);
	glNormalPointer(GL_FLOAT, 0, normals);

	glDrawElements(GL_QUADS,4*32, GL_UNSIGNED_INT,indices);

	glDisableClientState(GL_VERTEX_ARRAY);
	glDisableClientState(GL_NORMAL_ARRAY);



#Eck hole edge
def EckLochRand() :

	vertices=[2.5,-5.9,4.8,
		5,-3.5,4.7,
		6.1,0,4.7,
		5.8,2.3,4.7,
		4.4,4.4,4.7,
		2.3,5.8,4.7,
		0,6.1,4.7,
		-3.5,5,4.7,
		-5.9,2.5,4.8,

		2.5,-5.9,5.2,
		5,-3.5,5.1,
		6.1,0,5.1,
		5.8,2.3,5.1,
		4.4,4.4,5.1,
		2.3,5.8,5.1,
		0,6.1,5.1,
		-3.5,5,5.1,
		-5.9,2.5,5.2,

		2.1,-5.5,5.2,
		4.4,-3.1,5.1,
		5,0,5.1,
		4.4,1.8,5.1,
		3.3,3.3,5.1,
		1.8,4.4,5.1,
		0,5,5.1,
		-3.1,4.4,5.1,
		-5.5,2.1,5.2,

		2.1,-5.5,4.8,
		4.4,-3.1,4.7,
		5,0,4.7,
		4.4,1.8,4.7,
		3.3,3.3,4.7,
		1.8,4.4,4.7,
		0,5,4.7,
		-3.1,4.4,4.7,
		-5.5,2.1,4.8]

	normals=[.7,-.7,-3,
		.8,-.5,-3,
		1,0,-3,
		.9,.4,-3,
		.7,.7,-3,
		.9,.4,-3,
		1,0,-3,
		.8,-.5,-3,
		.7,-.7,-3,

		.7,-.7,3,
		.8,-.5,3,
		1,0,3,
		.9,.4,3,
		.7,.7,3,
		.9,.4,3,
		1,0,3,
		.8,-.5,3,
		.7,-.7,3,

		-.7,.7,3,
		-.8,.5,3,
		-1,0,3,
		-.9,-.4,3,
		-.7,-.7,3,
		-.9,-.4,3,
		-1,0,3,
		-.8,.5,3,
		-.7,.7,3,
		
		-.7,.7,-3,
		-.8,.5,-3,
		-1,0,-3,
		-.9,-.4,-3,
		-.7,-.7,-3,
		-.9,-.4,-3,
		-1,0,-3,
		-.8,.5,-3,
		-.7,.7,-3]

	indices=[0,1,10,9,
		1,2,11,10,
		2,3,12,11,
		3,4,13,12,
		4,5,14,13,
		5,6,15,14,
		6,7,16,15,
		7,8,17,16,

		9,10,19,18,
		10,11,20,19,
		11,12,21,20,
		12,13,22,21,
		13,14,23,22,
		14,15,24,23,
		15,16,25,24,
		16,17,26,25,

		18,19,28,27,
		19,20,29,28,
		20,21,30,29,
		21,22,31,30,
		22,23,32,31,
		23,24,33,32,
		24,25,34,33,
		25,26,35,34,
		0,9,18,27,
		35,26,17,8
	]

	mat_ambient=[.1,.1,.1,1.0]
	mat_diffuse=[.3,.3,.3,1]
	mat_specular=[1.0,1.0,1.0,1.0]
	mat_shininess = 127.0;

	glMaterialfv(GL_FRONT, GL_AMBIENT,mat_ambient);
	glMaterialfv(GL_FRONT, GL_DIFFUSE,mat_diffuse);
	glMaterialfv(GL_FRONT, GL_SPECULAR,mat_specular);
	glMaterialf(GL_FRONT, GL_SHININESS,mat_shininess);

	glEnableClientState(GL_VERTEX_ARRAY);
	glEnableClientState(GL_NORMAL_ARRAY);

	glVertexPointer(3, GL_FLOAT, 0, vertices);
	glNormalPointer(GL_FLOAT, 0, normals);

	glDrawElements(GL_QUADS,4*26, GL_UNSIGNED_INT,indices);

	glDisableClientState(GL_VERTEX_ARRAY);
	glDisableClientState(GL_NORMAL_ARRAY);


def Diamond(x,  y,  z):
	glBegin(GL_QUADS);
	
	glNormal3f(0,0,1);
	glVertex3f(x+0.0,y+0.5,z);
	glVertex3f(x-0.5,y+0.0,z);
	glVertex3f(x+0.0,y-0.5,z);
	glVertex3f(x+0.5,y+0.0,z);
	
	glNormal3f(-0.235,0.235,0.94);
	glVertex3f(x+0.0,y+0.5,z-0.0);
	glVertex3f(x+0.0,y+1.5,z-0.3);
	glVertex3f(x-1.5,y+0.0,z-0.3);
	glVertex3f(x-0.5,y+0.0,z-0.0);
	
	glNormal3f(-0.235,-0.235,0.94);
	glVertex3f(x-0.5,y+0.0,z-0.0);
	glVertex3f(x-1.5,y+0.0,z-0.3);
	glVertex3f(x-0.0,y-1.5,z-0.3);
	glVertex3f(x-0.0,y-0.5,z-0.0);
	
	glNormal3f(0.235,-0.235,0.94);
	glVertex3f(x+0.0,y-0.5,z-0.0);
	glVertex3f(x+0.0,y-1.5,z-0.3);
	glVertex3f(x+1.5,y+0.0,z-0.3);
	glVertex3f(x+0.5,y+0.0,z-0.0);
	
	glNormal3f(0.235,0.235,0.94);
	glVertex3f(x+0.5,y+0.0,z-0.0);
	glVertex3f(x+1.5,y+0.0,z-0.3);
	glVertex3f(x-0.0,y+1.5,z-0.3);
	glVertex3f(x-0.0,y+0.5,z-0.0);
	
	glEnd()


tableCVV1 = [
	[[1.0,1.0,1.0,0],[-64.2,68.5,-2.8575],[-64.2,0.7,-2.8575]],
	[[1.0,1.0,1.0,.2],[-63.5,0.0,-2.8575],[-63.5,68.5,-2.8575]],
	[[1.0,1.0,1.0,0],[-64.2,0.7,-2.8575],[-65.2,0.7,-2.8575]],
	[[1.0,1.0,1.0,.2],[-64.5,0.0,-2.8575],[-63.5,0.0,-2.8575]],
	[[1.0,1.0,1.0,0],[-65.2,0.7,-2.8575],[-65.2,-0.7,-2.8575]],
	[[1.0,1.0,1.0,.2],[-64.5,0.0,-2.8575],[-64.5,0.0,-2.8575]],
	[[1.0,1.0,1.0,0],[-65.2,-0.7,-2.8575],[-64.2,-0.7,-2.8575]],
	[[1.0,1.0,1.0,.2],[-63.5,0.0,-2.8575],[-64.5,0.0,-2.8575]],
	[[1.0,1.0,1.0,0],[-64.2,-0.7,-2.8575],[-64.2,-68.5,-2.8575]],
	[[1.0,1.0,1.0,.2],[-63.5,-68.5,-2.8575],[-63.5,0.0,-2.8575]],
	[[1.0,1.0,1.0,.2],[-63.5,68.5,-2.8575],[-63.5,0,-2.8575]],
	[[1.0,1.0,1.0,0],[-62.8,0,-2.8575],[-62.8,68.5,-2.8575]],
	[[1.0,1.0,1.0,0.2],[-63.5,0,-2.8575],[-63.5,-68.5,-2.8575]],
	[[1.0,1.0,1.0,0],[-62.8,-68.5,-2.8575],[-62.8,0,-2.8575]],
	[[1.0,1.0,1.0,0],[-.5,0.5,-2.8575],[-1.5,0.5,-2.8575]],
	[[1.0,1.0,1.0,.2],[-1,0.0,-2.8575],[0,0.0,-2.8575]],
	[[1.0,1.0,1.0,0],[-1.5,0.5,-2.8575],[-1.5,-0.5,-2.8575]],
	[[1.0,1.0,1.0,.2],[-1,0.0,-2.8575],[-1,0.0,-2.8575]],
	[[1.0,1.0,1.0,0],[-1.5,-0.5,-2.8575],[-.5,-0.5,-2.8575]],
	[[1.0,1.0,1.0,.2],[0,0.0,-2.8575],[-1,0.0,-2.8575]],
	[[1.0,1.0,1.0,0],[-.5,-0.5,-2.8575],[-.5,-1.5,-2.8575]],
	[[1.0,1.0,1.0,.2],[0,-1,-2.8575],[0,0.0,-2.8575]],
	[[1.0,1.0,1.0,0],[-.5,-1.5,-2.8575],[.5,-1.5,-2.8575]],
	[[1.0,1.0,1.0,.2],[0,-1,-2.8575],[0,-1,-2.8575]],
	[[1.0,1.0,1.0,0],[.5,-1.5,-2.8575],[.5,-0.5,-2.8575]],
	[[1.0,1.0,1.0,.2],[0,0.0,-2.8575],[0,-1,-2.8575]],
	[[1.0,1.0,1.0,0],[.5,-0.5,-2.8575],[1.5,-0.5,-2.8575]],
	[[1.0,1.0,1.0,.2],[1,0.0,-2.8575],[0,0.0,-2.8575]],
	[[1.0,1.0,1.0,0],[1.5,-0.5,-2.8575],[1.5,0.5,-2.8575]],
	[[1.0,1.0,1.0,.2],[1,0.0,-2.8575],[1,0.0,-2.8575]],
	[[1.0,1.0,1.0,0],[1.5,0.5,-2.8575],[.5,0.5,-2.8575]],
	[[1.0,1.0,1.0,.2],[0,0.0,-2.8575],[1,0.0,-2.8575]],
	[[1.0,1.0,1.0,0],[.5,0.5,-2.8575],[.5,1.5,-2.8575]],
	[[1.0,1.0,1.0,.2],[0,1,-2.8575],[0,0.0,-2.8575]],
	[[1.0,1.0,1.0,0],[.5,1.5,-2.8575],[-.5,1.5,-2.8575]],
	[[1.0,1.0,1.0,.2],[0,1,-2.8575],[0,1,-2.8575]],
	[[1.0,1.0,1.0,0],[-.5,1.5,-2.8575],[-.5,0.5,-2.8575]],
	[[1.0,1.0,1.0,.2],[0,0.0,-2.8575],[0,1,-2.8575]]
]	
tableCVV2=[	
	[[1.0,1.0,1.0,0],[-2.91,1.68,-2.8575],[-3.36,0,-2.8575]],
	[[1.0,1.0,1.0,.2],[-2.86,0,-2.8575],[-2.47,1.43,-2.8575]],
	[[1.0,1.0,1.0,0],[-1.68,2.91,-2.8575],[-2.91,1.68,-2.8575]],
	[[1.0,1.0,1.0,.2],[-2.47,1.43,-2.8575],[-1.43,2.47,-2.8575]],
	[[1.0,1.0,1.0,0],[13.17,11.48,-2.8575],[-1.68,2.91,-2.8575]],
	[[1.0,1.0,1.0,.2],[-1.43,2.47,-2.8575],[13.42,11.05,-2.8575]],
	[[1.0,1.0,1.0,0],[14.85,11.93,-2.8575],[13.17,11.48,-2.8575]],
	[[1.0,1.0,1.0,.2],[13.42,11.05,-2.8575],[14.85,11.43,-2.8575]],
	[[1.0,1.0,1.0,0],[16.53,11.48,-2.8575],[14.85,11.93,-2.8575]],
	[[1.0,1.0,1.0,.2],[14.85,11.43,-2.8575],[16.28,11.05,-2.8575]],
	[[1.0,1.0,1.0,0],[17.76,10.25,-2.8575],[16.53,11.48,-2.8575]],
	[[1.0,1.0,1.0,.2],[16.28,11.05,-2.8575],[17.32,10.00,-2.8575]],
	[[1.0,1.0,1.0,0],[18.21,8.57,-2.8575],[17.76,10.25,-2.8575]],
	[[1.0,1.0,1.0,.2],[17.32,10.00,-2.8575],[17.71,8.57,-2.8575]],
	[[1.0,1.0,1.0,0],[18.21,0.5,-2.8575],[18.21,8.57,-2.8575]],
	[[1.0,1.0,1.0,.2],[17.71,8.57,-2.8575],[17.71,0.0,-2.8575]],
	[[1.0,1.0,1.0,0],[53,0.5,-2.8575],[18.21,0.5,-2.8575]],
	[[1.0,1.0,1.0,.2],[17.71,0.0,-2.8575],[53,0.0,-2.8575]],
	[[1.0,1.0,1.0,0],[18.21,-0.5,-2.8575],[53,-0.5,-2.8575]],
	[[1.0,1.0,1.0,.2],[53,0.0,-2.8575],[17.71,0.0,-2.8575]],
	[[1.0,1.0,1.0,0],[18.21,-8.57,-2.8575],[18.21,-0.5,-2.8575]],
	[[1.0,1.0,1.0,.2],[17.71,0.0,-2.8575],[17.71,-8.57,-2.8575]],
	[[1.0,1.0,1.0,0],[17.76,-10.25,-2.8575],[18.21,-8.57,-2.8575]],
	[[1.0,1.0,1.0,.2],[17.71,-8.57,-2.8575],[17.32,-10.0,-2.8575]],
	[[1.0,1.0,1.0,0],[16.53,-11.48,-2.8575],[17.76,-10.25,-2.8575]],
	[[1.0,1.0,1.0,.2],[17.32,-10.0,-2.8575],[16.28,-11.05,-2.8575]],
	[[1.0,1.0,1.0,0],[14.85,-11.93,-2.8575],[16.53,-11.48,-2.8575]],
	[[1.0,1.0,1.0,.2],[16.28,-11.05,-2.8575],[14.85,-11.43,-2.8575]],
	[[1.0,1.0,1.0,0],[13.17,-11.48,-2.8575],[14.85,-11.93,-2.8575]],
	[[1.0,1.0,1.0,.2],[14.85,-11.43,-2.8575],[13.42,-11.05,-2.8575]],
	[[1.0,1.0,1.0,0],[-1.68,-2.91,-2.8575],[13.17,-11.48,-2.8575]],
	[[1.0,1.0,1.0,.2],[13.42,-11.05,-2.8575],[-1.43,-2.47,-2.8575]],
	[[1.0,1.0,1.0,0],[-2.91,-1.68,-2.8575],[-1.68,-2.91,-2.8575]],
	[[1.0,1.0,1.0,.2],[-1.43,-2.47,-2.8575],[-2.47,-1.43,-2.8575]],
	[[1.0,1.0,1.0,0],[-3.36,0.0,-2.8575],[-2.91,-1.68,-2.8575]],
	[[1.0,1.0,1.0,.2],[-2.47,-1.43,-2.8575],[-2.86,0.0,-2.8575]],
	[[1.0,1.0,1.0,0],[-2.36,0.0,-2.8575],[-2.04,1.18,-2.8575]],
	[[1.0,1.0,1.0,.2],[-2.47,1.43,-2.8575],[-2.86,0.0,-2.8575]],
	[[1.0,1.0,1.0,0],[-2.04,1.18,-2.8575],[-1.18,2.04,-2.8575]],
	[[1.0,1.0,1.0,.2],[-1.43,2.47,-2.8575],[-2.47,1.43,-2.8575]],
	[[1.0,1.0,1.0,0],[-1.18,2.04,-2.8575],[13.67,10.61,-2.8575]],
	[[1.0,1.0,1.0,.2],[13.42,11.05,-2.8575],[-1.43,2.47,-2.8575]],
	[[1.0,1.0,1.0,0],[13.67,10.61,-2.8575],[14.85,10.93,-2.8575]],
	[[1.0,1.0,1.0,.2],[14.85,11.43,-2.8575],[13.42,11.05,-2.8575]],
	[[1.0,1.0,1.0,0],[14.85,10.93,-2.8575],[16.03,10.61,-2.8575]],
	[[1.0,1.0,1.0,.2],[16.28,11.05,-2.8575],[14.85,11.43,-2.8575]],
	[[1.0,1.0,1.0,0],[16.03,10.61,-2.8575],[16.89,9.75,-2.8575]],
	[[1.0,1.0,1.0,.2],[17.32,10.0,-2.8575],[16.28,11.05,-2.8575]],
	[[1.0,1.0,1.0,0],[16.89,9.75,-2.8575],[17.21,8.57,-2.8575]],
	[[1.0,1.0,1.0,.2],[17.71,8.57,-2.8575],[17.32,10.0,-2.8575]],
	[[1.0,1.0,1.0,0],[17.21,8.57,-2.8575],[17.21,0.5,-2.8575]],
	[[1.0,1.0,1.0,.2],[17.71,0.0,-2.8575],[17.71,8.57,-2.8575]],
	[[1.0,1.0,1.0,0],[17.21,0.5,-2.8575],[0.5,0.5,-2.8575]],
	[[1.0,1.0,1.0,.2],[0.0,0.0,-2.8575],[17.71,0.0,-2.8575]],
	[[1.0,1.0,1.0,0],[0.5,0.5,-2.8575],[0.5,1.5,-2.8575]],
	[[1.0,1.0,1.0,.2],[0.0,1.0,-2.8575],[0.0,0.0,-2.8575]],
	[[1.0,1.0,1.0,0],[0.5,1.5,-2.8575],[-0.5,1.5,-2.8575]],
	[[1.0,1.0,1.0,.2],[0.0,1.0,-2.8575],[0.0,1.0,-2.8575]],
	[[1.0,1.0,1.0,0],[-0.5,1.5,-2.8575],[-0.5,-1.5,-2.8575]],
	[[1.0,1.0,1.0,.2],[0.0,-1.0,-2.8575],[0.0,1.0,-2.8575]],
	[[1.0,1.0,1.0,0],[-0.5,-1.5,-2.8575],[0.5,-1.5,-2.8575]],
	[[1.0,1.0,1.0,.2],[0.0,-1.0,-2.8575],[0.0,-1.0,-2.8575]],
	[[1.0,1.0,1.0,0],[0.5,-1.5,-2.8575],[0.5,-0.5,-2.8575]],
	[[1.0,1.0,1.0,.2],[0.0,0.0,-2.8575],[0.0,-1.0,-2.8575]],
	[[1.0,1.0,1.0,0],[0.5,-0.5,-2.8575],[17.21,-0.5,-2.8575]],
	[[1.0,1.0,1.0,.2],[17.71,0.0,-2.8575],[0.0,0.0,-2.8575]],
	[[1.0,1.0,1.0,0],[-2.04,-1.18,-2.8575],[-2.36,0.0,-2.8575]],
	[[1.0,1.0,1.0,.2],[-2.86,0.0,-2.8575],[-2.47,-1.43,-2.8575]],
	[[1.0,1.0,1.0,0],[-1.18,-2.04,-2.8575],[-2.04,-1.18,-2.8575]],
	[[1.0,1.0,1.0,.2],[-2.47,-1.43,-2.8575],[-1.43,-2.47,-2.8575]],
	[[1.0,1.0,1.0,0],[13.67,-10.61,-2.8575],[-1.18,-2.04,-2.8575]],
	[[1.0,1.0,1.0,.2],[-1.43,-2.47,-2.8575],[13.42,-11.05,-2.8575]],
	[[1.0,1.0,1.0,0],[14.85,-10.93,-2.8575],[13.67,-10.61,-2.8575]],
	[[1.0,1.0,1.0,.2],[13.42,-11.05,-2.8575],[14.85,-11.43,-2.8575]],
	[[1.0,1.0,1.0,0],[16.03,-10.61,-2.8575],[14.85,-10.93,-2.8575]],
	[[1.0,1.0,1.0,.2],[14.85,-11.43,-2.8575],[16.28,-11.05,-2.8575]],
	[[1.0,1.0,1.0,0],[16.89,-9.75,-2.8575],[16.03,-10.61,-2.8575]],
	[[1.0,1.0,1.0,.2],[16.28,-11.05,-2.8575],[17.32,-10.0,-2.8575]],
	[[1.0,1.0,1.0,0],[17.21,-8.57,-2.8575],[16.89,-9.75,-2.8575]],
	[[1.0,1.0,1.0,.2],[17.32,-10.0,-2.8575],[17.71,-8.57,-2.8575]],
	[[1.0,1.0,1.0,0],[17.21,-0.5,-2.8575],[17.21,-8.57,-2.8575]],
	[[1.0,1.0,1.0,.2],[17.71,-8.57,-2.8575],[17.71,-0.0,-2.8575]]
]
tableCVV3=[
	[[0.0,0.0,0.0,0.0],[-139,65,-2.8575],[139,65,-2.8575]],
	[[0.0,0.0,0.0,.6],[139,68.5,-2.8575],[-139,68.5,-2.8575]],
	[[0.0,0.0,0.0,0.0],[139,-65,-2.8575],[-139,-65,-2.8575]],
	[[0.0,0.0,0.0,.6],[-139,-68.5,-2.8575],[139,-68.5,-2.8575]],
	[[0.0,0.0,0.0,0.0],[128.5,65,-2.8575],[128.5,-65,-2.8575]],
	[[0.0,0.0,0.0,.6],[132,-65,-2.8575],[132,65,-2.8575]],
	[[0.0,0.0,0.0,0.0],[-128.5,-65,-2.8575],[-128.5,65,-2.8575]],
	[[0.0,0.0,0.0,.6],[-132,65,-2.8575],[-132,-65,-2.8575]]

]

#quarter hole
def quarterHole( x,  y,  xd,  yd, z1,  z2,  r1,  r2) :

	''' x = Breite des Rechtecks
	   y = H鰄e des Rechtecks
	   xd = Anzahl der Teile der x-Strecke
	   yd = Anzahl der Teile der y-Stecke
	   z1 = Tiefe 鋟遝rer Kreis
	   z2 = Tiefe innerer Kreis
	   r1 = innerer Radius
	   r2 = 鋟遝rer Radius
	   '''

	vertices = [.0] *(12*(xd+yd+1));
	normals = [.0] *(12*(xd+yd+1));
	indices = [0] *(12*(xd+yd));

	iv=0; 
	ii=0; 
	in1=0;
	for iy in range(yd):
		yi=(iy*y)/yd;
		laenge=sqrt(x*x+yi*yi);
		xn=x/laenge;
		yn=yi/laenge;

		vertices[iv:iv+3*4]=[
			x,yi,0,
			r1*xn,r1*yn,0,
			r2*xn,r2*yn,-z1,
			r2*xn,r2*yn,-z2
		]
		iv+=3*4
		
		normals[in1:in1+3*4] = [
			0,0,1,
			0,0,1,
			-xn,-yn,0,
			-xn,-yn,0
		]
		in1+=3*4
	
	for ix in range(xd,-1,-1):
	#for (int ix=xd;ix>=0;ix--) {
		xi=(ix*x)/xd;
		laenge=sqrt(xi*xi+y*y);
		xn=xi/laenge;
		yn=y/laenge;

		vertices[iv:iv+3*4]=[
			xi,y,0,
			r1*xn,r1*yn,0,
			r2*xn,r2*yn,-z1,
			r2*xn,r2*yn,-z2
		]
		iv+=3*4
		
		normals[in1:in1+3*4] = [
			0,0,1,
			0,0,1,
			-xn,-yn,0,
			-xn,-yn,0
		]
		in1+=3*4

	for b in range(xd+yd):
		for h in range(3):
			indices[ii:ii+4]=[
				4*b+h,
				4*(b+1)+h,
				4*(b+1)+h+1,
				4*b+h+1
			]
			ii+=4
		
	glEnableClientState(GL_VERTEX_ARRAY)
	glEnableClientState(GL_NORMAL_ARRAY)

	glNormalPointer(GL_FLOAT, 0, normals)
	glVertexPointer(3, GL_FLOAT, 0, vertices)

	glDrawElements(GL_QUADS,12*(xd+yd), GL_UNSIGNED_INT,indices)

	glDisableClientState(GL_VERTEX_ARRAY)
	glDisableClientState(GL_NORMAL_ARRAY)


#quarter hole
def quarterHole( x,  y,  xd,  yd,z1,  z2,  r1,  r2, xo, yo, m00, m01, m10, m11):
	''' x = Breite des Rechtecks
	   y = H鰄e des Rechtecks
	   xd = Anzahl der Teile der x-Strecke
	   yd = Anzahl der Teile der y-Stecke
	   z1 = Tiefe 鋟遝rer Kreis
	   z2 = Tiefe innerer Kreis
	   r1 = innerer Radius
	   r2 = 鋟遝rer Radius
	   '''

	vertices = [.0] *(12*(xd+yd+1))
	normals = [.0] *(12*(xd+yd+1))
	texcoord = [.0] *(8*(xd+yd+1))
	indices = [0]  *(12*(xd+yd))

	iv=0;
	ii=0
	in1=0; 
	it=0;

	for iy in range(yd):
		yi=(iy*y)/yd;
		laenge=sqrt(x*x+yi*yi);
		xn=x/laenge;
		yn=yi/laenge;

		vertices[iv:iv+3*4 ]=[
			x,yi,0,
			r1*xn, r1*yn, 0,
			r2*xn, r2*yn, -z1,
			r2*xn, r2*yn, -z2
		]
		iv+=3*4
		
		normals[in1:in1+3*4 ]=[
			0,0,1,
			0,0,1,
			-xn, -yn, 0,
			-xn, -yn, 0
		]
		in1+=3*4
		
		texcoord[it:it+2*4 ]=[
			(m00*x+m01*yi+xo)/8.5, (m10*x+m11*yi+yo)/8.5,
			(m00*r1*xn+m01*r1*yn+xo)/8.5, (m10*r1*xn+m11*r1*yn+yo)/8.5,
			(m00*r2*xn+m01*r2*yn+xo)/8.5, (m10*r2*xn+m11*r2*yn+yo)/8.5,
			(m00*r2*xn+m01*r2*yn+xo)/8.5, (m10*r2*xn+m11*r2*yn+yo)/8.5
		]
		it+=2*4
	

	for ix in range(xd,-1,-1):
		xi=(ix*x)/xd;
		laenge=sqrt(xi*xi+y*y);
		xn=xi/laenge;
		yn=y/laenge;

		vertices[iv:iv+3*4]=[
			xi,y,0,
			r1*xn, r1*yn, 0,
			r2*xn, r2*yn, -z1,
			r2*xn, r2*yn, -z2
		]
		iv+=3*4
		
		normals[in1:in1+3*4 ]=[
			0,0,1,
			0,0,1,
			-xn, -yn, 0,
			-xn, -yn, 0
		]
		in1+=3*4
		
		texcoord[it:it+2*4 ]=[
			(m00*xi+m01*y+xo)/8.5, (m10*xi+m11*y+yo)/8.5,
			(m00*r1*xn+m01*r1*yn+xo)/8.5, (m10*r1*xn+m11*r1*yn+yo)/8.5,
			(m00*r2*xn+m01*r2*yn+xo)/8.5, (m10*r2*xn+m11*r2*yn+yo)/8.5,
			(m00*r2*xn+m01*r2*yn+xo)/8.5, (m10*r2*xn+m11*r2*yn+yo)/8.5
		]
		it+=2*4
	
	for b in range(xd+yd):
		for h in range(3):
			indices[ii:ii+4]=[
				4*b+h,
				4*(b+1)+h,
				4*(b+1)+h+1,
				4*b+h+1
			]
			ii+=4
		
	glEnableClientState(GL_VERTEX_ARRAY)
	glEnableClientState(GL_NORMAL_ARRAY)
	glEnableClientState(GL_TEXTURE_COORD_ARRAY)

	glNormalPointer(GL_FLOAT, 0, normals)
	glVertexPointer(3, GL_FLOAT, 0, vertices)
	glTexCoordPointer(2, GL_FLOAT, 0, texcoord)

	glDrawElements(GL_QUADS,12*(xd+yd), GL_UNSIGNED_INT,indices);

	glDisableClientState(GL_VERTEX_ARRAY);
	glDisableClientState(GL_NORMAL_ARRAY);
	glDisableClientState(GL_TEXTURE_COORD_ARRAY);

class BallTable:
	'''
	
	'''

	def __init__(self,game):
		self.game = game
		self.TableAreaIndex = None
		self.BandenIndex = None
		self.LinesIndex = None
		self.TableAreaTexture=None
		self.HolzBandenTexture=None
		
	def Init(self, textureSize) :
		if not  self.LinesIndex:
			self.LinesIndex=glGenLists(1);
		
		#glNewList(self.LinesIndex, GL_COMPILE_AND_EXECUTE)
		glNewList(self.LinesIndex, GL_COMPILE)
		glDisable(GL_LIGHTING)

		glBegin(GL_QUADS);
		for CVV in tableCVV1:
			color=CVV[0]
			vertex1=CVV[1]
			vertex2=CVV[2]
			glColor4f(color[0],color[1],color[2],color[3])
			glVertex3f(vertex1[0],vertex1[1],vertex1[2])
			glVertex3f(vertex2[0],vertex2[1],vertex2[2])
		glEnd()

		glPushMatrix()
		glTranslatef(63.5,0.0,0.0)
		glScalef(1.35,1.35,1)
		glBegin(GL_QUADS)
		for CVV in tableCVV2:
			color=CVV[0]
			vertex1=CVV[1]
			vertex2=CVV[2]
			glColor4f(color[0],color[1],color[2],color[3])
			glVertex3f(vertex1[0],vertex1[1],vertex1[2])
			glVertex3f(vertex2[0],vertex2[1],vertex2[2])
		glEnd()
		glPopMatrix()

		glBegin(GL_QUADS);
		for CVV in tableCVV3:
			color=CVV[0]
			vertex1=CVV[1]
			vertex2=CVV[2]
			glColor4f(color[0],color[1],color[2],color[3])
			glVertex3f(vertex1[0],vertex1[1],vertex1[2])
			glVertex3f(vertex2[0],vertex2[1],vertex2[2])
		glEnd()

		glEnable(GL_LIGHTING)
		glEndList()

		'''
		draw table surface
		'''
		if not self.TableAreaTexture:
			self.TableAreaTexture = glGenTextures(1)

		if textureSize!=0 and textureSize<8 :
			T=textureSize;
			if (T==4) :
				T=2
			
			glBindTexture(GL_TEXTURE_2D,self.TableAreaTexture)
			Name = "images/"+str(T)+"/filzkachel.bmp"; 
			CreateTextureMipmap(Name)
			#createTextureMipmap(woodtex_r,woodtex_g,woodtex_b);
		
		if not self.TableAreaIndex:
			self.TableAreaIndex=glGenLists(1);      # Display List erzeugen
		
		glNewList(self.TableAreaIndex, GL_COMPILE)
		glPushMatrix()

		glTranslatef(0,0,-2.8575);     # Tisch um Kugelradius nach unten schieben

		# 254 x 127
		xteile=16;     # Anzahl muss gerade sein
		yteile=8;     # Anzahl muss gerade sein; 
		widthx=264.0/xteile;
		widthy=137.0/yteile;

		''' -------------------------
		   Flaeche berechnen  
		   ------------------------- 
	        '''  
		if textureSize!=0 and textureSize<8 :
			mat_ambient=[1.0,1.0,1.0,1.0];
			mat_diffuse=[1.0,1.0,1.0,1.0];
			mat_specular=[0,0,0,1.0];
			mat_shininess = 0.0;
			glMaterialfv(GL_FRONT, GL_AMBIENT,mat_ambient);
			glMaterialfv(GL_FRONT, GL_DIFFUSE,mat_diffuse);
			glMaterialfv(GL_FRONT, GL_SPECULAR,mat_specular);
			glMaterialf(GL_FRONT, GL_SHININESS,mat_shininess);
			glBindTexture(GL_TEXTURE_2D,self.TableAreaTexture);
			glEnable(GL_TEXTURE_2D)
			TableSurfaceTexture()

			# unten left
			glPushMatrix()
			glTranslatef(-133.29,-69.79,0);
			quarterHole(widthx+1.3,widthy+1.3,4,4,.63,10,9.84,9.21,-133.29,-69.79,1,0,0,1); 
			glPopMatrix()

			# unten middle 
			glPushMatrix();
			glTranslatef(0,-71.75,0);
			quarterHole(widthx+0.01,widthy+3.26,4,4,.63,10,7.62,6.99,0,-71.75,1,0,0,1);
			glPopMatrix();

			glPushMatrix();
			glTranslatef(0,-71.75,0);
			glRotatef(90,0,0,1);
			quarterHole(widthy+3.26,widthx+0.01,4,4,.63,10.2,7.62,6.99,0,-71.75,0,-1,1,0);
			glPopMatrix();

			#unten right  
			glPushMatrix();
			glTranslatef(133.29,-69.79,0); 
			glRotatef(90,0,0,1);
			quarterHole(widthy+1.3,widthx+1.3,4,4,.63,10,9.84,9.21,133.29,-69.79,0,-1,-1,0); 
			glPopMatrix();

			#oben rechts
			glPushMatrix();
			glTranslatef(133.29,69.79,0);
			glRotatef(180,0,0,1);
			quarterHole(widthx+1.3,widthy+1.3,4,4,.63,10,9.84,9.21,133.29,69.79,-1,0,0,-1); 
			glPopMatrix();

			#oben Mitte
			glPushMatrix();
			glTranslatef(0,71.75,0);
			glRotatef(180,0,0,1);
			quarterHole(widthx+0.1,widthy+3.26,4,4,.63,10,7.62,6.99,0,71.75,-1,0,0,-1); 
			glPopMatrix();

			glPushMatrix();
			glTranslatef(0,71.75,0);
			glRotatef(-90,0,0,1);
			quarterHole(widthy+3.26,widthx+0.1,4,4,.63,10,7.62,6.99,0,71.75,0,1,-1,0);
			glPopMatrix();

			#oben links
			glPushMatrix();
			glTranslatef(-133.29,69.79,0); 
			glRotatef(-90,0,0,1);
			quarterHole(widthy+1.3,widthx+1.3,4,4,.63,10,9.84,9.21,-133.29,69.79,0,1,-1,0); 
			glPopMatrix();
			glDisable(GL_TEXTURE_2D);
		
		else:
			mat_ambient=[0.1,0.45,0.2,1.0]
			mat_diffuse=[0.1,0.45,0.2,1.0]
			mat_specular=[0,0,0,1.0]
			mat_shininess = 0.0;
			glMaterialfv(GL_FRONT, GL_AMBIENT,mat_ambient);
			glMaterialfv(GL_FRONT, GL_DIFFUSE,mat_diffuse);
			glMaterialfv(GL_FRONT, GL_SPECULAR,mat_specular);
			glMaterialf(GL_FRONT, GL_SHININESS,mat_shininess);

			TableSurface();

			# unten links
			glPushMatrix();
			glTranslatef(-133.29,-69.79,0);
			quarterHole(widthx+1.3,widthy+1.3,4,4,.63,10,9.84,9.21); 
			glPopMatrix();

			# unten Mitte 
			glPushMatrix();
			glTranslatef(0,-71.75,0);
			quarterHole(widthx+0.01,widthy+3.26,4,4,.63,10,7.62,6.99);
			glPopMatrix();

			glPushMatrix();
			glTranslatef(0,-71.75,0);
			glRotatef(90,0,0,1);
			quarterHole(widthy+3.26,widthx+0.01,4,4,.63,10.2,7.62,6.99);
			glPopMatrix();

			#unten rechts   
			glPushMatrix();
			glTranslatef(133.29,-69.79,0); 
			glRotatef(90,0,0,1);
			quarterHole(widthy+1.3,widthx+1.3,4,4,.63,10,9.84,9.21); 
			glPopMatrix();

			#oben rechts
			glPushMatrix();
			glTranslatef(133.29,69.79,0);
			glRotatef(180,0,0,1);
			quarterHole(widthx+1.3,widthy+1.3,4,4,.63,10,9.84,9.21); 
			glPopMatrix();

			#oben Mitte
			glPushMatrix();
			glTranslatef(0,71.75,0);
			glRotatef(180,0,0,1);
			quarterHole(widthx+0.1,widthy+3.26,4,4,.63,10,7.62,6.99); 
			glPopMatrix();

			glPushMatrix();
			glTranslatef(0,71.75,0);
			glRotatef(-90,0,0,1);
			quarterHole(widthy+3.26,widthx+0.1,4,4,.63,10,7.62,6.99);
			glPopMatrix();

			#oben links
			glPushMatrix();
			glTranslatef(-133.29,69.79,0); 
			glRotatef(-90,0,0,1);
			quarterHole(widthy+1.3,widthx+1.3,4,4,.63,10,9.84,9.21); 
			glPopMatrix();

		glPopMatrix();
		glEndList();


		''' --------------------
		   Banden berechnen 
		   -------------------- '''
		if not self.HolzBandenTexture :
			self.HolzBandenTexture = glGenTextures(1)

		if (textureSize != 0) :
			Name = "images/"+ str(textureSize) +"/holz.bmp"
			#loadBMP(woodtex_r,woodtex_g,woodtex_b,Name);
			glBindTexture(GL_TEXTURE_2D, self.HolzBandenTexture);
			CreateTexture(Name);
		
		if not self.BandenIndex == 0 :
			self.BandenIndex=glGenLists(1);      # Display List erzeugen
		
		glNewList(self.BandenIndex, GL_COMPILE);
		
		mat_ambient=[0.1,0.45,0.2,1.0]
		mat_diffuse=[0.1,0.45,0.2,1.0]
		mat_specular=[0,0,0,1.0]
		mat_shininess = 127.0
		glMaterialfv(GL_FRONT, GL_AMBIENT,mat_ambient);
		glMaterialfv(GL_FRONT, GL_DIFFUSE,mat_diffuse);
		glMaterialfv(GL_FRONT, GL_SPECULAR,mat_specular);
		glMaterialf(GL_FRONT, GL_SHININESS,mat_shininess);

		glPushMatrix();

		glTranslatef(0,0,-2.8575);     # Tisch um Kugelradius nach unten schieben

		# Bande links 
		glPushMatrix();
		Banden(0,1);
		glPopMatrix();

		# Bande rechts 
		glPushMatrix();
		glRotatef(180,0,0,1);
		Banden(0,1);
		glPopMatrix();

		# Bande oben links
		glPushMatrix();
		Banden(1,1);
		glPopMatrix();    

		# Bande oben rechts
		glPushMatrix();
		Banden(1,-1);
		glPopMatrix();

		# Bande unten links
		glPushMatrix();
		glRotatef(180,0,0,1);
		Banden(1,-1);
		glPopMatrix();

		# Bande unten rechts
		glPushMatrix();
		glRotatef(180,0,0,1);
		Banden(1,1);
		glPopMatrix();

		#Verkleidungen (;)
		glPushMatrix();
		MidHolePanel();
		MidHoleInnerPanel();
		MittelLochRand();
		glRotatef(180,0,0,1);
		MidHolePanel();
		MidHoleInnerPanel();
		MittelLochRand();
		glPopMatrix();

		glPushMatrix();
		glTranslatef(132,68.5,0);
		EdgeHolePanel();
		EckLochInnenverkleidung();
		EckLochRand();
		glPopMatrix();

		glPushMatrix();
		glRotatef(180,0,0,1);
		glTranslatef(132,68.5,0);
		EdgeHolePanel();
		EckLochInnenverkleidung();
		EckLochRand();
		glPopMatrix();

		glPushMatrix();
		glRotatef(90,0,0,1);
		glTranslatef(68.5,132,0);
		EdgeHolePanel();
		EckLochInnenverkleidung();
		EckLochRand();
		glPopMatrix();

		glPushMatrix();
		glRotatef(-90,0,0,1);
		glTranslatef(68.5,132,0);
		EdgeHolePanel();
		EckLochInnenverkleidung();
		EckLochRand();
		glPopMatrix();

		mat_diffuse=[0.8,0.8,1.0,1.0]
		mat_specular=[1.0,0.8,0.8,1.0]
		mat_shininess = 127.0;

		glMaterialfv(GL_FRONT, GL_AMBIENT,mat_diffuse);
		glMaterialfv(GL_FRONT, GL_DIFFUSE,mat_diffuse);
		glMaterialfv(GL_FRONT, GL_SPECULAR,mat_specular);
		glMaterialf(GL_FRONT, GL_SHININESS,mat_shininess);
	
		#draw diamod
		Diamond(31.75,72.5,4.9);
		Diamond(63.5,72.5,4.9);
		Diamond(95.25,72.5,4.9);
		Diamond(-31.75,72.5,4.9);
		Diamond(-63.5,72.5,4.9);
		Diamond(-95.25,72.5,4.9);
		Diamond(31.75,-72.5,4.9);
		Diamond(63.5,-72.5,4.9);
		Diamond(95.25,-72.5,4.9);
		Diamond(-31.75,-72.5,4.9);
		Diamond(-63.5,-72.5,4.9);
		Diamond(-95.25,-72.5,4.9);
		Diamond(136.5,31.75,4.9);
		Diamond(136.5,0,4.9);
		Diamond(136.5,-31.75,4.9);
		Diamond(-136.5,31.75,4.9);
		Diamond(-136.5,0,4.9);
		Diamond(-136.5,-31.75,4.9);

		#Holzbanden
		if (textureSize != 0) :
			#CreateTexture("image/"+textureSize+"/holz.bmp");
			glBindTexture(GL_TEXTURE_2D,self.HolzBandenTexture);
			glEnable(GL_TEXTURE_2D);
			glTexEnvf(GL_TEXTURE_ENV,GL_TEXTURE_ENV_MODE,GL_MODULATE);

			glPushMatrix();
			glTranslatef(7.5,68.5,0);
			WoodBand(115.5,8,1,1);
			glPopMatrix();

			glPushMatrix();
			glRotatef(180,0,0,1);
			glTranslatef(7.5,68.5,0);
			WoodBand(115.5,8,1,1);
			glPopMatrix();

			glPushMatrix();
			glTranslatef(-123,68.5,0);
			WoodBand(115.5,8,1,1);
			glPopMatrix();

			glPushMatrix();
			glRotatef(180,0,0,1);
			glTranslatef(-123,68.5,0);
			WoodBand(115.5,8,1,1);
			glPopMatrix();

			glPushMatrix();
			glTranslatef(-132,-59.5,0);
			glRotatef(90,0,0,1);
			WoodBand(119,8,1,1);
			glPopMatrix();

			glPushMatrix();
			glTranslatef(132,59.5,0);
			glRotatef(-90,0,0,1);
			WoodBand(119,8,1,1);
			glPopMatrix();

			glDisable(GL_TEXTURE_2D);
		else:
			glPushMatrix();
			glTranslatef(7.5,68.5,0);
			WoodBandOT(115.5,8);
			glPopMatrix();

			glPushMatrix();
			glRotatef(180,0,0,1);
			glTranslatef(7.5,68.5,0);
			WoodBandOT(115.5,8);
			glPopMatrix();

			glPushMatrix();
			glTranslatef(-123,68.5,0);
			WoodBandOT(115.5,8);
			glPopMatrix();

			glPushMatrix();
			glRotatef(180,0,0,1);
			glTranslatef(-123,68.5,0);
			WoodBandOT(115.5,8);
			glPopMatrix();

			glPushMatrix();
			glTranslatef(-132,-59.5,0);
			glRotatef(90,0,0,1);
			WoodBandOT(119,8);
			glPopMatrix();

			glPushMatrix();
			glTranslatef(132,59.5,0);
			glRotatef(-90,0,0,1);
			WoodBandOT(119,8);
			glPopMatrix();

			mat_diffuse=[1.0,1.0,1.0,1.0]
			mat_specular=[1.0,1.0,1.0,1.0]
			mat_shininess = 0.0

			glMaterialfv(GL_FRONT, GL_AMBIENT,mat_diffuse);
			glMaterialfv(GL_FRONT, GL_DIFFUSE,mat_diffuse);
			glMaterialfv(GL_FRONT, GL_SPECULAR,mat_specular);
			glMaterialf(GL_FRONT, GL_SHININESS,mat_shininess);

		glPopMatrix();
		glEndList();

	def drawSurface(self) :
		glCallList(self.TableAreaIndex)
	
	def drawBorder(self) :
		glCallList(self.BandenIndex)
	
	def drawLine(self) :
		glCallList(self.LinesIndex)
	

