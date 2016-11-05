#-*- encoding:utf-8 -*-
filtered_words = open('filtered_words.txt','r').read()

while True:
	input_text = input('Please input:')
	for x in filtered_words.split('\n'):
		if x in input_text:
			input_text = input_text.replace(x, '*'*len(x))
	print (input_text)

'''str.replace(old,new[,max])
Python replace() 方法把字符串中的old(旧字符串)替换成new(新字符串)，
如果指定了第三个参数max,则替换不超过max次。'''