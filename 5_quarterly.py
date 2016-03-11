# from collections import deque

# def answer(L, k):
# 	# your code here
# 	# the list of deques and their sums perspectively
# 	dqs, sums = [deque([L[0]])], [L[0]]
# 	ret = L[0]
# 	# create k deques and keep them aligned
# 	for i in xrange(1, k):
# 		new_dq = deque(list(dqs[-1]))
# 		new_dq.append(L[i])
# 		dqs.append(new_dq)
# 		sums.append(sums[-1] + L[i])
# 		if sums[-1] > ret: ret = sums[-1]
# 		# update existing deques
# 		for j in xrange(len(dqs)-1):
# 			sums[j] = sums[j] - dqs[j].popleft() + L[i]
# 			dqs[j].append(L[i])
# 			if sums[j] > ret: ret = sums[j]
	
# 	for i in xrange(k, len(L)):
# 		for j in xrange(len(dqs)):
# 			sums[j] = sums[j] - dqs[j].popleft() + L[i]
# 			dqs[j].append(L[i])
# 			if sums[j] > ret: ret = sums[j]

# 	return ret


# previous solution use k deques. O(nk) time, O(k^2) space. Exceeds time limit.
# record the current window in a class to avoid duplicate calculation

class Accumulator:
	def __init__(self, val = None):
		if val is not None:
			self._sum = val
			self._list = [val]
		else:
			self._sum = 0
			self._list = []

	def __len__(self):
		return len(self._list)

	def append(self, val):
		self._sum += val
		self._list.append(val)

	def extend(self, obj):
		self._sum += obj._sum
		self._list.extend(obj._list)

	def sum(self):
		return self._sum


def answer(L, k):
	ret = None

	for i in xrange(len(L)):
		if L[i] < 0:
			# in case all negatives
			ret = max(ret, L[i])
			continue

		window = Accumulator()
		j = i
		while j < len(L) and len(window) < k:
			if L[j] >= 0:
				window.append(L[j])
				ret = max(ret, window.sum())

			else:
				negative = Accumulator(L[j])
				while j+1 < len(L) and L[j+1] < 0:
					negative.append(L[j+1])
					j += 1
					if len(window) + len(negative) == k:
						break
				if window.sum() + negative.sum() < 0:
					break
				window.extend(negative)

			j += 1

	return ret

assert(answer([-100, 95, 86, 47], 3) == 228)
assert(answer([40, 91, -68, -36, 24, -67, -32, -23, -33, -52], 7) == 131)
assert(answer([8, -1, -2, -1, 0], 4) == 8)
