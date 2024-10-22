print("="*40)
print("TABUNG")
print("="*40)

PHI = 3.14
t = float(input("masukan tinggi :"))
r = float(input("masukan jari2 :"))

volume = PHI * r * r * t
LP = (2 * PHI * r * t) + (2 * 2 * PHI * r)

print("volume : ",volume, "cm3")
print("LP : ",LP, "cm2")