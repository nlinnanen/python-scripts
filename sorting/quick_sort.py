import random
import time

# implements quick sort in a way

length=10**6

arr = [i for i in range(length)]
random.shuffle(arr)

startTime = time.time()
result = []
n = 1

def halve(lst):
	avg = sum(lst)/len(lst)
	if len(lst)==2 and lst[0] == lst[1] :
		return [[lst[0]], [lst[1]]]
	halves = [[], []]
	for i in lst:
		if i > avg:
			halves[1].append(i)
		else:
			halves[0].append(i)

	return halves


def sort(lst):
	parts = halve(lst)
	return sort(parts[0]) + sort(parts[1]) if len(lst)>2 else parts[0]+parts[1]

result = list(sort(arr))
executionTime = (time.time() - startTime)
print('\nExecution time in seconds: ' + str(executionTime))
print(f"Wrong order on numbers: {[e for i, e in enumerate(sorted(arr)) if e!=result[i]]}")
