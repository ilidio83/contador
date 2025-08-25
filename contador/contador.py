from statistics import median

alturas= []
generos = []
soma_alturas_m = 0
qtd_m = 0
qtd_f = 0

for i in range (15):
    print(f'\nPessoa {i+1}:')
    altura = float(input("Digite a altura (em metros):"))
    genero = input("Digite o genero (M/F):").strip().upper()

    alturas.append(altura)
    generos.append(genero)

    if genero == 'M':
        soma_alturas_m += altura
        qtd_m += 1
    elif genero == 'F':
        qtd_f += 1

maior_altura = max(alturas)
menor_altura = min(alturas)
media_m = soma_alturas_m / qtd_m if qtd_m > 0 else 0

print("\n--- RESULTADOS ---")
print(f"Maior altura do grupo: {maior_altura:.2f} m")
print(f"Menor altura do grupo: {menor_altura:.2f} m")
print(f"Média de altura dos homens: {media_m:.2f} m")
print(f"Número de mulheres: {qtd_f}")