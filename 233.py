import pandas as pd
import numpy as np

num_of_data_perpoint = 10
res = list()
for n in range(8):
	n = n + 1
	sum = 0
	for t in range(num_of_data_perpoint):
		t=t+1
		if t < 10:
			if n < 10:
				df_s = pd.read_table("G:/gdwlsy/Data/POINT_0000" + str(n) + "/DATA_0000" + str(t) + "_2.xls")	#read fangbo
				df_r = pd.read_table("G:/gdwlsy/Data/POINT_0000" + str(n) + "/DATA_0000" + str(t) + "_1.xls")	#read xiangying 
			else:
				df_s = pd.read_table("G:/gdwlsy/Data/POINT_000" + str(n) + "/DATA_0000" + str(t) + "_2.xls")	#read fangbo
				df_r = pd.read_table("G:/gdwlsy/Data/POINT_000" + str(n) + "/DATA_0000" + str(t) + "_1.xls")	#read xiangying 
		else:
			if n < 10:
				df_s = pd.read_table("G:/gdwlsy/Data/POINT_0000" + str(n) + "/DATA_000" + str(t) + "_2.xls")	#read fangbo
				df_r = pd.read_table("G:/gdwlsy/Data/POINT_0000" + str(n) + "/DATA_000" + str(t) + "_1.xls")	#read xiangying 
			else:
				df_s = pd.read_table("G:/gdwlsy/Data/POINT_000" + str(n) + "/DATA_000" + str(t) + "_2.xls")	#read fangbo
				df_r = pd.read_table("G:/gdwlsy/Data/POINT_000" + str(n) + "/DATA_000" + str(t) + "_1.xls")	#read xiangying 
		df_s.columns = [1,2]
		df_r.columns = [1,2]
	
	#get t_s
		t_s = 0
		for i in range(len(df_s.index)):
			if df_s[2][i] > 0:
				t_s = df_s[1][i]
				break

	#get t_e
		t_e = 0
		
		u_min = min(df_r[2])	#get minimal u
		u_1_3 = u_min / 3
		u_2_3 = u_1_3 * 2
		u_1_2 = u_min / 2
	
		dif_1_3 = abs(df_r[2] - u_1_3)
		dif_2_3 = abs(df_r[2] - u_2_3)
		
		min_dif_1_3 = min(dif_1_3)
		min_dif_2_3 = min(dif_2_3)
		
		t_1_3 = df_r[1][ list(dif_1_3).index(min_dif_1_3) ]
		t_2_3 = df_r[1][ list(dif_2_3).index(min_dif_2_3) ]

	#calculate function of line u = a*t + b

		a = ( u_1_3 - u_2_3 ) / ( t_1_3 - t_2_3 )
		b = u_1_3 - a * t_1_3
	
		t_e = ( u_1_2 - b ) / a
	
	
		delta_t = t_e - t_s
		
		sum = sum + delta_t

	res = res + [sum / num_of_data_perpoint]

print(res)
	
