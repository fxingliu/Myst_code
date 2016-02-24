# from collections import deque

# def answer(t, n):
# 	# your code here
# 	flex = t-n+1
# 	if flex < 0: return 0
# 	if flex == 0: return 1
# 	strategy = gen_strat(n, flex)
# 	solution = 0

# 	for back, stay in strategy:
# 		slot = n-2
# 		solution_back = gen_back(back, slot)
# 		step = n-1+back*2
# 		solution_stay = gen_stay(step, stay)
# 		solution += solution_back * solution_stay

# 	return solution % 123454321

# # generate the pair of (back, stay)
# def gen_strat(n, flex):
# 	if n == 2:
# 		return [(0, flex)]
# 	strat = []
# 	for i in xrange(flex/2+1):
# 		strat.append((i, flex-2*i))
# 	return strat

# # generate C(step+stay, stay)
# def gen_stay(step, stay):
# 	ret = 1
# 	step += stay
# 	for i in xrange(stay):
# 		ret *= step-i
# 	for i in xrange(stay):
# 		ret /= i+1
# 	return ret

# # generate all the combination of back
# def gen_back2(back, slot):
# 	if slot == 0:
# 		return 1
# 	# start, step, count
# 	w = [0, 0, 0]
# 	helper(back, slot, slot+back*2, w)
# 	return w[2]

# # the helper function of gen_back
# def helper(back, slot, total_step, wrapper):
# 	if wrapper[1] == total_step:
# 		if wrapper[0] == slot:
# 			wrapper[2] += 1
# 		return
# 	if wrapper[0] > 0 and back > 0:
# 		# try back
# 		back -= 1
# 		wrapper[0] -= 1
# 		wrapper[1] += 1
# 		helper(back, slot, total_step, wrapper)
# 		wrapper[1] -= 1
# 		wrapper[0] += 1
# 		back += 1

# 	if wrapper[0] < slot:
# 		# try forward
# 		wrapper[0] += 1
# 		wrapper[1] += 1
# 		helper(back, slot, total_step, wrapper)
# 		wrapper[1] -= 1
# 		wrapper[0] -= 1

# def gen_back(back, slot):
# 	if slot == 0:
# 		return 1
# 	move = [1] * (back + slot)
# 	total_move = deque([move])
# 	while len(total_move[0]) < 2*back + slot:
# 		cur = total_move.popleft()
# 		for x in xrange(1, len(cur)):
# 			copy = [i for i in cur]
# 			copy.insert(x, -1)
# 			total_move.append(copy)
# 	count = 0
# 	unique_move = [list(x) for x in set(tuple(x) for x in total_move)]
# 	for cur in unique_move:
# 		sum = 0
# 		for i in xrange(len(cur)):
# 			sum += cur[i]
# 			if sum < 0 or sum > slot:
# 				break
# 		else:
# 			count += 1
# 			# print cur
# 	return count


# the above two solutions both exceed time / space limit
# here is DP solution:



def answer(t, n):
	# your code here
	if t-n+1 < 0: return 0
	if t-n+1 == 0: return 1
	if n == 2: return t

	mod = 123454321
	cur, prev = [0]*n, [0]*n
	cur[0] = 1
	for i in xrange(t):
		prev, cur = cur, prev
		cur[0] = (prev[0] + prev[1]) % mod
		cur[-1] = (prev[-2] + prev[-1]) % mod
		cur[-2] = (prev[-3] + prev[-2]) % mod
		for j in xrange(1, n-2):
			cur[j] = (prev[j-1] + prev[j] + prev[j+1]) % mod

	return cur[-1]

 
# assert(gen_strat(3, 1) == [(0,1)])
# assert(gen_strat(3, 2) == [(0,2), (1,0)])
# assert(gen_strat(2, 2) == [(0,2)])

# assert(gen_back(2, 2) == 4)
# assert(gen_back(2, 3) == 8)
# assert(gen_back(2, 4) == 13)
# assert(gen_back(2, 5) == 19)
# assert(gen_back(3, 2) == 8)
# assert(gen_back(3, 3) == 21)

# assert(gen_stay(1, 2) == 3)
# assert(gen_stay(2, 3) == 10)
# assert(gen_stay(6, 0) == 1)

assert(answer(1, 2) == 1)
assert(answer(3, 2) == 3)
assert(answer(10, 2) == 10)
assert(answer(6, 4) == 32)
assert(answer(6, 3) == 31)
assert(answer(5, 4) == 12)
