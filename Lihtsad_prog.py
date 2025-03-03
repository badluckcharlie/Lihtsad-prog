from datetime import*
from calendar import*
from math import*
from time import strptime
tana=date.today()
print(f"Today is {tana}")

# 27/12/2022
tana1 = tana.strftime("%d/%m/%y")
print(tana1)

# December 27, 2022
tana2 = tana.strftime("%B %d, %Y")
print(tana2)

# 27/12/2022
tana3 = tana.strftime("%m/%d/%y")
print(tana3)

# Dec-27-2022
tana4 = tana.strftime("%b-%d-%y")
print(tana3)

päev=tana.day
kuu=tana.month
aasta=tana.year

print(f"Today is {päev}/{kuu}/{aasta}")
paevad=monthrange(2025,2)[1]
onjaanud=paevad-päev
print(f"Till the end of the month {onjaanud} days are left")

print(f"Today is {päev}/{kuu}/{aasta}")
months=monthrange(2025,1)[1]
mothsleft=months-kuu
print(f"Till the end of the year {onjaanud} months are left")

try:
    sünnipäev=input("Sünnipäaev: ") #YYYY-MM-DD
    sp=datetime.strptime(sünnipaev, "%Y-%m-%d")
    print(sp)
    vanus_aastades=tana.year-sp.year
    vanus_kuudes=vanus_aastades*12
    vanus_päevades=vanus_kuudes*30
    print(f"Vastus:vanus aastades {vanus_aastades};Vanus kuudes {vanus_kuudes}; Vanus päevades {vanus_päevades}")
except:
    print("data is incorrect")


#Ülesanne 2
a1=3 + 8 / (4-2)*4
print(a1)
a2=(3+8) / 4-2*4
print(a2)
a3=(3+8) / (4-2*4)
print(a3)
a4=((3+8) / (4-2*4))
print(a4)

#Ülesanne 3  #== равенство, != не равно >, <, =>, <=

try:
    R=float(input("Enter R of round, which is Radius "))
    if R<=0:
       print("0 and negative numbers cannot be entered!")
    else:
        Round_S=pi*R**2
        Round_P=2*pi*R
        Quadrant_S=2*R*2*R
        Quadrant_P=4*2*R
        print(f"Round S {round(Round_S, 2)} , Round P {round(Round_P, 2)} , Quadrant S {Quadrant_S} , Quadrant P {Quadrant_P}")
       
except:
    print("Error! Only the numbers must be entered!")

#Ülesanne 4

Earth_Radius =float(637800000)
Coin_Radius =float(25.75)
Earth_D=2*Earth_Radius #Diameter
Earth_C=pi*Earth_D  #Round Length
Coins_Per_Earth=Earth_C/Coin_Radius
print(f"It would take {round(Coins_Per_Earth, 2)} 2 euro coins to wrap the globe around")

#Ülesanne 5

Phr_1="kill-koll".capitalize()
Phr_2="killadi-koll".capitalize()
print(2*Phr_1,Phr_2,2*Phr_1,Phr_2,4*Phr_1)

#Ülesanne 6

Text1="""Rong see sõitis tsuhh tsuhh tsuhh,
piilupart oli rongijuht.
Rattad tegid rat tat taa,
rat tat taa ja tat tat taa.
Aga seal rongi peal,
kas sa tead, kes olid seal?

Rong see sõitis tuut tuut tuut,
piilupart oli rongijuht.
Rattad tegid kill koll koll,
kill koll koll ja kill koll kill."""
print(Text1.upper())

#Ülesanne 7

S_1=float(input("Enter short side of the rectangular"))
S_2=float(input("Enter long side of the rectangular"))
P_Rect=S_1*2+S_2*2
S_Rect=S_1*S_2
print(f"You rectangular perimeter is {P_Rect} , and your square is {S_Rect}")

#Ülesanne 8

MileRange=float(input("Enter the distance you have traveled in kilometers"))
FuelConsumed=float(input("Enter the amount of fuel that has been consumed in litres"))
Consumption=MileRange/FuelConsumed
Consumption100=Consumption*100
print(f"The fuel consuption per 100 kilometers is {round(Consumption100, 3)}")

#Ülesanne 9

Roller_Speed= 29.9
Roller_Range=float(input("Enter the distance for the travel on rollers in kilometers"))
Roller_Time=Roller_Range/Roller_Speed
print(f"It would take {Roller_Time} hours to make his way to the destination")

#Ülesanne 10

minutes_user=int(input("time in minutes"))
hours=minutes_user//60
minutes=minutes_user%60
print(f"answer is {hours}:{minutes}".center(20,"*"))