import drug_distr
from cost_calc import *

drone_array = [
	['F', 2, 22, 79, 24],
	['B', 1, 8, 79, 40],
	['C', 2, 14, 64, 35],
	['G', 2, 20, 64, 16],
	['D', 1, 11, 60, 18],
	['E', 2, 15, 60, 15],
	['A', 1, 3.5, 40, 35]]

# med_belong_hospital =	[0,0,1,1,1,2,2,3,3,3,3,3,4]
med_belong_hosp_dic = {0: [0, 1], 1: [2, 3, 4], 2: [5, 6], 3: [7, 8, 9, 10, 11], 4: [12]}
med_type = [0, 2, 0, 0, 1, 0, 1, 0, 0, 1, 2, 2, 0]

print("Generating distribution list")
drug_distr_list = drug_distr.get_list_of_drug_distribution_to_each_supply_station()
# drug_distr_list = [
# 					[[0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,1], [0,0,0,0,0,0,0,0,0,0,0,0,0]],
# 					[[1,1,1,1,0,0,0,1,1,1,1,1,1], [0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,1,1,1,0,0,0,0,0,0]],
# 					[[1,1,0,1,0,0,0,1,1,1,1,1,0], [0,0,1,0,0,0,0,0,0,0,0,0,1], [0,0,0,0,1,1,1,0,0,0,0,0,0]],
# 					[[0,0,1,1,0,0,0,1,1,1,1,1,0], [1,1,0,0,0,0,0,0,0,0,0,0,1], [0,0,0,0,1,1,1,0,0,0,0,0,0]]
# 				  ]
'''
Considering the worst situation where a group
of drones are going to deliver packages to
Puerto Rico Children's Hospital in Bayamon,
there are only a maximum of 5 packages to be delivered.
Using the drone that can carry the least,
2 drones will be enough.
'''
supply_station_exp = [0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0]

drone_fleet_list = []
for i in range(7):
	if not i == 0:
		drone_fleet_list.append([i, ])
	for j in range(7-i):
		if not (drone_array[i][1] == 2 or drone_array[j+i][1] == 2):
			drone_fleet_list.append([i, j])
drone_fleet_list = [[],[1], [1, 0], [1,1], [2],[3],[4],[4,0],[5],[6]]
print(drone_fleet_list)

print("---------------------------------------Drone fleet possibilities established-----------------------------------")

def get_hospital_list(supply_station):
	ret = []
	
	for hospital in range(5):
		hospital_request_list = [0,0,0]
		hospital_drug_index_list = med_belong_hosp_dic[hospital]
		
		for drug_index in hospital_drug_index_list:
			if supply_station[drug_index] == 1:
				drug_type = med_type[drug_index]
				hospital_request_list[drug_type] += 1
		ret.append(hospital_request_list)
	return ret
# print(get_hospital_list)


def check_not_overload(med_array, drone_ind):
	if sum(med_array) == 0:
		return True
	else:
		if len(drone_ind) == 0:
			return False
		else:
			weight = med_array[0] * 2 + med_array[1] * 2 + med_array[2] * 3
			not_over_weight = weight <= drone_array[drone_ind[0]][2] * len(drone_ind)
			not_over_size = False
			if drone_array[drone_ind[0]][1] == 2:
				not_over_size = True
			else:
				if sum(med_array) <= len(drone_ind) * 2:
					not_over_size = True
				elif med_array in [[len(drone_ind) * 0, len(drone_ind) * 3, 0], [len(drone_ind) * 1, len(drone_ind) * 2, 0],
								   [len(drone_ind) * 2, 0, len(drone_ind) * 1], [0, len(drone_ind) * 4, 0]]:
					not_over_size = True
				else:
					not_over_size = False
			return not_over_size and not_over_weight
  

def find_best_mode_for_supply(supply_station, drone_fleet_list, hospital_list):
	for fleetMode0 in drone_fleet_list:

		if not check_not_overload(hospital_list[0], fleetMode0):
			continue
		else:
			# Check Hospital 1
			for fleetMode1 in drone_fleet_list:
				if not check_not_overload(hospital_list[1], fleetMode1):
					continue
				else:
					# Check request fron Hospital 2
					for fleetMode2 in drone_fleet_list:
						if not check_not_overload(hospital_list[2], fleetMode2):
							continue
						else:
							# Check request fron Hospital 3
							for fleetMode3 in drone_fleet_list:
								if not check_not_overload(hospital_list[3], fleetMode3):
									continue
								else:
									# Check request fron Hospital 4
									for fleetMode4 in drone_fleet_list:
										if not check_not_overload(hospital_list[4], fleetMode4):
											continue
										else:
											fleetList_single_supply = [fleetMode0, fleetMode1, fleetMode2,fleetMode3, fleetMode4]
											cost_contrib = get_cost_single_supply(fleetList_single_supply)
											return (fleetList_single_supply, cost_contrib)


def get_cost_of_drug_distri(distribution):
	maximum_cost_contrib = 0
	fleet_modes = []
	cost_contrib_list = []
	for i in range(len(distribution)):
		supply_station = distribution[i]
		hospital_list = get_hospital_list(supply_station)
		if i == 1:
			print("", end = '')
		supp_info = (fleet_mode_for_supply_to_hosp, cost_contrib) = find_best_mode_for_supply(supply_station, drone_fleet_list, hospital_list)
		fleet_modes.append(fleet_mode_for_supply_to_hosp);
		supp_cost_value = cost_contrib[2]
		if supp_cost_value > maximum_cost_contrib:
			maximum_cost_contrib = supp_cost_value
		cost_contrib_list.append(cost_contrib)
	return [maximum_cost_contrib, fleet_modes, cost_contrib_list]


def main():
	min_cost = 100
	min_occasion = []
	i = 0
	for distri in drug_distr_list:
		if i % 100 == 0:
			print(i, end = ",")
		i += 1

		get_cost_of_this_distri = get_cost_of_drug_distri(distri)
		if min_cost > get_cost_of_this_distri[0]:
			min_cost = get_cost_of_this_distri[0]
			min_occasion = get_cost_of_this_distri

	print(min_occasion)

if __name__ == '__main__':
	main()
	