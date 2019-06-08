import json
from CMR import *
from Contract import *
from Invoice import *
from Agreement import *
from gr47 import *

sokr_cntr_lst = {'RUSSIA': 'RU', 'SWITZERLAND': 'SW', 'Australia': 'AUS'}
cntr_lst = {'RUSSIA': 'РОССИЯ', 'SWITZERLAND': 'ШВЕЙЦАРИЯ', 'Australia': 'Австралия'}


def gr1_1():
    a = json.dumps('ИМ')
    return (a)


def gr1_2():
    a = json.dumps('40')
    return (a)


def gr1_3():
    a = json.dumps('ЭД')
    return (a)


def gr2():
    c = ' '.join(Отправитель)
    a = json.dumps(c)
    return (a)


def gr3():
    a = json.dumps('1/1')
    return (a)


def gr5():
    a = json.dumps('1')
    return (a)


def gr6():
    x = list(Товар[0])
    a = json.dumps(x[0])
    return (a)


def gr8_1():
    b = inn + '/' + kpp
    a = json.dumps(b)
    return (a)


def gr8_2():
    a = json.dumps(Получатель)
    return (a)


def gr8_3():
    a = json.dumps(ogrn)
    return (a)


def gr9_1():
    b = inn + '/' + kpp
    a = json.dumps(b)
    return (a)


def gr9_2():
    a = json.dumps(Получатель)
    return (a)


def gr9_3():
    a = json.dumps(ogrn)
    return (a)


def gr11_1():
    a = json.dumps(sokr_cntr_lst[Отправитель[3]])
    return (a)


def gr11_2():
    a = json.dumps(cntr_lst[Отправитель[3]])
    return (a)


def gr12():
    a = json.dumps(str(int(ctoim) * 65.03))
    return (a)


def gr14_1():
    b = inn + '/' + kpp
    a = json.dumps(b)
    return (a)


def gr14_2():
    a = json.dumps(Получатель)
    return (a)


def gr14_3():
    a = json.dumps(ogrn)
    return (a)


def gr15_1():
    a = json.dumps(sokr_cntr_lst[Отправитель[3]])
    return (a)


def gr15_2():
    a = json.dumps(cntr_lst[Отправитель[3]])
    return (a)


def gr16():
    a = json.dumps(cntr_lst[proizv])
    return (a)


def gr16_2():
    a = json.dumps(sokr_cntr_lst[proizv])
    return (a)


def gr17_2():
    a = json.dumps('RU')
    return (a)


def gr17_2():
    a = json.dumps(cntr_lst[Получатель[3]])
    return (a)


def gr18_1():
    b = "1:" + transcp[0]
    a = json.dumps(b)
    return (a)


def gr18_2():
    a = json.dumps('00')
    return (a)


def gr19():
    a = json.dumps('1')
    return (a)


def gr20():
    c = ' '.join(oplata)
    a = json.dumps(c)
    return (a)


def gr21_1():
    b = "1:" + transcp[0]
    a = json.dumps(b)
    return (a)


def gr21_2():
    a = json.dumps('00')
    return (a)


def gr22_1():
    a = json.dumps(valuta)
    return (a)


def gr22_2():
    a = json.dumps(ctoim)
    return (a)


def gr23():
    a = json.dumps('65.03')
    return (a)


def gr24_1():
    a = json.dumps('010')
    return (a)


def gr24_1():
    a = json.dumps('00')
    return (a)


def gr25():
    a = json.dumps('31')
    return (a)


def gr26():
    a = json.dumps('31')
    return (a)


def gr29():
    a = json.dumps(tamogni[0:2])
    return (a)


def gr30():
    a = json.dumps(tamogni[2::])
    return (a)


def gr31():
    a = json.dumps(tvr[b])
    return (a)


def gr32():
    a = json.dumps('1')
    return (a)


def gr34():
    a = json.dumps(sokr_cntr_lst[Отправитель[3]])
    return (a)


def gr35():
    a = json.dumps(vesy)
    return (a)


def gr36():
    a = json.dumps('ОООО-ОО')
    return (a)


def gr37():
    a = json.dumps('4000 000')
    return (a)


def gr38():
    a = json.dumps(vesy)
    return (a)


def gr41():
    a = json.dumps('ШТ/975')
    return (a)


def gr43():
    a = json.dumps('1')
    return (a)


def gr44():
    b = ' '.join(contr) + '\n' + ' '.join(inv) + '\n' + ' '.join(numcmr) + '\n' + ' '.join(num_dov)
    a = json.dumps(b)
    return (a)


def gr45():
    a = json.dumps(str(int(ctoim) * 65.03))
    return (a)


def gr46():
    a = json.dumps(ctoim)
    return (a)


def gr54():
    b = ' '.join(pasp) + '\n' + ' '.join(dov) + '\n'
    # print(b)
    a = json.dumps(b)
    return (a)
