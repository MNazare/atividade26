# Exercício Python 26: Desenvolva um programa que leia o primeiro termo e a razão de uma Pogreçao Aritimetica.
# No final, mostre os 10 primeiros termos dessa progressão.

a1 = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a razão da PA: "))

for i in range(10):
    print(i)
    termo = a1 + i * r
    print(f'Termo {i+1}: {termo}')