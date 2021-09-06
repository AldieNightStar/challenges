# Task:
# - Find a middle letter in string
#    - if no letter, return ""
#    - example:
# 	     middle("abc") should return "b"

def middle(s: str) -> str:
	size = len(s)
	if size < 3:
		return ""
	if not size % 2 == 0:
		size -= 1
	mid = int(size / 2)
	return s[mid]

def show(s: str):
	print("Original:", s)
	print("Mid Let :", middle(s))

show("Hello")
show("abc")
show("xyz")
show("TIZ")
show("987")

