HS=ghc
HSFLAGS=--make -fwarn-incomplete-patterns

all: solution

solution: solution.hs
	$(HS) $(HFLAGS) $^

clean:
	@rm -rf solution solution.hi solution.o

.PHONY: all clean
