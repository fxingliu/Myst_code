
def answer(n):
	# your code here
	if int(n**.5)**2 == n:
		return 1
	square = [i**2 for i in xrange(1, int(n**.5)+1)]
	ind = 0
	dp = [i for i in xrange(n+1)]
	for i in square:
		dp[i] = 1
	for i in xrange(1, n+1):
		if dp[i] == 1:
			ind += 1
			continue
		for j in xrange(ind):
			dp[i] = min(dp[i], dp[i-square[j]]+1)
	return dp[n]

assert(answer(1) == 1)
assert(answer(9) == 1)
assert(answer(2) == 2)
assert(answer(5) == 2)
assert(answer(24) == 3)
assert(answer(160) == 2)
