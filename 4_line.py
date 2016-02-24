# def answer(x, y, n):
# 	# your code here
# 	permutation = generate_permutation(range(n))
# 	count = 0
# 	for p in permutation:
# 		if check(p, True) == x and check(p, False) == y:
# 			count += 1
# 	return str(count)

# def generate_permutation(num):
# 	ret = []
# 	dfs(num, 0, ret)
# 	return ret

# def dfs(num, pos, ret):
# 	if pos == len(num):
# 		new_list = list(num)
# 		ret.append(new_list)
# 		return
# 	for i in xrange(pos, len(num)):
# 		num[i], num[pos] = num[pos], num[i]
# 		dfs(num, pos+1, ret)
# 		num[i], num[pos] = num[pos], num[i]

# def check(num, left):
# 	# reverse doesn't matter
# 	if not left: num.reverse()
# 	count, last = 0, -1
# 	for i in num:
# 		if i > last:
# 			count += 1
# 			last = i
# 		if i == len(num)-1:
# 			break
# 	return count
	
# the brute-force solution will exceed space limit
# use DP & memoization


def answer(x, y, n):
	# your code here
	factorial = gen_factorial(n)
	dp = {}
	return str(arrange(n-1, x+y-2, dp, factorial) * combination(x+y-2, x-1, factorial))

def gen_factorial(n):
	factorial = [1]
	for i in xrange(1, n+1):
		factorial.append(factorial[-1] * i)
	return factorial

# return C(n, k)
def combination(n, k, factorial):
	return factorial[n] / factorial[k] / factorial[n-k]

# return the number of arrangements of n rabbits where k of them are visible from one side
def arrange(n, k, dp, factorial):
	if k > n: return 0
	if k == n: return 1
	if k == n-1: return combination(n ,2, factorial)
	if k == 1: return factorial[n-1]
	if k == 0: return 0

	if (n, k) not in dp:
		dp[(n, k)] = arrange(n-1, k-1, dp, factorial) + arrange(n-1, k, dp, factorial) * (n-1)
	return dp[(n, k)]


assert(answer(2, 2, 3) == '2')
assert(answer(1, 2, 6) == '24')
