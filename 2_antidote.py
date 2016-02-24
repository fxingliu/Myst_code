

def answer(meetings):
	candidate = sorted(meetings, key = lambda x : x[1])
	count = 0
	while len(candidate):
		cur = candidate[0]
		count += 1
		del candidate[0]
		candidate[:] = [x for x in candidate if not_overlap(cur, x)]
	return count


def not_overlap(a, b):
	if a[0]>=b[1] or b[0]>=a[1]: return True
	return False

	
i1 = [[0, 1], [1, 2], [2, 3], [3, 5], [4, 5]]
o1 = 4
i2 = [[0, 1000000], [42, 43], [0, 1000000], [42, 43]]
o2 = 1

assert(answer(i1) == o1)
assert(answer(i2) == o2)