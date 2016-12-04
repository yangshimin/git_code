# -*-coding:utf-8 -*-

import xlrd


def count(file):
    data = xlrd.open_workbook(file)
    table = data.sheets()[0]
    rowCount = table.nrows
    total_account = 0
    for i in range(1, rowCount):
        cell_value = table.cell_value(i, 3)
        total_account += int(cell_value)
    return total_account


if __name__ == '__main__':
    total_num = count('src.xls')
    print('这月的通话时间一共为%s秒' % total_num)
