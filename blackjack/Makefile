DEBUG ?= TRUE
FLAGS += -std=c++17 -MMD -MP -Wall -Wextra

ifdef DEBUG
FLAGS += -O0 -ggdb
CFLAGS += -DDEBUG
else
FLAGS += -O2
CFLAGS += -DNDEBUG
LDFLAGS += -s
endif

CXX ?= c++

COMPILE = $(CXX) $(CFLAGS) $(FLAGS) -c
LINK = $(CXX) $(LDFLAGS) $(FLAGS)

SOURCES = blackjack.cpp
OBJECTS =  $(SOURCES:.cpp=.o)
DEPENDENCIES = $(OBJECTS:.o=.d)

EXECUTABLE = blackjack

.PHONY: all clean

all: $(EXECUTABLE)
-include $(DEPENDENCIES)
clean:
	-rm -v $(OBJECTS) $(DEPENDENCIES) $(EXECUTABLE)

$(EXECUTABLE): $(OBJECTS)
	$(LINK) -o$@ $^

%.o : %.cxx
	$(COMPILE) -o $@ $<

