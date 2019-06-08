from docx import Document
from docx2txt import*
import json

document = Document('CMR.docx')
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

def pars(ot, do, ind):
    pregr = []
    for x in range(ot, do):
        inf = infogr[x]
        pregr.append(inf[ind])
    while '' in pregr:
        pregr.remove('')
    return pregr
def ves():
    text = process("CMR.docx")
    a = text.split()
    b = a[a.index("KG")-1]
    return b
def num_cmr():
    num = ['02015/0']
    text = process('CMR.docx')
    a = text.split()
    for i in range(1, 4):
        num.append(a[i])
    return num
    
Отправитель = pars(0, 5, 0)
Отправитель.remove('\t\t')
Получатель = pars(6, 11, 0)
Перевозчик = pars(6, 11, -1)
Место_разгрузки = pars(12, 15, 1)
Место_погрузки = pars(16, 19, 1)
Документы = pars(20, 22, 0)
Товар = pars(23, 30, 0)
tamogni = pars(32, 37, 0)
oplati = pars(40, 41, 1)
oplati = oplati[0]
oplati = oplati.split()
oplata = []
oplata.append(oplati[3])
oplata.append(oplati[4])
transcp = pars(50, 51, 0)
vesy = ves()
numcmr = num_cmr()

if __name__ == "__main__":
    print(Отправитель)
    print(Получатель)
    print(Перевозчик)
    print(Место_разгрузки)
    print(Место_погрузки)
    print(Документы)
    print(Товар)
    print(tamogni)
    print(oplata)
    print(transcp)
    print(vesy)
    print(numcmr)

    resulting_json = {"Otpravitel": Отправитель,
                "Poluchatel": Получатель,
                "Perevozchik": Перевозчик,
                "Mesto_razgruzki": Место_разгрузки,
                "Mesto_pogruzki": Место_погрузки,
                "Docs": Документы,
                "Tovar": Товар,
                "tamogni": tamogni,
                "oplata": oplata,
                "transcp": transcp,
                "vesy": vesy,
                "numcmr": numcmr
                }

    with open("D:\\test_customs_json.json", 'w') as test_json:
        json.dump(resulting_json, test_json)
