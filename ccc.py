import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d  import Axes3D

INFTY = 0


figure = plt.figure()
ax = Axes3D(figure)

request_array = [
			[1, 0, 1],
			[2, 1, 0],
			[1, 1, 0],
			[2, 1, 2],
			[1, 0, 0] ]

bay_cap = [
		[0, 3, 0],
		[1, 2, 0],
		[0, 2, 1],
		[0, 4, 0],
]


def if_able(bay_id, transp_arr):
	if bay_id == 1:
		if sum(transp_arr) <= 2:
			return True
		else:
			if transp_arr in  bay_cap:
				return True
			else:
				return false
	elif bay_id == 2:
		return True

position_array = [
	[191.4818457,	57.79130153],\
	[151.7214303,	45.84776588],\
	[147.1751812,	70.12011252],\
	[137.6974078,	65.72797360],\
	[77.51739912,	73.35642541] ]
def dist_from(from_pnt, to_pnt_ind):
	x_sq = pow((from_pnt[0] - position_array[to_pnt_ind][0]), 2)
	y_sq = pow((from_pnt[1] - position_array[to_pnt_ind][1]), 2)
	dist = np.sqrt(x_sq + y_sq)
	return dist


pnt_req = [1, 1, 0, 1, 0]

grid_dens = 0.1
x_plot = np.arange(145, 180, grid_dens)
y_plot = np.arange(35, 82, grid_dens)

X, Y = np.meshgrid(x_plot, y_plot)

max_dist = 79 * 40 / 60

min_pos_x = INFTY
min_pos_y = INFTY
min_weight = 65536



z_plot = []
for x in x_plot:
	z_l = []
	for y in y_plot:
		from_pnt = (x, y)
		# cost = INFTY
		if(dist_from(from_pnt, 0) > max_dist or dist_from(from_pnt, 1) > max_dist or dist_from(from_pnt, 3) > max_dist):
			cost = 0
		else:
			cost = 100 * max(dist_from(from_pnt, 0) / 79, dist_from(from_pnt, 1) / 79, dist_from(from_pnt, 3) / 79)
		z_l.append(cost)
		if not (cost == 0 or cost == INFTY):
			if cost < min_weight:
				min_pos_y = y
				min_pos_x = x
				min_weight = cost

	z_plot.append(z_l)

Z = np.transpose(np.array(z_plot))
print("x = %f, y = %f" % (min_pos_x, min_pos_y))
print("cost = %f" % min_weight)
print(X.shape)
print(Y.shape)
# print(Z.shape)
ax.plot_surface(X, Y, Z, cmap = 'rainbow')
plt.show() 