import matplotlib.pyplot as plt

# Zahlen von 0 bis 9
myList = list(range(10))

# Berechnung der Quadratzahlen
quadratzahlen = [i**2 for i in myList]

# Berechnung der Kubikzahlen
kubikzahlen = [i**3 for i in myList]

# Diagramm für Quadratzahlen
plt.plot(myList, quadratzahlen, label='Quadratzahlen', color='blue', marker='^')

# Diagramm für Kubikzahlen
plt.plot(myList, kubikzahlen, label='Kubikzahlen', color='red', marker='D')

# Diagramm einrichten und konfigurieren
plt.title('Quadratzahlen und Kubikzahlen von 0 bis 9')
plt.xlabel('Zahl')
plt.ylabel('Wert')

# Legende anzeigen
plt.legend()

# Diagramm speichern
plt.savefig('quad_kub.png')

# Diagramm anzeigen
plt.show()
