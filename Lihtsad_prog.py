from datetime import*
from calendar import*
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