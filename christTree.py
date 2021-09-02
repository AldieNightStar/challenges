# Settings
# --------------
COUNT = 3
SIZE  = 15
SYM   = "*"

SPEC  = True
RAND  = True
SPECS = "#$@!*&oPZ#"
# --------------

from random import randint


def symProviderDefault(n):
	return SYM

def symProviderSpecial(n):
	return SPECS[n%len(SPECS)]

def main():
	xprint = lambda s: print(s, end="")
	# Special symbols
	symP = symProviderDefault
	if SPEC:
		symP = symProviderSpecial
	# ---
	chrisTree(SIZE, COUNT, xprint, symP, "\n")

def chrisTree(n: int, cnt: int, f_print=print, symProvider=symProviderDefault, nextLineSym="\n"):
	for j in range(cnt):
		for i in range(n):
			spaces = " " * (n-i)
			# ---
			drawsCnt = 1 + (i * 2)
			drawsArr = []
			for i in range(drawsCnt):
				if RAND:
					drawsArr.append(symProvider(randint(0, drawsCnt)))
				else:
					drawsArr.append(symProvider(i))
			# ---
			f_print(spaces)
			f_print("".join(drawsArr))
			f_print(nextLineSym)

if __name__ == "__main__":
	main()