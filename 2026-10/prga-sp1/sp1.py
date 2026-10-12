# Tady bude tvůj kód žáka (např. IT2-07)
# 12. 10. 2026
1010
import time
import math


pocet = int(input("Zadej počet (od 5 do 15): "))


print("Kulička jede:")


for i in range(pocet):
    
    print(" " * i + "O")

    time.sleep(0.1)

for i in range(pocet):
    print(" " * (pocet - i) + "O")
    time.sleep(0.1)


print("\nTabulka:")


for i in range(1, pocet + 1):
    print(i, i * i, math.sqrt(i))
