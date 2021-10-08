szam1 = int(input("Ird be az első számot: "))
szam2 = int(input("Ird be az második számot: "))

if szam1 > szam2:
    kulombseg = szam1 - szam2
else:
    kulombseg = szam2 - szam1

print("Külömbség:",kulombseg)