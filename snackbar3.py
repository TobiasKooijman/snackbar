print("-----------------------------------------------------")
print("")
print("Welkom bij Cees Patat!")
print("")
geld = 0
totaal = 0
vgg1 = 1.75
vgg2 = 1.95
vgg3 = 2.15
brood = 0
frik = 0
xxl = 0
vega = 0
looper = 0
gewn = 0
#Vragen
while looper == 0:
    vraag1 = input('Hoeveel patat (per stuk €1,75)? ')
    if int(vraag1) > 0:
        saus1 = input('wilt u er saus bij? (€0,50) [ja/nee] ')
        if saus1.lower() == "ja":
            vgg1 = 2.25
            frik = 1
    vraag2 = input('Hoeveel frikadellen (per stuk €1,95)? ')
    if int(vraag2) > 0:
        saus2 = input('wilt u een gewone, XXL(€0,50) of een vega(€-0,25)? [gewoon/xxl/vega] ')
        if saus2.lower() == "xxl":
            vgg2 += 0.50
            xxl = 1
        elif saus2.lower() == "vega":
            vgg2 -= 0.25
            vega = 1
        else:
            gewn = 1
    vraag3 = input('Hoeveel kroketten (per stuk €2,15)? ')
    if int(vraag3) > 0:
        saus3 = input('wilt u daar een broodje bij?[ja/nee]')
        if saus3.lower() == "ja":
            vgg3 += 1.00 * int(vraag3)
            brood = 1

    vg1 = int(vraag1) * vgg1
    vg2 = int(vraag2) * vgg2
    vg3 = int(vraag3) * vgg3



    geld = vg1 + vg2 + vg3
    
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

    opnieuw = input('wilt u nog meer bestellen? [ja/nee] ')
    if opnieuw.lower() == "nee":
        looper = 1

#Bonnetje
print("             CEES PATAT")
print("------------------------------------")
print("    BONNETJE:")
print("")
if int(vraag1) > 0:
    if int(vraag1) == 1:
        print(vraag1, " stuk patat (€1.75)")
    else:
        print(vraag1, " stukken patat (€1.75)")
    if int(frik) > 0:
        print("met saus (€0.50 per portie)")

if int(vraag2) > 0:
    if gewn == 1:
        if int(vraag2) == 1:
            print(vraag2, " frikandel (€1.95)")
        else:
            print(vraag2, " frikandellen (€1.95)")
    if vega == 1:
        if int(vraag2) == 1:
            print(vraag2, " vega-frikandel (€1.70)")
        else:
            print(vraag2, " vega-frikandellen (€1.70)")
    if xxl == 1:
        if int(vraag2) == 1:
            print(vraag2, " XXL-frikandel (€2.45)")
        else:
            print(vraag2, " XXL-frikandellen (€2.45)")
if int(vraag3) > 0:
    if int(vraag3) == 1:
        print(vraag3, " kroket (€2.15)")
    else:
        print(vraag3, " kroketten (€2.15)")
    if int(brood) > 0:
        print("met broodje (€1,00 per stuk)")
if geld < 10:
    print("bestelkosten (€1,50)")
print("------------------")
print("Totaal: €", totaal)
