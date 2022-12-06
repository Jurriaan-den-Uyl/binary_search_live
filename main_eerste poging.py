# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 14:25:25 2022

@author: Mehr

Binary search tree
"""

import random
import time

start_time = time.process_time()

def search(list,number):
	j = len(list)//2
# 	print(j)
	list_A = list[:j]
	list_B = list[j:]
	if number in list_A:
		return list_A
		print(list_A)
	else:
		return list_B
		print(list_B)

step = 1
i = 0
j = 1000
j = j+step
numbers = list(range(i,j,step))

shuffled_numbers = []

while numbers:
	x = random.choice(numbers)
	numbers.remove(x)
	shuffled_numbers.append(x)

while len(shuffled_numbers) != 1:
	shuffled_numbers = search(shuffled_numbers,10)
# 	time.sleep(1)
	print(shuffled_numbers)
print("--- %s seconds ---" % (time.process_time() - start_time))