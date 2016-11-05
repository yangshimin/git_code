#-*- coding:utf-8 -*-
result = []

texts = open('filtered_words.txt','r').readlines()
words = input('Please input:')

for word in texts:
	result.append(word.strip()) #str.strip(rm)当rm为空时，默认删除空白符包括('\n','\r','\t',' ')
if words in result:
	print('Freedom')
else:
	print('Human Rights')
