import numpy as np

INFTY = 65535

drone_array = [
	['F', 2, 22, 79, 24],
	['B', 1, 8, 79, 40],
	['G', 2, 20, 64, 16],
	['C', 2, 14, 64, 35],
	['E', 2, 15, 60, 15],
	['D', 1, 11, 60, 18],
	['A', 1, 3.5, 40, 35]]

position_array = [
	[209.3,	63.2],\
	[165.6,	50.0],\
	[160.6,	76.6],\
	[150.4,	71.9],\
	[84.7,	80.3] ]
drain_ratio = 0.9


def dist_from(from_pnt, to_pnt_ind):
	x_sq = pow((from_pnt[0] - position_array[to_pnt_ind][0]), 2)
	y_sq = pow((from_pnt[1] - position_array[to_pnt_ind][1]), 2)
	dist = np.sqrt(x_sq + y_sq)
	return dist
					#[1,1], 1				(x, y)
def get_cost_contrib(fleet, hospital_index, iter_position):
	cost = []
	for i in range(len(fleet)):
		drone_index = fleet[i]
		distance = dist_from(iter_position, hospital_index)
		capacity = drain_ratio * drone_array[drone_index][3] * drone_array[drone_index][4] / 60
		if distance < capacity:
			cost.append(distance / (drone_array[drone_index][3]))
		else:
			cost.append(INFTY)
	ret = 0
	if len(cost) > 0:
		ret = max(cost)
	return ret

#[[], [7], [], [1], [6]]
def get_cost_single_supply(fleetModeGroup):
	
	grid_dens = 10
	x_range = np.arange(0, 300, grid_dens)
	y_range = np.arange(20, 82, grid_dens)

	X, Y = np.meshgrid(x_range, y_range)
	
	weight = 65535
	min_cost = 65536
	min_x = 0
	min_y = 0
	

	z_plot = []
	for x in x_range:
		z_l = []
		for y in y_range:
			cur_cost = max(get_cost_contrib(fleetModeGroup[0], 0, (x, y)),  \
							get_cost_contrib(fleetModeGroup[1], 1, (x, y)), \
							get_cost_contrib(fleetModeGroup[2], 2, (x, y)), \
							get_cost_contrib(fleetModeGroup[3], 3, (x, y)), \
							get_cost_contrib(fleetModeGroup[4], 4, (x, y)))
			z_l.append(cur_cost)
			if cur_cost < min_cost:
				min_x = x
				min_y = y
				min_cost = cur_cost
		z_plot.append(z_l)
	Z = np.transpose(np.array(z_plot))
	# print(min_x)
	# print(min_y)
	# print(min_cost)

	return (min_x, min_y, min_cost)

if __name__ == '__main__':
	print(get_cost_single_supply([[0], [], [], [], [1]]))
