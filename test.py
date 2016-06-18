#!/usr/bin/env python
#-*- coding:utf-8 -*-
import math
def findprime(num):
	isprime = "True"	
	i=2
	while i< (num+1):
		c=int(math.sqrt(i))
		j=2
		while j<=c:

			if i%j == 0:
				isprime="False"
				break

			j=j+1

		if isprime == "True":
			print i
 		
		isprime = "True"
		i=i+1

num=int(raw_input('please input a number:'))
findprime(num)
	
