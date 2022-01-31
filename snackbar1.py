print("-----------------------------------------------------")
print("")
print("Welkom bij Cees Patat!")
print("")
geld = 0
totaal = 0
#Vragen

vraag1 = input('Hoeveel patat (per stuk €1,75)? ')
vraag2 = input('Hoeveel frikadellen (per stuk €1,95)? ')
vraag3 = input('Hoeveel kroketten (per stuk €2,15)? ')

vg1 = int(vraag1) * 1.75
vg2 = int(vraag2) * 1.95
vg3 = int(vraag3) * 2.15

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
        print(vraag1, " stuk patat (€1,75)")
    else:
        print(vraag1, " stukken patat (€1,75)")

if int(vraag2) > 0:
    if int(vraag2) == 1:
        print(vraag2, " frikandel (€1,95)")
    else:
        print(vraag2, " frikandellen (€1,95)")
if int(vraag3) > 0:
    if int(vraag3) == 1:
        print(vraag3, " kroket (€2,15)")
    else:
        print(vraag3, " kroketten (€2,15)")
if geld < 10:
    print("bestelkosten (€1,50)")
print("------------------")
print("Totaal: €", totaal)