frase = str(input('Digite uma frase:  ')).upper().strip()
print('Analisando a frase.....')
print('A letra A aparece {} vezes'.format(frase.count('A')))
print('A letra A aparece pela primeira vez na posição {}'.format(frase.find('A')))
print('A letra A apareceu pela ultima vez na posição {}'.format(frase.rfind('A')))
