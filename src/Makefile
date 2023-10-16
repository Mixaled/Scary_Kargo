RM = rm -rf
PY = python3
all: clean build start

start:
	cd bots && sh start.sh
clean:
	$(RM) bots/*.py bots/*.sh
build:
	$(PY) configParser.py
