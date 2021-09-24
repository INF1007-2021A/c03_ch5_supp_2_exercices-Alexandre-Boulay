#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def get_num_letters(text):
	num=0
	for char in text:
		if char.isalnum():
			num+=1
		else:
			continue
	return(num)

def get_word_length_histogram(text):
	histo = [0]
	for word in text.split():
		length= get_num_letters(word)

		if length>= len(histo):
			histo+=[0] * (length-len(histo)+1)
		if length!=0:
			histo[length]+=1
		elif length==0:
			continue



	return (histo)

def format_histogram(histogram):
	for i in range(len(histogram)):
		if i == 0:
			continue
		else:
			print(i, "*" * (histogram[i]))

def format_horizontal_histogram(histogram):
	BLOCK_CHAR = "|"
	LINE_CHAR = "¯"

	return ""


if __name__ == "__main__":
	spam = "Stop right there criminal scum! shouted the guard confidently."
	eggs = get_word_length_histogram(spam)
	print(eggs, "\n")
	print(format_histogram(eggs), "\n")
	print(format_horizontal_histogram(eggs))
