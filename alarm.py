import time
"""
Coded by ÖMER MİRAÇ KÖKÇAM
omermirac.kokcam@gmail.com

"""

print('Alarm Kurmak istediğiniz Zamanı Giriniz: ')
print('-'*40)
time.sleep(1)

saat=int(input('Saat : '))
dakika=int(input('Dakika: '))


while True:

    zaman = time.localtime(time.time())
    if (saat == zaman.tm_hour and dakika == zaman.tm_min):
        print('Alarm Çalıyor Saat:{}.{}'.format(saat,dakika))
        break
    else:
        continue
