lista_mage = ["Raka situps", "Diagonala situps, böjda ben", "Diagonala situps, raka ben", "Raka crunch", "Laterala crunch", "Vaggan, statiskt", "Mountain climber, raka", "Mountain climber, knä utanför armen", "Bensänkningar", "Cykelcrunch", "Cykling åt sidorna"]
lista_rygg = ["Albatross, framåtlutad", "Raka rygglyft, händer under hakan", "Sneda rygglyft, händer vid öronen", "Diagonala rygglyft", "Benlyft på mage, dubbla", "Benlyft på mage, ett i taget", "Armdrag växelvis bakåt"]
lista_ben = ["Jägarvila", "Jägarvila med bensträckning", "Squats", "Statisk knäböj m hällyft", "Lunges, framåt", "Lunges, sidan", "Reverse lunge", "Knäböj med hopp", "Knäböj, ta i golvet", "Stående benlyft snett bakåt", "Höftlyft", "Höftlyft m bensträckning", "Tåhävning", "Tå-hälgång", "Step Ups", "Step Ups m frånskjut", "Step Ups m knäuppdrag"]
lista_armar = ["Armhävning", "Armhävning m vridning", "Armhävning med armbågslyft", "Breda armhävningar", "Sneda armhävningar", "Armsträckning, framåtlutad", "Armlyft åt sidan", "Tricep Dips", "Tricep Dips med bensträckning"]
lista_total_styrka = ["Burpees", "Burpees m armhävning", "Burpees på rygg", "Plankan m hällyft", "Fyrfota tåtouch", "Sidlyft, stående på ett knä", "Larvgång", "Sittgång"]
lista_kondition = ["Höga knäuppdragningar på stället", "Hälkickar", "Superstarhopp, jämfota", "Superstarhopp, växelvis", "Jämfotahopp i sidled", "Jumping Jacks", "Diagonala skidhopp", "Squats med dubbelstuds", "Grapewine", "Boxning på stället", "Skridskohopp", "Twisthopp"]
import random

print("Hej mamma! Välkommen till ditt alldeles egna slumpprogram för dina träningsövningar! Nedan presenteras övningarna för just detta passet. Kör hårt! Love you <3")


#Nedan är första omgången av övningar från alla sex grupper

ovning_mage_1 = random.choice(lista_mage)
ovning_rygg_1 = random.choice(lista_rygg)
ovning_ben_1 = random.choice(lista_ben)
ovning_armar_1 = random.choice(lista_armar)
ovning_total_styrka_1 = random.choice(lista_total_styrka)
ovning_kondition_1 = random.choice(lista_kondition)

print("1:a övningen: ", ovning_mage_1)
print("2:a övningen: ", ovning_rygg_1)
print("3:e övningen: ", ovning_ben_1)
print("4:e övningen: ", ovning_armar_1)
print("5:e övningen: ", ovning_total_styrka_1)
print("6:e övningen: ", ovning_kondition_1)


#Nedan är andra omgången av övningar från alla sex grupper

ovning_mage_2 = random.choice(lista_mage)
if (ovning_mage_2 != ovning_mage_1):
    print("7:e övningen: ", ovning_mage_2)
else:
    ovning_mage_2 = random.choice(lista_mage)
    print("7:e övningen: ", ovning_mage_2)
    
ovning_rygg_2 = random.choice(lista_rygg)
if (ovning_rygg_2 != ovning_mage_1):
    print("8:e övningen: ", ovning_rygg_2)
else:
    ovning_rygg_2 = random.choice(lista_rygg)
    print("8:e övningen: ", ovning_rygg_2)
    
ovning_ben_2 = random.choice(lista_ben)
if (ovning_ben_2 != ovning_ben_1):
    print("9:e övningen: ", ovning_ben_2)
else:
    ovning_ben_2 = random.choice(lista_ben)
    print("9:e övningen: ", ovning_ben_2)

ovning_armar_2 = random.choice(lista_armar)
if (ovning_armar_2 != ovning_armar_1):
    print("10:e övningen: ", ovning_armar_2)
else:
    ovning_armar_2 = random.choice(lista_armar)
    print("10:e övningen: ", ovning_armar_2)

ovning_total_styrka_2 = random.choice(lista_total_styrka)
if (ovning_total_styrka_2 != ovning_total_styrka_1):
    print("11:e övningen: ", ovning_total_styrka_2)
else:
    ovning_total_styrka_2 = random.choice(lista_total_styrka)
    print("11:e övningen: ", ovning_total_styrka_2)
    
ovning_kondition_2 = random.choice(lista_kondition)
if (ovning_kondition_2 != ovning_kondition_1):
    print("12:e övningen: ", ovning_kondition_2)
else:
    ovning_kondition_2 = random.choice(lista_kondition)
    print("12:e övningen: ", ovning_kondition_2)


#Nedan är tredje omgången av övningar från alla sex grupper

ovning_mage_3 = random.choice(lista_mage)
if (ovning_mage_3 != ovning_mage_2):
    print("13:e övningen: ", ovning_mage_2)
else:
    ovning_mage_3 = random.choice(lista_mage)
    print("13:e övningen: ", ovning_mage_3)
    
ovning_rygg_3 = random.choice(lista_rygg)
if (ovning_rygg_3 != ovning_mage_2):
    print("14:e övningen: ", ovning_rygg_3)
else:
    ovning_rygg_3 = random.choice(lista_rygg)
    print("14:e övningen: ", ovning_rygg_3)
    
ovning_ben_3 = random.choice(lista_ben)
if (ovning_ben_3 != ovning_ben_2):
    print("15:e övningen: ", ovning_ben_3)
else:
    ovning_ben_3 = random.choice(lista_ben)
    print("15:e övningen: ", ovning_ben_3)

ovning_armar_3 = random.choice(lista_armar)
if (ovning_armar_3 != ovning_armar_2):
    print("16:e övningen: ", ovning_armar_3)
else:
    ovning_armar_3 = random.choice(lista_armar)
    print("16:e övningen: ", ovning_armar_3)

ovning_total_styrka_3 = random.choice(lista_total_styrka)
if (ovning_total_styrka_3 != ovning_total_styrka_2):
    print("17:e övningen: ", ovning_total_styrka_3)
else:
    ovning_total_styrka_3 = random.choice(lista_total_styrka)
    print("17:e övningen: ", ovning_total_styrka_3)
    
ovning_kondition_3 = random.choice(lista_kondition)
if (ovning_kondition_3 != ovning_kondition_2):
    print("18:e övningen: ", ovning_kondition_3)
else:
    ovning_kondition_3 = random.choice(lista_kondition)
    print("18:e övningen: ", ovning_kondition_3)
