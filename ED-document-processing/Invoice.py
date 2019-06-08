from docx import Document
from docx2txt import*

document = Document('Invoice.docx')
table = document.tables[0]

data = []

keys = None
for i, row in enumerate(table.rows):
    text = (cell.text for cell in row.cells)
    if i == 0:
        keys = list(text)
        continue
    row_data = dict(zip(keys, text))
    data.append(row_data)

infogr =[]
for elem in data:
    infogr.append(list(dict.values(elem)))
##for x in range(len(infogr)):
##    print(x)
##    print(infogr[x])

def pars_con():
    if len(infogr[3][0].split())> 7:
        a = infogr[3][0].split()[6] + " " + infogr[3][0].split()[7]
    else:
        a = infogr[3][0].split()[6]
    return a


text = process("Invoice.docx")
a = text.split()
inv = ['04031/0']
for i in range (7, 10):
    inv.append(a[i])

Отправления = infogr[1][0].split()[-1]
proizv = infogr[2][0].split()[-1]
Назначения = pars_con()
valuta = infogr[4][-1].split()[-1]
Колтов = infogr[6][0].split()[0]
ctoim = infogr[6][-1].split()[-1]

if __name__ == "__main__":
    print(inv)
    print(Отправления)
    print(proizv)
    print(Назначения)
    print(valuta)
    print(Колтов)
    print(ctoim)


