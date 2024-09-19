import math
print("Berechnung eines Kreises:")
print("=========================")

r = int(input("Was ist der Radius ? "))

ufläche = math.pi * r * r
fläche = round(ufläche, ndigits=2)
uumfang = 2 * math.pi * r
umfang = round(uumfang, ndigits=2)

print("Gegeben: ", r)
print("Gesucht: Umfang, Fläche")

print("Lösung: Umfang = Pi * r * r\n"
      f"        Umfang = {umfang}\n"
      "        Fläche = 2 * pi * r\n"
      f"        Fläche = {fläche}")
