#=============================================================================
#   FileName: Makefile
#     Author: zzy
#      Email: zzy@gmail.com
#   HomePage: http://zhuzhengyi.github.com
# LastChange: 2013-11-20 16:33:57
#=============================================================================

SRC.py=$(wildcard *.py)

TARGETS=BillardGL

all:${TARGETS}
	@echo "ok!"

${TARGETS} : ${SRC.py}
	@python BillardGL.py

clean:
	rm -rf *.pyc
