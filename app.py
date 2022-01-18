# Projeto impar ou par
while True:
    try:
        valor = int(input('Digite um Valor:'))
        if valor % 2 == 0:
            print('Número Par')
        else:
            print('Número impar')
    except:
        print('Digite apenas números')
