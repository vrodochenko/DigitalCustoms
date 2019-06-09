import os
from docx2txt import*
text = process(os.path.join("..", "Documents", "Contract.docx"))
a = text.split()
contr = ['03011/0']
ogrn = a[a.index("ОГРН")+1]
inn = a[a.index("ИНН")+1]
kpp = a[a.index("КПП")+1]
contr.append(a[6])
contr.append('ОТ')
contr.append(a[8])


