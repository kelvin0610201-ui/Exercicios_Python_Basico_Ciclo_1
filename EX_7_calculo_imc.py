# Escreva um código que pede ao usuário a altura e o peso e faça o cálculo do IMC (Índice de massa corporal) do usuário.
# Dica:
# Para calcular o IMC você deve dividir o peso pela altura ao quadrado
# imc = peso / (altura ** 2)


# OUTPUT ESPERADO:

# Digite sua altura: 1.78
# Digite seu peso: 85
# O seu IMC é: 26.83

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

nome = input('qual seu nome? ')
peso = float(input('qual seu peso? '))
altura = float(input('qual sua altura? '))

imc = peso/ (altura ** 2)

print('bom seu imc é', imc)
if imc <= 18.5:
 print('Abaixo do peso')
elif imc <=24.9:
 print('Peso normal')
elif imc <29.9:
 print('Sobrepeso')
elif imc <=34.9:
 print('Obesidade grau 1')
elif imc <= 39.9:
 print('Obesidade grau 2')
elif imc <=40:
 print('Obesidade grau 3')