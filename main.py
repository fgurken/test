import datetime

today = datetime.datetime.now() #Gunumuz

d20 = datetime.timedelta(days = 20) #datetime'dan 20 gun degisken tanimliyoruz
d40 = datetime.timedelta(days = 40) #datetime'dan 40 gun degisken tanimliyoruz
d60 = datetime.timedelta(days = 60) #datetime'dan 60 gun degisken tanimliyoruz
h3 = datetime.timedelta(hours = 3) #datetime'dan 3 saatlik degisken tanimliyoruz

prev20D = today - d20 #Yeni bir degiskene uygun formatta ki tanimladigimiz 20 gunu cikartiyoruz
prev40D = today - d40
prev60D = today - d60
prev3H = today - h3 #Yeni bir degiskene uygun formatta ki tanimladigimiz 3 saati cikartiyoruz

print(prev20D)
print(prev40D)
print(prev60D)
print(prev3H)

