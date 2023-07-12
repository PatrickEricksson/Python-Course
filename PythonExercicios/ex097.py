def escreva(msg):
    print('-' * (len(msg) + 4))
    print(f'  {msg}')
    print('-' * (len(msg) + 4))
#Programa Principal
texto = str(input('Digite um texto: '))
escreva(texto)