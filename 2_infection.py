
def answer(population, x, y, strength):
	if y in range(len(population)) and x in range(len(population[0])):
		if -1 < population[y][x] and population[y][x] <= strength:
			population[y][x] = -1
			answer(population, x-1, y, strength)
			answer(population, x+1, y, strength)
			answer(population, x, y-1, strength)
			answer(population, x, y+1, strength)
	return population


input = [[6, 7, 2, 7, 6], [6, 3, 1, 4, 7], [0, 2, 4, 1, 10], [8, 1, 1, 4, 9], [8, 7, 4, 9, 9]]
output = [[6, 7, -1, 7, 6], [6, -1, -1, -1, 7], [-1, -1, -1, -1, 10], [8, -1, -1, -1, 9], [8, 7, -1, 9, 9]]
assert answer(input, 2, 1, 10) == output