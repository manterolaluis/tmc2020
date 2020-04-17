#Mostrar mediante un programa en python que la expresión P si y solo si -P es una contradicción

valores = [False, True]

# mediante reglas p si y solo si not p se puede transformar en
# (not p or not p) and ( p or p)
# lo que equivale a not p and p

for p in valores:
    if (not p or not p) and (p or p):
        print("Este mensaje nunca lo verás")

#alternativamente

for p in valores:
    if not p and p:
        print("Este mensaje nunca lo verás")

#alternativamente

for p in valores:
    if p == (not p):
        print("Este mensaje nunca lo verás")
