#!/usr/bin/env python

import sys,os
def wordcount(path):
	f=open(path,"r")
	lines=f.readlines()[0].replace('.','').replace(',','').split()
	lines.uniq=list(set(lines))
	
	for line in lines_uniq:
		print lines.count(line),line

path=sys.path[0]
path=path+"/test.log"
wordcount(path)	