import json
from Invoice import*
tvr={'3919101200' : 'Плиты, листы, пленка, лента и прочие плоские полимерные самоклеящиеся формы, в рулонах шириной не более 20 см',
     '0105140000': 'Гуси живые массой не более 185г',
     '0602400000': 'Розы живые привитые и непривитые',
     '5002000000':'Шелк-сырец (некрученый)',
     '7102210000': 'Алмазы технические, необработанные, распиленные, расколотые или грубо обработанные; пемза; наждак; корунд природный, гранат природный и прочие природные абразивы',
     '001':'test'}
stavka={'Плиты, листы, пленка, лента и прочие плоские полимерные самоклеящиеся формы, в рулонах шириной не более 20 см': [6.5, 20],
        'test': [0.5, 20],
        'Гуси живые массой не более 185г': [0,20],
        'Розы живые привитые и непривитые': [5,20],
        'Шелк-сырец (некрученый)':[5,20],
        'Алмазы технические, необработанные, распиленные, расколотые или грубо обработанные; пемза; наждак; корунд природный, гранат природный и прочие природные абразивы': [10,0]}

Цена=2000000
b=str(input("Kod plz: "))
def gr33():
    a=json.dumps(b)
    return(a)
def gr42():
    a=json.dumps(str(int(ctoim) * 65.03))
    return (a)

def gr47():
    tovar_plat=stavka[tvr[b]]
    ##Подсчет сбора за таможенное оформление
    if int(ctoim) * 65.03<200000:
        sbor=375
    elif int(ctoim) * 65.03<450000:
        sbor=750
    elif int(ctoim) * 65.03<1200000:
        sbor=1500
    elif int(ctoim) * 65.03<2500000:
        sbor=4125
    elif int(ctoim) * 65.03<5000000:
        sbor=5625
    elif int(ctoim) * 65.03<10000000:
        sbor=15000
    elif int(ctoim) * 65.03>10000000:
        sbor=22500
    ##Подсчет таможенной пощлины
    poshlina=round(int(ctoim) * 65.03/100*tovar_plat[0],2)
    print(poshlina)
    ##Подсчет налогоблагаемой базы для НДС
    baza_nds=round(poshlina+int(ctoim) * 65.03,2) 
    nds=round(baza_nds/100*tovar_plat[1],2)
    sbor47='1010   '+ str(round(int(ctoim) * 65.03,2))+'   ' + str(sbor) +'РУБ  '  + str(sbor )+'.00   '+ ' ИУ'
    poshlina47='2010   '+ str(round(int(ctoim) * 65.03,2))+'   ' + str(tovar_plat[0]) +'%  '  + str(poshlina )+'   '+ ' ИУ'
    nds47='5010   '+ str(baza_nds)+'   ' + str(tovar_plat[1]) +'%  '  + str(nds )+'   '+ ' ИУ'
    print(sbor47)
    print(poshlina47)
    print(nds47)
    ##Запись json gr47.
    a1=json.dumps(sbor47)
    a2=json.dumps(poshlina47)
    a3=json.dumps(nds47)
    b_sbor='1010-'+str(sbor)+'.00-643-123-08.06.2019-БН'
    b_poshlina='2010-'+str(poshlina)+'-643-123-08.06.2019-БН'
    b_nds='5010-'+str(nds)+'-643-123-08.06.2019-БН'
    a4=json.dumps(b_sbor)
    a5=json.dumps(b_poshlina)
    a6=json.dumps(b_nds)
    
    print(b_sbor)
    print(b_poshlina)
    print(b_nds)
    return(a1,a2,a3,a4,a5,a6)


