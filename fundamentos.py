# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 12:41:08 2019

@author: mateu
"""
'''
# QUESTÃO 1
#verificando se é triângulo
a = float(input("Valor a: "))

b = float(input("Valor b: "))

c = float(input("Valor c: "))

TorF = (abs(b-c) < a < (b+c)) and (abs(a-c) < b < (a+c)) and (abs(a-b) < c < (a+b))
if (TorF):# se for trinagulo, entre aqui!
    print("É triângulo!")
    
    #classificando o triangulo
    
    if(a == b and b==c and a==c):
        print("Equilátero")
    elif (a==b or b==c or c==a):
        print("Isósceles")
    else:
        print("Escaleno")
        
else: #caso não for, entre aqui
    print("Os 3 lados informados não formam triângulo!")


#QUESTÃO 2

valor = float(input("Valor: "))

if valor > 0:
    print("Valor positivo")
elif valor == 0:
    print("Valor Nulo")
else:
    print("Valor negativo")


QUESTÃO 3
valor = float(input("Valor: "))

if (valor%2 == 0):
    print("VALOR PAR")
else:
    print("Valor impar")



#QUESTÃO 4
n = int(input("n: "))
if n%5==0: print("divisível por 5!")


#QUESTÃO 5
sal = float(input("Salário? "))
prest = float(input("Prestação? "))

valor_max = sal*0.3

if (prest > valor_max):
    print("Emprestimo não pode ser concedido.")
else:
    print("Emprestimo OK. Sua prestação é de: ",prest," R$")


# QUESTÃO 6




a = float(input("Valor a: "))
b = float(input("Valor b: "))
c = float(input("Valor c: "))
if (a<c) and (a<b):
    MENOR = a
    if(b < c):
        INTER = b
        MAIOR = c
    else:
        INTER = c
        MAIOR = b

if (b < a) and (b < c):
    MENOR = b
    if a < c:
        INTER = a
        MAIOR = c
    else:
        INTER = c
        MAIOR = a
if (c < a) and (c < b):
    MENOR = c
    if a < c:
        INTER = a 
        MAIOR = b
    else:
        INTER = b
        MAIOR = a
print("Maior: {}, Inter: {}, Menor: {}".format(MAIOR,INTER,MENOR))


#QUESTAO 7

a = float(input("Valor a: "))
b = float(input("Valor b: "))

if a > b:
    if a >=0:
        print(b**(2))
        print(a**0.5)
    else:
        print('a < 0!!!!!!')
if b > a:
    if b >=0:
        print(a**(2))
        print(b**0.5)
    else:
        print('b < 0!!!!!!')
    

#questao 8
idade = int(input("idade: "))
if (idade < 16):
    print("Não eleitor.")
if 18 < idade < 65:
    print("eleitor obrigatorio")
if (16<=idade<18 or idade>=65):
    print("eleitor facultativo")      


#questão 9

valor = int(input("Valor entre 1 e 12:\n"))

if(1 =< valor =< 12):
    print("Valor: ", valor)
else:
    print("Não existe mes com esse valor")


  
  #REPETIÇÃO
  #questao 1


maior = 0
menor = 99999
for i in range(10):
  n = int(input("valor: "))
  if (n > maior):
    maior = n
  if (n < menor):
    menor = n
print('maior: ', maior, 'menor: ', menor)

  
#questao 2
    
print('100 Cachorro quente 1,10 \n101 Bauru simples 1,30 \n102 Bauru c/ovo 1,50 \n103 Hamburger 1,10 \n104 Cheeseburger 1,30 \n105 Refrigerante 1,00' )

cod = int(input("Código: "))

while(cod != -999):
    preco = 1
    qte = int(input("Quantidade: "))
    if (cod == 100):
        preco = 1.1
    if(cod == 101):
        preco = 1.3
    if(cod == 102):
        preco = 1.5
    if(cod == 103):
        preco = 1.1
    if(cod == 104):
        preco = 1.3
    if(cod == 105):
        preco = 1
    print('Valor a pagar: {:.2f} R$'.format(preco * qte))
    cod = int(input("Código: "))

#questao 3
soma_pos = 0
qte_neg = 0

while(True):

    for i in range(10):
        num = int(input("numero: "))
        if num>0:
            soma_pos+=num
        if num < 0:
            qte_neg+=1
    print('soma dos positivos: ',soma_pos,'quantidade de negativos: ', qte_neg)
    if(num == -999):
        break



#questao 4
a = int(input("Valor a: "))
b = int(input("Valor b: "))

# 3**4 = 3*3*3*3
auxiliar = 1
for i in range(b):
    auxiliar*=a
print(auxiliar)



#5 questao
n = int(input("numero de medias: "))
soma = 0
for i in range(n):
    nota = float(input('nota: '))
    soma += nota
print('media: {:.2f}'.format(soma/n))
    
    


# 6 questao

n = int(input("numero: "))

# 5! = 5*4*3*2*1

aux = 1
for i in range(n):
    aux*=(n-i)
print(aux)


#7 questao
# soma = 1/1 + 3/2 + 5/3 + 7/4 + ... + 99/50
soma = 0
for i in range(0,50):
    soma += (2*i+1)/(i+1)
print(soma)


  '''










