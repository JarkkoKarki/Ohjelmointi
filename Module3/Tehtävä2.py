Hytti = str(input('Kerro hytti luokka: "LUX", "A", "B" tai "C": '))
if Hytti == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif Hytti == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif Hytti == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif Hytti == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka")