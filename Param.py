# -*-  coding: UTF-8 -*-
#
#!/usr/bin/env python
#

try:
	from OpenGL.GL import *
	from OpenGL.GLU import *
	from OpenGL.GLUT import *
except:
	print ('Error! need PyOpenGL')
	raise SystemExit

class GameType:
	EIGHT_BALL = 8
	NINE_BALL = 9
	RANDOM_BALL = 7
	EMPTY  = 0

class GameMode:
	TRAINING = 101
	TWO_PLAYERS = 102
	NETWORK_MODE = 103
	CPU_MODE = 104
	TUTORIAL = 105

class GameState:
	'''
	
	'''
	START = 0
	VIEWING = 1
	AIMING = 2
	READY = 3
	SHOOT = 4
	NEW_WHITE = 5
	JUDGING = 6

	def __init__(self, game):
		self.game = game
		self.state = StateMachine.START

	def setState(self, stat):
		self.state = stat


M_PI=3.14159265358979323846

# Global Params
class ParamDef:
	ScreenResolution=(1024, 768)			#
	TextureSize = 2                     #贴图大小
	DisplayTextureSize = 1          	#
	TableTextureSize = 2
	BallResolution = 7
	InvertX = 0
	InvertY = 0
	Game_Type = GameType.EIGHT_BALL
	Shadow = 1;
	TexMMM  = 3;
	Epsilon = 0.05;
	MouseSpeed = 0.4;
	PhysicsFrequenz = 400;
	FrictionFactor = 1.2;
	GangsFactor = 0.4;
	CollisionFactor = 0.95;
	ZBufferDelete = 1;
	ColorDepth = 16;
	Reflections = 0;
	Language = 0;					#
	ShowFPS = 0;
	AmbientLighting = 1;
	TableLamps = 2;
	GrueneLamp = 0;
	FullScreen = 0;
	DelayCompensation = 0
	EffectVolumeDown = 0.5;
	MusicVolumeDown = 0.5;

	Player1 = "Player1"
	Player2 = "Player2"
	NetworkPlayer = "NetworkPlayer"
	NetworkTeam = "NetworkTeam"
	
	Factor = 0;
	FrameTimePoint = 0;
	Frames = 0;
	StartTime = 0;
	ShotTime = 0;
	JudgeDecision = 0;			#
	Player1Win = 0;				#
	Player2Win = 0;				#
	Foul = 0;					#犯规
	RecodingChanges = 0;		#
	
def SaveConfig():
	pass

def LoadConfig():
	pass

def GetParams():
	pass
	
