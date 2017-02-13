# -*- coding:utf-8 -*-

import mysql.connector
import random
import string


def activation_code(id, length=10):
    '''
    id + L + 随机码
    hex(x)将一个整数转换成16进制
    [random.choice(chars) for i in range(length)]是列表解析
    '''
    prefix = hex(int(id))[2:] + 'L'
    length = length - len(prefix)
    chars = string.ascii_letters + string.digits
    code = prefix + ''.join([random.choice(chars) for i in range(length)])
    return code


def get_id(code):
    '''hex to dec'''
    return str(int(code.upper(), 16))


def create_activation_code():
    activation = []
    for i in range(1, 201):
        code = activation_code(i)
        activation.append(code)
        # id_hex = code.split('L')[0]
        # id = get_id(id_hex)
        # print(code,id)
    return activation


def insertCode(id, thecode):
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='843113495gh',
        port=3306,
        database='activation_code')
    cur = conn.cursor()
    cur.execute("insert into thecode(id, code) values('%d','%s')" % (id, code))
    conn.commit()
    cur.close()
    conn.close()


def selectCode():
    result = []
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='843113495gh',
        port=3306,
        database='activation_code')
    cur = conn.cursor()
    cur.execute('select * from thecode')
    rows = cur.fetchall()
    for row in rows:
        result.append(str(row[1]))
    return result


if __name__ == '__main__':
    codes = create_activation_code()
    id = 0
    for code in codes:
        id = id + 1
        insertCode(id, code)
    result_code = selectCode()
    print(result_code)

