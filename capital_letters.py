# Task:
# - Find indexes of capital letters in a string

def capitals(s: str):
	arr = []
	for i in range(len(s)):
		if not s[i].islower():
			arr.append(i)
	return arr

def show(text):
	print("Original:", text)
	print("Capitals:", capitals(text))
	print("")

show("Hello World!")
show("Hi Sir AND all")
show("hellO")
show("This is COOL")