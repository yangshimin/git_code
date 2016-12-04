import json
import xlwt


def readTxt(file):
    with open(file) as f:
        json_txt = f.read()
        data = json.loads(json_txt)
        return data


def writeExcel(data, name):
    row = 0
    col = 0
    wt = xlwt.Workbook(encoding='utf-8')
    wt_sheet = wt.add_sheet('MySheet')
    for k, v in sorted(data.items(), key=lambda d: d[0]):
        wt_sheet.write(row, col, k)
        col += 1
        wt_sheet.write(row, col, v)

        col = 0
        row += 1
    wt.save(name)


if __name__ == '__main__':
    data = readTxt('city.txt')
    writeExcel(data, 'city.xlsx')
