from turtle import *
import time  # time modülü eklendi
  # Program başlamadan önce 3 saniye bekler

speed(0)  # En yüksek hız (250 yerine 0 kullan)
color('cyan')
bgcolor('black')

b = 1
time.sleep(3)  

while b <= 350:
    left(b)
    forward(b * 1)
    b += 1  

done()  # Çizim tamamlandıktan sonra pencereyi açık tutar
