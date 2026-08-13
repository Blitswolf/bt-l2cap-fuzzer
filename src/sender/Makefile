# Makefile for the L2CAP sender
CXX = g++
CXXFLAGS = -O2 -std=c++20 -Wall
LIBS = -lbluetooth

sender: sender.cpp
	$(CXX) $(CXXFLAGS) sender.cpp -o sender $(LIBS)

clean:
	rm -f sender

# use
# run command:  make 		(#this compiles sender.cpp → a binary called "sender")
# make clean    			(# removes it)