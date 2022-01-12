import random

# Sorts an array by randomizing the order and chekcing if it is in order
# Utterly useless and rediculously slow

arr = []
for i in range(10):
	arr.append(i)

random.shuffle(arr)
print(arr)
print("\n\n")

n = 1

sorted = False
while not sorted:
	random.shuffle(arr)
	sorted = True
	print(arr)
	for i in range(len(arr) - 1):
		print(n)
		n += 1
		if arr[i]>arr[i+1]:
			sorted = False

print(arr)
print(f"Wrong order on numbers: {[e for i, e in enumerate(sorted(arr)) if e!=result[i]]}")
