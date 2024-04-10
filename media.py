#nome do usuario
nome=input('digite seu nome')
print('Ola,',nome)
#informaçoes para fazer a soma, criando a variavel soma para guardar as notas digitadas na variavel n
n=0
soma=0
#digitalização das 4 notas
for x in range(0,4):
    n=float(input('digite nota'))
    soma=soma+n
media=soma/2
print(nome,'Sua media é',media)
    