import json
import xlwt


def readTxt(file):
    with open(file) as f:
        jsonText = f.read()
        data = json.loads(jsonText)
        return data


def writeExcel(data, name):
    wt = xlwt.Workbook(encoding='utf-8')
    wt_sheet = wt.add_sheet('Mysheet')

    col = 0
    row = 0

    for k in data:
        for j in k:
            wt_sheet.write(row, col, j)
            col += 1
        col = 0
        row += 1
    wt.save(name)


if __name__ == '__main__':
    data = readTxt('numbers.txt')
    writeExcel(data, 'numbers.xlsx')
