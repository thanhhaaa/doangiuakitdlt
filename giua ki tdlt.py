from datetime import datetime
now = datetime.now()
current_hour = now.strftime("%H")
current_minute = now.strftime("%M")
current_second = now.strftime("%S")
current_day = now.strftime("%d")
current_month = now.strftime("%m")
current_year = now.strftime("%Y")
print('giờ hiện tại: ', current_hour)
print('phút hiện tại: ', current_minute)
print('giây hiện tại: ', current_second)
print('năm hiện tại: ', current_year)
print('tháng hiện tại: ', current_month)
print('ngày hiện tại: ', current_day)
gbt = int(input("nhap gio bao thuc"))
if (gbt<0) or (gbt>23):
    gbt=int(input("vui lòng nhập lại giờ báo thức"))
else:
    pbt = int(input("nhap phút bao thuc"))
    if (pbt<0) or (pbt>60):
        pbt =int(input("vui lòng nhập lại phút báo thức"))
    else:
        giaybt= int(input("nhập giây báo thức"))
        if (giaybt<0) or (giaybt>60):
            giaybt= int(input("vui lòng nhập lại giây báo thức"))
nbt =int(input("nhap nam bao thuc"))
while (nbt < int(current_year)) :
   nbt= int(input("moi nhap lai nam bao thuc"))
else :
   tbt = int(input("nhap thang bao thuc"))
   if (tbt<1) or (tbt>12):
       tbt=int(input("vui lòng nhập lại tháng báo thức"))
   else:
       ngbt = int(input("nhap ngay bao thuc"))
       kq=0
       if (nbt % 4==0):
           kq=1
       else :
           kq=2
       if (tbt==2):
           if (kq==1):
               if (ngbt<1) or (ngbt>29):
                   ngbt=int(input("vui lòng nhập lại ngày báo thức"))
               else:
                   kq=3
           else :
               if (ngbt<1) or (ngbt>28):
                   ngbt =int(input("vui lòng nhập lại ngày báo thức"))
               else :
                   kq=3
       if (tbt!=2):
           if (tbt<8):
               if (tbt%2==0):
                   if (ngbt<1) or (ngbt>30):
                       ngbt=int(input("vui lòng nhập lại ngày báo thức"))
                   else :
                       kq=3
               else:
                   if (ngbt<1) or (ngbt>31):
                       ngbt= int(input("vui lòng nhập lại ngày báo thức"))
                   else:
                       kq=3
           else:
               if ngbt<1 or ngbt>31:
                   ngbt=int(input('vui lòng nhập lại ngày báo thức'))
               else:
                   kq=3

from datetime import datetime

today = datetime.today()
print("Bây giờ là ", today.hour, " giờ ", today.minute, " phút ", today.second, " giây, ngày ", today.day,
      " tháng ", today.month, " năm ", today.year)
t1 = datetime(year=today.year, month=today.month, day=today.day, hour=today.hour, minute=today.minute,
              second=today.second)
t2 = datetime(year=nbt, month=tbt, day=ngbt, hour=gbt, minute=pbt, second=giaybt)
t3 = t2 - t1
t4 = t1 - t2
if t3 > t4:
    number_of_days = t3.days
    number_of_seconds = t3.seconds
    sogio = t3.seconds // 3600
    sophut = (t3.seconds % 3600) // 60
    sogiay = t3.seconds - (sogio * 3600 + sophut * 60)
    print("Báo thức sẽ kêu sau: ",number_of_days, "ngày" , sogio, "giờ", sophut, "phút", sogiay, "giây")
else:
    print('Thời gian đặt báo thức không hợp lệ')

flag=False
while flag==False :
   from datetime import datetime
   now = datetime.now()
   current_year = now.strftime ("%Y")
   current_month = now.strftime ("%m")
   current_day = now.strftime("%d")
   current_hour = now.strftime("%H")
   current_minute = now.strftime("%M")
   current_second = now.strftime("%S")

   if  int(current_year)==nbt and int(current_month) == tbt and int(current_day)== ngbt and int(current_hour) == gbt and int(current_minute) == pbt and int(current_second)==giaybt: 
       print('dậy đi ')
       flag = True
   else:
       flag = False

daychua=int(input('tắt báo thức nhập 1, lặp lại báo thức nhập 0: '))
if daychua==1:
    print('đã tắt báo thức')
    flag=True
else:
    test = 0
    while test == 0:
        pbl = int(current_minute) + 5
        print('báo lại sau 5 phút')
        flag=False
        while flag==False:
             from datetime import datetime
             now = datetime.now()
             current_year = now.strftime("%Y")
             current_month = now.strftime("%m")
             current_day = now.strftime("%d")
             current_hour = now.strftime("%H")
             current_minute = now.strftime("%M")
             current_second = now.strftime("%S")
             if int(current_year) == nbt and int(current_month) == tbt and int(current_day) == ngbt and int(current_hour) == gbt and int(current_minute) == pbl:
                print('dậy đi ')
                test=int(input('tắt báo thức nhập 1, hoãn báo thức nhập 0: '))
                flag = True
                if test==1:
                   print('đã tắt báo thức')
             else:
                 flag=False
