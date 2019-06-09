from docx2txt import*
import os

text = process(os.path.join("..", "Documents", "Agreement.docx"))
a = text.split()
pasp = ['1-11001/0']
dov = ['2-11003/0 ДОВЕРЕННОСТЬ']
num_dov = ['11003/0']
pasp.append(a[a.index("уполномочивает")+1])
pasp.append(a[a.index("уполномочивает")+2])
pasp.append(a[a.index("уполномочивает")+3])
pasp.append("ПАСПОРТ")
pasp.append(a[a.index("серии")+1])
pasp.append(a[a.index("серии")+3])
pasp.append('ОТ')
pasp.append(a[a.index('проживающего')-2])
dov.append(a[a.index('N')+1])
dov.append('ОТ')
dov.append(a[a.index('N')+4])
dov.append(a[a.index('N')+5])
dov.append(a[a.index('N')+6])
dov.append('ДО')
dov.append(a[a.index('до')+1])
dov.append(a[a.index('до')+2])
dov.append(a[a.index('до')+3])
for i in range(1, len(dov)):
    num_dov.append(dov[i])

if __name__ == "__main__":
    print(pasp)
    print(dov)
    print(num_dov)
