import random

# implements bubble sort

arr = []
for i in range(1000):
	arr.append(i)

random.shuffle(arr)
print(arr)
print("\n\n")

n = 1

while True:
	sorted = True
	print(arr)
	for i in range(len(arr) - 1):
		print(n)
		n += 1
		if arr[i]>arr[i+1]:
			sorted = False
			x, y = arr[i+1], arr[i]
			arr[i], arr[i+1] = x, y
	if sorted:
		break

print(arr)