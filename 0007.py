# -*- coding:utf-8 -*-

import os

def line_counts(root,file):
	result = [0,0,0]		#分别为行数、注释、空行的数目
	path = os.path.join(root,file)
	lines = open(path,'r',encoding='UTF-8').readlines()
	for line in lines:
		if line.strip().startswith('#'):
			result[1] += 1		#注释的行数
		if line[0] == '\n':
			result[2] += 1    #空行的行数
	result[0] = len(lines) - result[1] - result[2]
	return result

def file_count(root,suffix):
	py_file = [x for x in os.listdir(root) if os.path.splitext(x)[1] == suffix]
	print (py_file)
	num_count = [0,0,0]
	for file in py_file:
		num = line_counts(root,file)
		num_count[0] +=num[0]
		num_count[1] +=num[1]
		num_count[2] +=num[2]
	print('目录中共有：%s,%s,%s'%(num_count[0],num_count[1],num_count[2]))

if __name__ == '__main__':
	root = 'e:/test'
	suffix = '.py'
	file_count(root,suffix)

"""
os.path.split():函数返回一个路径的目录名和文件名的元组
os.path.splitext():函数返回了一个文件名和拓展名的元组
str.strip():
函数原型
声明：s为字符串，rm为要删除的字符序列
s.strip(rm)        删除s字符串中开头、结尾处，位于 rm删除序列的字符
s.lstrip(rm)       删除s字符串中开头处，位于 rm删除序列的字符
s.rstrip(rm)      删除s字符串中结尾处，位于 rm删除序列的字符
注意：
当rm为空时，默认删除空白符（包括'\n', '\r',  '\t',  ' ')
"""