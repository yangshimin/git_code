import xlwt
import json

row = 0
col = 0


def read_text(file):
    with open(file, 'r') as f:
        text = f.read()
        unjson_text = json.loads(text)
        return unjson_text


def writeIntoExcel(data, name):
    row = 0
    col = 0
    wt = xlwt.Workbook(encoding='utf-8')
    wt_sheet = wt.add_sheet('MyExcel')
    for k, v in sorted(data.items(), key=lambda d: d[0]):
        wt_sheet.write(row, col, k)
        for i in v:
            col += 1
            wt_sheet.write(row, col, i)
        col = 0
        row += 1
    wt.save(name)


if __name__ == '__main__':
    data = read_text('excel.txt')
    writeIntoExcel(data, 'student.xlsx')
