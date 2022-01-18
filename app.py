# Projeto impar ou par
while True:
    try:
        valor = int(input('Digite um Valor:'))
        if valor % 2 == 0:
            print('Numero Par')
        else:
            print('Numero impar')
    except:
        print('Digite apenas numeros')
