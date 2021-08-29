# Settings
# --------------
COUNT = 4
SIZE  = 10
SYM   = "*"
# --------------

def main():
	xprint = lambda s: print(s, end="")
	chrisTree(SIZE, COUNT, xprint, SYM, "\n")

def chrisTree(n: int, cnt: int, f_print=print, sym="*", nextLineSym="\n"):
	for j in range(cnt):
		for i in range(n):
			spaces = " " * (n-i)
			draws = sym * (1 + (i * 2))
			f_print(spaces)
			f_print(draws)
			f_print(nextLineSym)

if __name__ == "__main__":
	main()