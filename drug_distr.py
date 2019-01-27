# This script is for generating all possiblilities of drug distribution.

import time
import sys

# All drug possibilities generated here

def reverse_arr(array):
		ret = []
		for ele in array:
			ret.append(int(not int(ele)))
		return ret

def to_int(arr):
	ret = []
	for ele in arr:
		ret.append(int(ele))
	return ret
def dec2bin_arr(bin1):
	binary = str(bin(bin1))
	bin1_str = binary[2:len(binary)]
	for i in range(13 - len(bin1_str)):
		bin1_str = '0' + bin1_str
	return to_int(bin1_str)

def bin_2_ok(bin1, bin2):
	for i in range(len(bin1)):
		ret = not (bin1[i] and bin2[i])
		if not ret:
			return False
	return ret

def getbin3(bin1, bin2):
	ret = []
	for i in range(len(bin1)):
		val = (1 - int(bin1[i]) - int(bin2[i]))
		if val < 0 or val > 1:
			print(bin1_arr, end = ',')
			print(bin2_arr, end = ',')
			print("error occur")
		ret.append(val)
	return ret

def get_spot_num(bin_arr_ele):
	num = 0
	for ele in bin_arr_ele:
		if not sum(ele) == 0:
			num += 1
	return num

request_array = [
			[1, 0, 1],
				[2, 1, 0],
				[1, 1, 0],
				[2, 1, 2],
				[1, 0, 0] ]

med_belong = [0,0,1,1,1,2,2,3,3,3,3,3,4]

med_deliverd = [1,1,1,1,1,1,1,1,1,1,1,1,1]

def get_list_of_drug_distribution_to_each_supply_station():
	bin_arr = []
	xx = 0
	bin_arr.append([med_deliverd, reverse_arr(med_deliverd), reverse_arr(med_deliverd)])
	for bin1 in range(2 ** (len(med_deliverd) - 1)):
		xx += 1
		bin1_arr = dec2bin_arr(bin1)
		if xx % 300 == 0:
			print(xx, end = ',')
			print(bin1_arr)
		for bin2 in range(2 ** (len(med_deliverd) - 1)):
			bin2_arr = dec2bin_arr(bin2)
			if (bin_2_ok(bin1_arr, bin2_arr) >= 1):
				bin3_arr = getbin3(bin1_arr, bin2_arr)
				bin_arr.append([bin1_arr, bin2_arr, bin3_arr])
	return bin_arr
	print(len(bin_arr))

if __name__ == '__main__':
	get_list_of_drug_distribution_to_each_supply_station()