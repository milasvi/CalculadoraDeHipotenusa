import math
import emoji

print(emoji.emojize('\n\n:red_triangle_pointed_up: Calculadora de Hipotenusa :red_triangle_pointed_up:\n\n'))
while True:
    cateto1= float(input('Digite o primeiro cateto:'))
    cateto2= float(input('Digite o segundo cateto:'))
    hipotenusa= math.sqrt((cateto1 ** 2)+(cateto2 ** 2))
    print(f'A hipotenusa desse triângulo é {round(hipotenusa, 2)}')
    repeticao = input('Deseja informar outros catetos?')
    while repeticao != 'S' and repeticao != 'N':
        repeticao = input('Digite apenas "S" ou "N", ok?')
    if repeticao == 'N':
        print('Obrigade por usar a Calculadora de Hipotenusa. \nAté mais!')
        break
