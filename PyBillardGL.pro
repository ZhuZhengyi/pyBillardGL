TEMPLATE = app
CONFIG -= console
CONFIG -= qt
TARGET	= PyBillardGL
#INCLUDEPATH += -I/usr/X11R6/include
#LIBS += -L. -L/usr/X11R6/lib -lGL -lGLU -lglut -lXmu -lXext -lX11 -lm -lXi

SOURCES += \
    Ball.py \
    BallTable.py \
    BillardGL.py \
    CreateTexture.py \
    Decision.py \
    EventHandler.py \
    Judge.py \
    Lighting.py \
    LoadingScreen.py \
    Menu.py \
    MouseKey.py \
    Param.py \
    Scale.py \
    Shadow.py \
    ShotStrength.py \
    TextItem.py

OTHER_FILES = \
    Makefile
