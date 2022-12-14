
bMaior = int(input("Informe a base maior do trapézio: "))
bMenor = int(input("Informe a base menor do trapézio: "))
altura = int(input("Informe a altura do trapézio: "))

if bMaior == 0:
    print("A Base não pode ser 0(Zero)!")
elif bMenor == 0:
    print("A Base não pode ser 0(Zero)!")
else:
    area = ((bMaior + bMenor) * 2) / 2
    print(f"A área do trapézio é : {area}")





