#-*-coding:utf-8-*-

import random
import string

def activation_code(id,length=10):
	'''
	id + L + 随机码
	hex(x)将一个整数转换成16进制
	[random.choice(chars) for i in range(length)]是列表解析
	'''
	prefix = hex(int(id))[2:] + 'L'
	length = length - len(prefix)
	chars = string.ascii_letters + string.digits
	return prefix + ''.join([random.choice(chars) for i in range(length)])

def get_id(code):
	'''hex to dec'''
	return str(int(code.upper(), 16))

if __name__ == '__main__':
	for i in range(10,500,35):
		code = activation_code(i)
		id_hex = code.split('L')[0]
		id = get_id(id_hex)
		print (code,id)

		
'''int(x,[base]):将x(通常是一个字符串)按照base进制转换成整数。
	int('10')->转换成整数10
	int('10',16)->'10'按16进制转换，将得到整数16
	int('ff',16)->255
	int('ff')->出错，无法将字符串'ff'按照10进制转换'''

