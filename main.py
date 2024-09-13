import math

import map


# Returns a list with the neighbors of the cell at (row, col), rows and cols
# are the dimenssions of the matrix
def neighbors(rows, cols, row, col):
	neig = []
	if row - 1 >= 0:
		neig.append((row - 1, col))
	if col - 1 >= 0:
		neig.append((row, col-1))
	if row + 1 < rows:
		neig.append((row + 1, col))
	if col + 1 < cols:
		neig.append((row, col + 1))
	return neig

# Prints the matrix in a matrix format (makig it easy to identify columns)
def printNicely(matrix):
	print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))

def tellDirections(sol):
	print(f'Starting at {sol[0]}')
	current = sol[0]
	for i in range(1, len(sol)):
		print(i)
		if current == sol[i]:
			print('New goal')
		elif current[0] == sol[i][0]:
			if current[1] + 1 == sol[i][1]:
				print('Move right')
			elif current[1] - 1 == sol[i][1]:
				print('Move left')
			else:
				print("Error in row")
		elif current[1] == sol[i][1]:
			if current[0] + 1 == sol[i][0]:
				print('Move down')
			elif current[0] - 1 == sol[i][0]:
				print('Move up')
			else:
				print("Error in column")
		else:
			print('Error somewhere', current, sol[i])
		current = sol[i]


# The matrix is the map with the weights, start and goal are touples with their coordinates
def dijkstra(matrix, start, goal):
	rows, cols = len(matrix), len(matrix[0])
	data = []
	visited = []
	unvisited = []
	for i in range(rows):
		for j in range(cols):
			data.append([(i, j), math.inf, None])
			unvisited.append((i, j))
	data[start[0] * cols + start[1]][1] = 0

	current = start
	while len(unvisited) > 1:
		neig = neighbors(rows, cols, current[0], current[1])
		for n in neig:
			if data[n[0] * cols + n[1]][1] > data[current[0] * cols + current[1]][1] + matrix[n[0]][n[1]]:
				data[n[0] * cols + n[1]][1] = data[current[0] * cols + current[1]][1] + matrix[n[0]][n[1]]
				data[n[0] * cols + n[1]][2] = current
		visited.append(current)
		unvisited.remove(current)
		if current == goal:
			break
		aux = [x for x in data if x[0] in unvisited]
		aux.sort(key=lambda x: x[1])
		# print(aux)
		current = aux[0][0]
	# print(data)
	# print(f'cost = {data[goal[0] * cols + goal[1]][1]}')
	# print('path...')
	current = goal
	inv_sol = []

	while data[current[0] * cols + current[1]][2]:
		inv_sol.append(current)
		matrix[current[0]][current[1]] = 5
		current = data[current[0] * cols + current[1]][2]
	inv_sol.append(start)
	sol = inv_sol[::-1]
	# for s in sol:
	# 	print(data[s[0] * cols + s[1]])
	# print(sol)
	# We return the cost and the solution path
	return data[goal[0] * cols + goal[1]][1] + matrix[goal[0]][goal[1]], sol

# dijkstraPath uses Dijkstra between one goal and the next one
def dijkstraPath(matrix, start, goals):
	cost = 0
	path = []
	new_matrix = [row[:] for row in matrix]
	new_start = start 
	new_goal = goals[0]
	for goal in goals:
		new_cost, new_path = dijkstra(new_matrix, new_start, goal)
		new_start = goal
		cost += new_cost
		path += new_path
	# print(f'The path is {path}')
	print(f'The cost is {cost}')
	print(f'The directions are...')
	tellDirections(path)
	return cost, path




matrix = [[1, 3, 5, 8], [4, 2, 1, 7], [4, 3, 2, 3]]
start = (0, 0)
goal = (2, 3)
# dijkstra(matrix, goal, start)

start = (7, 7) # The tutorial makes you move 2 to the right
goal = (5, 11)
# dijkstra(map.fog_map, start, goal)

goals = [(5, 11), (4, 10), (3, 9), (2, 8), (1, 12), (2, 13), (9, 13), 
	(13, 12), (13, 7), (10, 3), (10, 0), (8, 1), (5, 2), (5, 0), (3, 3), (0, 4), (0, 0)]

goals2 = [(12, 9), (11, 11), (9, 13), (13, 12), (13, 7), (14, 8), (12, 4), (10, 3),
	(10, 0), (8, 0), (8, 1), (5, 0), (5, 2), (3, 0), (0, 0), (0, 4), (0, 7), (2, 8),
	(3, 9), (3, 11), (2, 13), (1, 14), (1, 12)]
dijkstraPath(map.fog_map, start, goals)



