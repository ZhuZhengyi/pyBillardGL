# -*-  coding: UTF-8 -*-
#
#!/usr/bin/env python
#

from Param import *

try:
	from OpenGL.GL import *
	from OpenGL.GLU import *
	from OpenGL.GLUT import *
except:
	print ('Error! need PyOpenGL')
	raise SystemExit

from Param import *
import Image

def CreateTextureAlpha(path_bmp):
	'''
	'''
	image = Image.open(path_bmp)
	ix = image.size[0]
	iy = image.size[1]
	image = image.tostring("raw", "RGBX", 0, -1)

	glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
	glPixelStorei(GL_UNPACK_ALIGNMENT,1)
	
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
	if ParamDef.TexMMM & 2:
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
	else:
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
	
	if ParamDef.TexMMM & 1:
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
	else:
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

	return ix,iy

def CreateTexture(path_bmp):
	'''

	'''

	image = Image.open(path_bmp)
	ix = image.size[0]
	iy = image.size[1]
	image = image.tostring("raw", "RGBX", 0, -1)
	
	glPixelStorei(GL_UNPACK_ALIGNMENT,1)
	
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
	if ParamDef.TexMMM & 2:
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
	else:
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
	
	if ParamDef.TexMMM & 1:
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
	else:
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

	glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
	
	return ix,iy

def CreateTextureMipmap(path_bmp) :
	image = Image.open(path_bmp)
	ix = image.size[0]
	iy = image.size[1]
	image = image.tostring("raw", "RGBX", 0, -1)

	glPixelStorei(GL_UNPACK_ALIGNMENT,1);

	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);

	if (ParamDef.TexMMM & 2) :
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
	else:
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);


	if (ParamDef.TexMMM & 1) :
		if (ParamDef.TexMMM & 4) :
			glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR);
		else:
			glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_NEAREST);
	else:
		if (ParamDef.TexMMM & 4) :
			glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST_MIPMAP_LINEAR);
		else :
			glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST_MIPMAP_NEAREST);
		
	#gluBuild2DMipmaps(GL_TEXTURE_2D, GL_RGB, ix, iy, GL_RGB, GL_FLOAT, image);
	gluBuild2DMipmaps(GL_TEXTURE_2D, GL_RGB, ix, iy, GL_RGB, GL_UNSIGNED_BYTE, image);

	return ix,iy

