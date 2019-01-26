

bin_arr = []

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
	for i in range(5 - len(bin1_str)):
		bin1_str = '0' + bin1_str
	return to_int(bin1_str)

for pos_num in range(3):
	if pos_num == 1:
		bin_arr.append([[1,1,1,1,1], [0,0,0,0,0], [0,0,0,0,0]])

	elif pos_num == 2:
		for bin1 in range(16):
			bin1_arr = dec2bin_arr(bin1)
			bin2_arr = reverse_arr(bin1_arr)
			bin_arr.append([bin1_arr, bin2_arr, [0,0,0,0,0]])

	elif pos_num == 3:
		for bin1 in range(16):
			

print(bin_arr)