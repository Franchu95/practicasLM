#!/usr/bin/env python
#-*- coding: utf-8 -*-

def funimpar(li2):
	lif=[]
	impar=False
	for ele in li2:
		if impar:
			lif.append(ele)
		impar=not impar
	return lif
			
		
		
	
