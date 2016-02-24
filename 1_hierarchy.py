def answer(x):
	last, total = 1, 1
	for i in range(x):
		last *= 7
		total += last
	return total

print answer(1)
print answer(2)
print answer(10)
