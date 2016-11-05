# -*- coding:utf-8 -*-

def count_letters(file='0004.txt',ignore=[',', '.', ':', '!', '?', '”', '“', '1', '2', \
	'3', '4', '5', '6', '7', '8', '9', '0'],lower=True):
	txt = open(file).read()
	for i in ignore:
		txt = txt.replace(i,' ')
	if lower:
		txt = txt.lower()
	words = txt.split(' ')

	dic = {}
	for word in words:
		if word is ' ':
			pass
		elif word in dic:
			dic[word] += 1
		else:
			dic[word] = 1
	return dic

result = sorted(count_letters().items(),key=lambda s :s[1],reverse = True)

for i in result:
	print(i)
	#print (i[0],i[1])


"""Python replace()方法把字符串中的old(旧字符串)替换成new(新字符串)
如果指定第三个参数max,则替换不超过max次。
replace()方法语法：
	str.replace(old,new[,max])"""

"""
operator.itemgetter函数
operator模块提供的itemgetter函数用于获取对象某些维的数据，参数为一些序号
（即需要获取的数据在对象中的序号），
>>>a = [1,2,3]
>>>b = operator.itemgetter(1)     //定义函数b,获取对象的第一个域的值
>>>b(a)
2
>>>b = operator.itemgetter(1,0)	   //定义函数b，获取对象的第1个域和第0个值
>>>b(a)
(2,1)
注意：operator.itemgetter函数获取的不是值，而是定义了一个函数，通过该函数作用
到对象上才能获取值。

sorted函数
函数原型：sorted(iterable[,cmp[,key[,reverse]]])

参数解释：
1.iterable指定要排序的list或者iterable
2.cmp为函数，指定排序时进行比较的函数，可以指定一个函数或者lambda,如：
	students为类对象的list，没个成员有三个域，用sorted进行比较时可以自己定cmp函数，
	例如这里要通过比较第三个数据成员来排序，代码可以这样写：
    students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
    sorted(students, key=lambda student : student[2])
3.key为函数，指定取待排序元素的哪一项进行排序。函数用上面的例子来说明：
	sorted(students, key=lambda student : student[2])

    key指定的lambda函数功能是去元素student的第三个域（即：student[2]），因此sorted排序时，
    会以students所有元素的第三个域来进行排序。

	有了上面的operator.itemgetter函数，也可以用该函数来实现，例如要通过student的第三个域排序，可以这么写：
	sorted(students, key=operator.itemgetter(2)) 
	sorted函数也可以进行多级排序，例如要根据第二个域和第三个域进行排序，可以这么写：
	sorted(students, key=operator.itemgetter(1,2))
	即先跟句第二个域排序，再根据第三个域排序。
4.reverse参数就不用多说了，是一个bool变量，表示升序还是降序排列，默认为false（升序排列），
定义为True时将按降序排列。"""