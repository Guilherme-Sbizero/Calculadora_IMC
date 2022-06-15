''' < 16 magreza grave
16 a < 17 Magreza moderada
17 a < 18,5 Magreza leve
18,5 a < 25 Saudável
25 a < 30 Sobrepeso
30 a < 35 Obesidade Grau 1 
35 a < 40 Obesidade Grau 2 (Severa)
=> 40 Obesidade Grau 3 (Mórbida)
'''
# Cáculo do Indice de Massa Corporal IMC
import os

altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em Kg: "))

imc = peso / altura**2

print("Seu IMC é: %.4f" % imc)

if imc < 16:
    print("Magreza grave")
elif imc < 17:
    print("Magreza moderada")
elif imc < 18.5:
    print("Magreza leve")
elif imc < 25:
    print("Saudável")
elif imc < 30:
    print("Sobrepeso")
elif imc < 35:
    print("Obesidade Grau 1")
elif imc < 40:
    print("Obesidade Grau 2 (severa)")
else:
    print("Obesidade Grau 3 (mórbida)")

    os.system("pause")
