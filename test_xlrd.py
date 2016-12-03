import xlrd

# 打开text_xlsx文件
data = xlrd.open_workbook('test.xlsx')
# 获取一个工作表
table = data.sheets()[0]
# table = data.sheet_by_index(0)
# table = data.sheet_by_name('1111')

# 获取工作表中第一行的数据
r_values = table.row_values(1)
# 获取工作表中第一列的数据
c_values = table.col_values(1)

# 获取行数
n_count = table.nrows
# 获取列数
c_count = table.ncols

# 获取单元格内容
cell_value = table.cell(0,1).value
print(cell_value)