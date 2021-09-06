from typing import Dict, List

ARR = [1, 7, 9, 2, 4, 2, 7, 3, 5, 3, 4, 9, 10, 4, 9, 21]

# Task
# - Sort the array in 1,2,3 order
# - Find number which has no duplicates

def sort(arr: List[int]):
	for i in range(len(arr)):
		for j in range(len(arr)):
			a = arr[i]
			b = arr[j]
			if a < b: # TODO check order
				arr[i] = b
				arr[j] = a

def dups(arr: List[int]):
	map = {}
	for i in range(len(arr)):
		n = arr[i]
		mapn = map.get(n)
		if mapn == None:
			mapn = 0
		map[n] = mapn + 1
	return map

def find_no_dups(arr: List[int]):
	map = dups(arr)
	noDups = []
	for k in map.keys():
		v = map[k]
		if v == 1:
			noDups.append(k)
	return noDups

print("Original:\t", ARR)
print("Sorted & NoDups:", find_no_dups(ARR))