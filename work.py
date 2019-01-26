def get_spot_num(bin_arr_ele):
	num = 0
	for ele in bin_arr_ele:
		if not sum(ele) == 0:
			num += 1
	return num

bin_arrange = [[1,1,1,1,1,1,1,1,1,1,1,1,0], [0,0,0,0,0,0,0,0,0,0,0,0,1], [0,0,0,0,0,0,0,0,0,0,0,0,0]]

med_belong = [0,0,1,1,1,2,2,3,3,3,3,3,4]


# 'mission' is single element in bin_arange
def get_position_of_bin(mission):
	hospital_to_go = [0,0,0,0,0]
	for i in range(len(mission)):
		if mission[i] == 1:
			hospital_to_go[med_belong[i]] += 1
	return hospital_to_go


def get_arrange_opt_cost(bin_arrange):
	for bin in bin_arrange:
		pass

print(get_position_of_bin(bin_arrange[0]))