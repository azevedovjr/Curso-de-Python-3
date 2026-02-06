#Faça um progama que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as infomações possiveis sobre ele.

b=input('Digite algo: ')
print('Você digitou algo da classe:', type(b))
print('Você digitou algo alfanumérico?', b.isalnum())
print('Você digitou algo numérico?', b.isnumeric())
print('Você digitou algo alfabético?', b.isalpha())
print('Está em minúsculas?', b.islower())
print('Está em maiúsculas?', b.isupper())
print('Tem espaços?', b.isspace())

