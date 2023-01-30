CXX=g++
CXXFLAGS=-Wall -Iinclude
BIN=bin/kruskal

# liste des fichiers sources 
SRCS0=kruskal.cpp
DIR_GUARD=@mkdir -p $(@D)

default: $(BIN)

bin/kruskal: $(SRCS0)
	$(DIR_GUARD)
	$(CXX) $(CXXFLAGS) -o $@ $+

clean:
	rm -f $(BIN) *~