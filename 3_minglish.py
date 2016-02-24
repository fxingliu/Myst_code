# def answer(words):
# 	# your code here
# 	dependency = []
# 	get_dep(words, dependency)

# 	in_degree = {}
# 	for (i, j) in dependency:
# 		if i not in in_degree:
# 			in_degree[i] = 0
# 		in_degree[j] = in_degree.get(j, 0) + 1

# 	ret = ''
# 	queue = [key for key in in_degree if in_degree[key] == 0]
# 	while len(queue) > 0:
# 		cur = queue.pop(0)
# 		ret += cur
# 		for (i, j) in dependency:
# 			if i == cur: 
# 				in_degree[j] -= 1
# 				if in_degree[j] == 0:
# 					queue.append(j)
# 	return ret


# there is a bug in the code above:
# 	consider input as ['a', 'a'], there is no dependency, so in_degree is empty

def answer(words):
	# your code here
	dependency = []
	get_dep(words, dependency)

	in_degree = {}
	for (i, j) in dependency:
		in_degree[j] = in_degree.get(j, 0) + 1
	for s in words:
		for c in s:
			if c not in in_degree:
				in_degree[c] = 0

	ret = ''
	queue = [key for key in in_degree if in_degree[key] == 0]
	while len(queue) > 0:
		cur = queue.pop(0)
		ret += cur
		for (i, j) in dependency:
			if i == cur: 
				in_degree[j] -= 1
				if in_degree[j] == 0:
					queue.append(j)
	return ret


def get_dep(words, dependency):
	if len(words) == 0: return
	i, j = 0, 0
	while j < len(words):
		if words[i][0] == words[j][0]:
			j += 1
		else:
			dependency.append((words[i][0], words[j][0]))
			new_words = [words[k][1:] for k in xrange(i, j) if len(words[k]) > 1]
			get_dep(new_words, dependency)
			i = j
	new_words = [words[k][1:] for k in xrange(i, j) if len(words[k]) > 1]
	get_dep(new_words, dependency)


words = ['z', 'yz', 'yxy', 'yxx', 'yu']
print answer(words)
assert(answer(["y", "z", "xy"]) == "yzx")
assert(answer(["ba", "ab", "cb"]) == "bac")
words = ['a', 'a']
print answer(words)