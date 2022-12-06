# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 16:23:07 2022

@author: Mehr

Binary search tree 3rd try
"""
#importing
import random
import time

#function to check the amount of time elapsed
start_time = time.process_time()

#variables. number is the number to be found.
list_length = 100000
number = 250
random_list = random.sample(range(200000), list_length)
index = 0

sorted_list = [(idx, item) for idx,item in enumerate(random_list)]
sorted_list.sort(key=lambda x: x[1])


while True:
	#j variable to pinpoint the middle of the list
	j = len(sorted_list)//2
	
	#a separate check from the mainloop to check if the number is at position j
	if number == sorted_list[j][1]:
		print(f"--- found at index {random_list.index(number)} of original list ---")
		break
	
	#separate the list into two halves
	list_A = sorted_list[:j]
	list_B = sorted_list[j:]

	#first check if there is only one item left in list. If so, end program because the program would have ended
	#already at the first check
	if len(sorted_list) == 1:
		print("your number is not in the list ")
		break
	
	#check if number is smaller than first entry in list_B. If so, number must be in list A.
	elif number <= list_B[0][1]:
		sorted_list = list_A
#		print(list_A)
	
	#check if number is larger than the larger item in list A, if so number must be in list B.
	elif number >= list_A[j-1][1]:
		sorted_list = list_B
#		print(list_B)

#second part of the time checking function
print("--- %s seconds ---" % (time.process_time() - start_time))