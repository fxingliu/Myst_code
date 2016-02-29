cache = {0: 1, 1: 1, 2: 2}

def get_ans(n):
	if n in cache:
		return cache[n]
	mid = n >> 1
	if n & 1:
		cache[n] = get_ans(mid) + get_ans(mid-1) + 1
	else:
		cache[n] = get_ans(mid) + get_ans(mid+1) + mid
	return cache[n]

# use binary search to reduce computation cost
# search for target over only odds or evens in [start, end]
def binary_search(start, end, target, parity):
	# print start, end, target, parity
	if start > end:
		return None
	mid = start + (end - start) / 2
	mid += parity != (mid & 1)
	ans = get_ans(mid)
	if ans == target:
		return str(mid)
	if ans > target:
		end = mid - 2
	else:
		start = mid + 2
	return binary_search(start, end, target, parity)

def answer(str_S):
	# your code here
	s = int(str_S)
	if s & 1:
		ret = binary_search(1, s, s, 1), binary_search(0, s+1, s, 0)
	else:
		ret = binary_search(1, s+1, s, 1), binary_search(0, s, s, 0)
	if not ret[0] and not ret[1]:
		return 'None'
	return ret[0] or ret[1]


assert(answer('7') == '4')
assert(answer('100') == 'None')
print answer(str(10**10))
