# Decorator @repeat(5)
def repeat(n):
	def decorator(fn):
		def wrapper(*a, **k):
			for _ in range(n):
				sq = fn(*a, **k)
				for j in sq:
					yield j
		return wrapper
	return decorator

# Decorator @infinite
def infinite(fn):
	def wrapper(*a, **k):
		while True:
			sq = fn(*a, **k)
			for i in sq:
				yield i
	return wrapper

@repeat(10)
def numbers(n):
	for i in range(n):
		yield i

@infinite
def numbers2(n):
	for i in range(n):
		yield i

for i in numbers(1):
	print(i)

print("---")

cnt = 0
for i in numbers2(3):
	print(i)
	cnt += 1
	if cnt > 10:
		break
