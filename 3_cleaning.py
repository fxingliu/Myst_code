import time

# def answer(chunk, word):
# 	# your code here
# 	candidate = []
# 	helper(chunk, word, candidate)
# 	min_len = min([len(c) for c in candidate])
# 	candidate = sorted([c for c in candidate if len(c) == min_len])
# 	return candidate[0]

# def helper(chunk, word, candidate):
# 	ind = [i for i in xrange(len(chunk)-len(word)+1) if chunk.startswith(word, i)]
# 	if len(ind) == 0:
# 		candidate.append(chunk)
# 		return
# 	for i in ind:
# 		sub_chunk = chunk[:i] + chunk[i+len(word):]
# 		helper(sub_chunk, word, candidate)

# above solution will exceed time limit


from collections import deque

def answer(chunk, word):
	# your code here
	queue = deque([chunk])
	all_ans = set()
	min_ans = chunk

	while len(queue):
		cur = queue.popleft()
		ind = [i for i in xrange(len(cur)-len(word)+1) if cur.startswith(word, i)]
		for i in ind:
			next = cur[:i] + cur[i+len(word):]
			if next in all_ans:
				continue
			all_ans.add(next)
			if len(next) < len(min_ans):
				min_ans = next
			elif len(next) == len(min_ans) and next < min_ans:
				min_ans = next
			queue.append(next)

	return min_ans



start_time = time.time()
assert(answer('lololololo', 'lol') == 'looo')
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
assert(answer('aabb', 'ab') == '')
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
assert(answer('goodgooogoogfogoood', 'goo') == 'dogfood')
print("--- %s seconds ---" % (time.time() - start_time))
