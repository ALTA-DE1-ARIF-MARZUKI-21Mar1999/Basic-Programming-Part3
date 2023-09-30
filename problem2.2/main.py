bilangan = int(input('Masukkan bilangan : '))

print("Faktor-faktor dari", bilangan, "adalah:")
for i in range(bilangan, 0,  -1):
    if bilangan % i == 0:
        print(i)