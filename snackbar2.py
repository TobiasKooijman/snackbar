print("-----------------------------------------------------")
print("")
print("Welkom bij Cees Patat!")
print("")
geld = 0
totaal = 0
vgg1 = 1.75
vgg2 = 1.95
vgg3 = 2.15

#Vragen

vraag1 = input('Hoeveel patat (per stuk €1,75)? ')
if int(vraag1) > 0:
    saus1 = input('wilt u er saus bij? (€0,50) [ja/nee] ')
    if saus1.lower() == "ja":
        vgg1 = 2.25
vraag2 = input('Hoeveel frikadellen (per stuk €1,95)? ')
if int(vraag2) > 0:
    saus2 = input('wilt u een gewone, XXL(€0,50) of een vega(€-0,25)? [gewoon/xxl/vega] ')
    if saus2.lower() == "xxl":
        vgg2 += 0.50
    if saus2.lower() == "vega":
        vgg2 -= 0.25
vraag3 = input('Hoeveel kroketten (per stuk €2,15)? ')

vg1 = int(vraag1) * vgg1
vg2 = int(vraag2) * vgg2
vg3 = int(vraag3) * vgg3



geld = vg1 + vg2 + vg3
print(geld)
if geld < 11:
    totaal += 1.50
    totaal += geld
elif 40 >= geld <= 99:
    totaal = geld * 0.95
elif geld > 100:
    totaal = geld * 0.925
else:
    totaal = geld
round(int(totaal))

#Bonnetje
print("             CEES PATAT")
print("------------------------------------")
print("    BONNETJE:")
print("")
if int(vraag1) > 0:
    if int(vraag1) == 1:
        print(vraag1, " stuk patat (€",vgg1,")")
    else:
        print(vraag1, " stukken patat (€",vgg1,")")

if int(vraag2) > 0:
    if int(vraag2) == 1:
        print(vraag2, " frikandel (€",vgg2,")")
    else:
        print(vraag2, " frikandellen (€",vgg2,")")
if int(vraag3) > 0:
    if int(vraag3) == 1:
        print(vraag3, " kroket (€",vgg3,")")
    else:
        print(vraag3, " kroketten (€",vgg3,")")
if geld < 10:
    print("bestelkosten (€1,50)")
print("------------------")
print("Totaal: €", totaal)