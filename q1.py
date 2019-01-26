from math import pow
from math import sqrt
# from math import 

'''			med1	med2	med3	

	CMC		1		0		1
	HH		1		0		1	
	HPS		1		1		0
	PRCH	2		1		2
	HPA		1		0		0
'''



'''
input: 飞机种类，此仓库分管运送的货物、每次可以携带的组合
output：最优位置
'''
# Global Environment
position_array = [
	[191.4818457,	57.79130153],\
	[151.7214303,	45.84776588],\
	[147.1751812,	70.12011252],\
	[137.6974078,	65.72797360],\
	[77.51739912,	73.35642541] ]
	
'''
a list of list
element:



[speed, ]
'''	


request_array = [
			[1, 0, 1],
			[2, 1, 0],
			[1, 1, 0],
			[2, 1, 2],
			[1, 0, 0] ]

class Bin:

	def __init__(self, bin_id):
		self.bin_id = bin_id
		self.pos_x = 77.51739912
		self.pos_y = 73.35642541
		self.iter = 1
		# self.drone_array
		# initialization motions

	def get_ratio(self, pnt_ind):
		delta_x_2 = (position_array[pnt_ind][0] - pos_x)
		delta_y_2 = (position_array[pnt_ind][1] - pos_y) / abs(delta_x_2)
		delta_x_2 = delta_x_2 / abs(delta_x_2)	# +-1
		return (delta_x_2, delta_y_2)

	def move(self, direction, coeff):
		if direction == 'east':
			this.pos_y += iter * coeff
		elif direction == 'south':
			this.pos_x -= iter * coeff
		elif direction == 'west':
			this.pos_y -= iter * coeff
		elif direction == 'north':
			this.pos_x += iter * coeff
		else:
			print("error occur when iter")

	def move_to_pnt_iter(self, pnt_ind):
		x_dir_coeff = (position_array[pnt_ind][0] - self.pos_x)
		y_dir_coeff = (position_array[pnt_ind][1] - self.pos_y) / abs(x_dir_coeff)
		x_dir_coeff = x_dir_coeff / abs(x_dir_coeff)	# +-1
		move('east', x_dir_coeff)
		move('north', y_dir_coeff)

	def get_weight(self):

	def dist_from(self, pnt_ind):
		x_sq = pow((self.pos_x - position_array[pnt_ind][0]), 2)
		y_sq = pow((self.pos_x - position_array[pnt_ind][1]), 2)
		dist = sqrt(x_sq + y_sq)
		return dist

	# cargo_itm: a list with a type identical to request_array[0]
	def deliver(self, pnt_ind, cargo_itm):
		for i in range(3):
			request_array[pnt_ind][i] - cargo_itm[i]
		time = self.dist_from(pnt_ind)
		return time

	def can_response_to_point(self, pnt_ind, model):




if __name__ == '__main__':
	a = Bin()



